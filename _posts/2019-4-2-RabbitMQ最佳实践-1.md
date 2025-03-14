---
key: 20190402
title: RabbitMQ最佳实践-1
tags: RabbitMQ 云最佳实践  
---

使用RabbitMQ消息队列时两个重要的考虑因素是：吞吐与可靠。有的场景要求高吞吐，有的场景要求高可靠。在系统设计时候如何平衡消息队列的的吞吐量与可靠性，是使用好RabbitMQ消息队列的关键。
这篇文章列出RabbitMQ的最佳实践，基于吞吐量与可靠性两个指标，给出怎么做是好的、怎么做是差的指导，包括队列大小、常见错误、延迟加载队列、预提取值、连接与通道、集群节点数量等，这些指导都是在实践中总结出来的。<!--more-->

## 队列 Queues

### 队列尽可能短
队列过长的话会占用系统较多内存，RabbitMQ为了释放内存，会将队列消息转储到硬盘，称为 **page out** 。 如果队列很长，Page out 操作会消耗较长时间，page out 过程中队列不能处理消息。

队列过长同时会加长RabbitMQ重启时间，因为启动时候需要重建索引。
队列过长还会导致集群之间节点同步消息时间变长。

### 启用 lazy queue 使得性能可预期
RabbitMQ3.6版本引入了 **lazy queue** 特性， lazy queue 开启之后队列中的消息自动存储到磁盘，消息只在需要的时候才加载到内存中。开启了 lazy queue 后内存使用量会降低，但是会增加消息处理时延。

在实践中我们观察到开启了 lazy queue 后RabbitMQ集群会更稳定，性能也更可预期。消息不会突然在没有预警的情况下被写到磁盘，也不会出现突发性能毛刺。如果你一次批量往队列写入大量消息，或者消费者对消息时延不敏感，建议启动 lazy queue 。

### 通过 TTL 或 max-length 限制队列大小
通过设置 TTL 或 max-length 来限制队列大小，从而让队列不超过设定大小。

### 队列数量
RabbitMQ中一个队列对应一个线程，一个队列的吞吐量大约为50k消息/秒。在多核服务器上，使用多个队列与消费者可以获得更好的吞吐量，将队列数量设置为等于服务器cpu核数将获得最佳吞吐量。

### 将队列分布到不同的CPU核，甚至不同节点
队列的性能极限是一个CPU核处理能力，因此，将队列分布到不同的CPU核（集群模式下可以到不同节点），将获得更好的性能。
RabbitMQ队列被绑定到第一个节点上，即使创建了集群，所有消息也是被投递到主队列所在的节点。你可以手动调整队列到不同的节点，但是带来的负面影响是你要管理这个映射关系。

有两个插件可以辅助实现队列分布到不同节点或不同CPU和（单节点集群）。

#### Consistent hash exchange plugin
[Consistent hash exchange plugin](https://github.com/rabbitmq/rabbitmq-consistent-hash-exchange) 插件可以实现 Exchange 按照负载均衡方式投递消息到队列中。插件将要投递消息的 Routing Key 哈希之后找到要投递的队列，这种方式能保证同一个 Routing key 的消息总是投递到同一个队列。
使用插件时候需要注意，消费者需要在多个队列上消息分析，不要有遗漏。

#### RabbitMQ sharding
[RabbitMQ sharding](https://github.com/rabbitmq/rabbitmq-sharding) 插件自动完成消息的分区，一旦在 Exchange 上定义了分区，插件会在集群的每个节点上创建一个分区队列；同时RabbitMQ sharding 插件对消费者只提供一个队列（但是实际后端有多个队列）。RabbitMQ sharding 插件提供消息生产与消费的中心访问点，并提供消息跨节点自动分区、管理节点上的队列等能力。

### 临时队列名字系统自动分配
给队列取一个有意义的名字很关键，生产者与消费者之间通过名字找到队列。但是对于临时队列，名字就交由给系统自动分配。

### 自动删除不再使用的队列
生产者或消费者可能异常退出导致队列被残留，大量的残留队列会影响RabbitMQ实例的性能。RabbitMQ提供了3种自动删除队列的方法。

- 设置队列的 TTL ：如 TTL 为28天的队列，当持续28天没有被消费后会被自动删除
- 配置 auto-delete 队列： auto-delete 队列在最后一个消费者取消消费、或链接关闭后被删除
- 配置 exclusive queue： exclusive queue 只能在创建此队列的 Connection/Channel 中使用，当 Connection/Channel 关闭后队列被删除

### 限制优先队列数量
每个优先队列会启动一个Erlang进程，过多的优先队列会影响性能，建议数量为5。

## 连接数与通道数 Connections and channels
每个连接会消耗掉大约100KB的内存（如果使用TLS会更多），成千上万的连接会导致RabbitMQ负载很高，极端情况会出现内存溢出。AMQP协议引入了Channel概念，一个连接中可以有多个Channel。
建议一个Channel对应一个线程，一个连接对应一个进程，并使用长连接。

### 不要在多个线程之间共享Channel
很多SDK并未实现Channel的线程安全，因此不要在多个线程之间共享Channel 。

### 不要频繁打开与关闭 Channel
同样是基于性能考虑。

### 生产者与消费者使用独立的连接
这么做吞吐量更高。
当生产者发送大量消息时候RabbitMQ会将压力传递到TCP连接上，如果使用同一个连接消费消息可能会得不到确认消息。

### 大量连接与通道会影响RabbitMQ管理控制台的性能
RabbitMQ会采集每个连接与通道的指标数据并分析，然后在控制台展示，大量的连接与通道会对控制台有较大压力。

## Acknowledgements and Confirms
消息在传输过程中可能会丢失（如连接中断），这时候就需要重传。确认消息用于告知客户端与服务端何时重传消息。客户端需要发送确认消息当收到消息、或者对于重要消息是消息被处理后。消息确认对性能也有影响，在高吞吐场景下，尽量避免使用手动确认。

对于消费者，一些重要的消息，建议在消息消费逻辑处理完成后才确认，确保消息不丢失。

### 未确认消息 Unacknowledged messages
所有未确认的消息都存储在内存中，当有大量的为确认消息时候可能会将内存耗尽。一个高效的限制未确认消息的方法是设置消费者的预提取（prefetch）消息数量。可以参考RabbitMQ的 prefect 机制。

## Persistent messages and durable queues
如果消息不允许丢失，需要将队列设置为 durable ，将消息设置为 persistent 。这种方式消息与队列都会持久化到硬盘，当然相比于 transient 消息，吞吐量会下降。

## Prefetch
[prefetch](https://www.rabbitmq.com/blog/2012/05/11/some-queuing-theory-throughput-latency-and-bandwidth/) 值用于指定一次发送多少个消息给消费者。RabbitMQ官网对 prefetch 的定义：

```prefetch 的目的是使得消费者处于饱和工作状态，同时又要让消费者客户端内存缓存最少，并使得消息呆在队列中让其他消费者尽快消费。```

RabbitMQ默认不设定消费者内存缓存上限，意思是一次性发送尽量多的消息给消费者，消息在消费者客户端内存中缓存直到被处理。 Prefetch 限定消费者一次消费的消息数量， 所有 Prefetch 的消息都会从队列中删除，其他消费者不再可见。

Prefetch 的值对RabbitMQ的性能有影响。

过小的值会导致RabbitMQ将时间都花费在等待发送消息与正在发送消息过程内。下图是一个 Prefetch 设置过小，导致时间都花费在网络传输上的例子：消费者处理消息只用了5ms，但是接收消息，确认消息却耗费了120ms。

![](https://www.cloudamqp.com/img/blog/prefetch-rabbitmq-low-prefetch.png)

过大的值会导致一个消费者取走了所有消息非常繁忙，其他消费者没有消息可处理空闲等待的现象。

![](https://www.cloudamqp.com/img/blog/prefetch-rabbitmq-high-prefetch.png)


### 如何设置合适的 prefetch 值

- 消费者很少且消息处理很快：prefetch 设置尽可能大；
- 消费者很多且消息处理很快：prefetch 设置较小；比 "消费者很少且消息处理很快" 场景要小
- 消费者很多且消息处理很慢：prefetch 设置为1；这样尽可能将消息分布给不同的消费者处理

需要注意的是，**如果消费者设置了自动确认消息消费，那么 prefetch 是无效的。**

常见的错误做法是不设定 prefetch 的值，这种情况下会导致一些消费者撑死，一些消费者饿死。

## HiPE
HiPE(High Performance Erlang)开启之后可以提升吞吐量，负面影响是增加启动时间；开启了 HiPE 之后，RabbitMQ会在启动时候编译，开启 HiPE 后性能会有 20%~80% 的提升，启动时长会增加 1~3 分钟。

## Disable unused plugins
插件会消耗CPU与内存，禁用不需要的插件。

## Do not set RabbitMQ Management statistics rate mode to detailed in production
Setting RabbitMQ Management statistics rate mode to detailed has a serious performance impact and should not be used in production.

## Use updated RabbitMQ client libraries
确保你使用的SDK是最新的稳定版本。

## Use latest stable RabbitMQ and Erlang version
使用最新稳定的RabbitMQ与Erlang版本。

## Use TTL with caution
死信投递与TTL是两个流行的特性，但是这两个特性对性能会有影响，在使用时候通常容易忽视这点。

### 死信投递
队列设置了 ```x-dead-letter-exhcange``` 属性将会接收到被拒绝的、或超时的消息。消息设置了 ```x-dead-letter-routing-key``` 后 routing key 将会在死信投递后被改变。

### TTL
队列设置了 ```x-message-ttl``` 属性后，消息将会被从队列中移除如果在TTL时间内未被消费。

## Reference
[Part 1: RabbitMQ Best Practice](https://www.cloudamqp.com/blog/2017-12-29-part1-rabbitmq-best-practice.html)
[RabbitMQ for beginners - What is RabbitMQ?](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)

