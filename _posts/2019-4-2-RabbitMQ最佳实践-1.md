---
key: 20190402
title: RabbitMQ最佳实践-1
tags: RabbitMQ 云最佳实践  
published: false
---

使用RabbitMQ消息队列时两个重要的考虑因素是：吞吐与可靠。有的场景要求高吞吐，有的场景要求高可靠。在系统设计时候如何平衡消息队列的的吞吐量与可靠性，是使用好RabbitMQ消息队列的关键。
这篇文章列出RabbitMQ的最佳实践，基于吞吐量与可靠性两个指标，给出怎么做是好的、怎么做是差的指导，包括队列大小、常见错误、延迟加载队列、预提取值、连接与通道、集群节点数量等，这些指导都是在实践中总结出来的。<!--more-->

### 队列 Queues

#### 队列尽可能短
队列过长的话会占用系统较多内存，RabbitMQ为了释放内存，会将队列消息转储到硬盘，称为 **page out** 。 如果队列很长，Page out 操作会消耗较长时间，page out 过程中队列不能处理消息。

队列过长同时会加长RabbitMQ重启时间，因为启动时候需要重建索引。
队列过长还会导致集群之间节点同步消息时间变长。

#### 启用 lazy queue 使得性能可预期
RabbitMQ3.6版本引入了 **lazy queue** 特性， lazy queue 开启之后队列中的消息自动存储到磁盘，消息只在需要的时候才加载到内存中。开启了 lazy queue 后内存使用量会降低，但是会增加消息处理时延。

在实践中我们观察到开启了 lazy queue 后RabbitMQ集群会更稳定，性能也更可预期。消息不会突然在没有预警的情况下被写到磁盘，也不会出现突发性能毛刺。如果你一次批量往队列写入大量消息，或者消费者对消息时延不敏感，建议启动 lazy queue 。

#### 通过 TTL 或 max-length 限制队列大小
通过设置 TTL 或 max-length 来限制队列大小，从而让队列不超过设定大小。

#### 队列数量
RabbitMQ中一个队列对应一个线程，一个队列的吞吐量大约为50k消息/秒。在多核服务器上，使用多个队列与消费者可以获得更好的吞吐量，将队列数量设置为等于服务器cpu核数将获得最佳吞吐量。

#### 将队列分布到不同的CPU核，甚至不同节点
队列的性能极限是一个CPU核处理能力，因此，将队列分布到不同的CPU核（集群模式下可以到不同节点），将获得更好的性能。
RabbitMQ队列被绑定到第一个节点上，即使创建了集群，所有消息也是被投递到主队列所在的节点。你可以手动调整队列到不同的节点，但是带来的负面影响是你要管理这个映射关系。

有两个插件可以辅助实现队列分布到不同节点或不同CPU和（单节点集群）。

##### Consistent hash exchange plugin
[Consistent hash exchange plugin](https://github.com/rabbitmq/rabbitmq-consistent-hash-exchange) 插件可以实现 Exchange 按照负载均衡方式投递消息到队列中。插件将要投递消息的 Routing Key 哈希之后找到要投递的队列，这种方式能保证同一个 Routing key 的消息总是投递到同一个队列。
使用插件时候需要注意，消费者需要在多个队列上消息分析，不要有遗漏。

##### RabbitMQ sharding
[RabbitMQ sharding](https://github.com/rabbitmq/rabbitmq-sharding) 插件自动完成消息的分区，一旦在 Exchange 上定义了分区，插件会在集群的每个节点上创建一个分区队列；同时RabbitMQ sharding 插件对消费者只提供一个队列（但是实际后端有多个队列）。RabbitMQ sharding 插件提供消息生产与消费的中心访问点，并提供消息跨节点自动分区、管理节点上的队列等能力。

#### 临时队列名字系统自动分配
给队列取一个有意义的名字很关键，生产者与消费者之间通过名字找到队列。但是对于临时队列，名字就交由给系统自动分配。

#### 自动删除不再使用的队列
生产者或消费者可能异常退出导致队列被残留，大量的残留队列会影响RabbitMQ实例的性能。RabbitMQ提供了3种自动删除队列的方法。

- 设置队列的 TTL ：如 TTL 为28天的队列，当持续28天没有被消费后会被自动删除
- 配置 auto-delete 队列： auto-delete 队列在最后一个消费者取消消费、或链接关闭后被删除
- 配置 exclusive queue： exclusive queue 只能在创建此队列的 Connection/Channel 中使用，当 Connection/Channel 关闭后队列被删除

#### 限制优先队列数量
每个优先队列会启动一个Erlang进程，过多的优先队列会影响性能，建议数量为5。

### 连接数与通道数 Connections and channels
每个连接会消耗掉大约100KB的内存（如果使用TLS会更多），成千上万的连接会导致RabbitMQ负载很高，极端情况会出现内存溢出。AMQP协议引入了Channel概念，一个连接中可以有多个Channel。
建议一个Channel对应一个线程，一个连接对应一个进程，并使用长连接。

#### 不要在多个线程之间共享Channel
很多SDK并未实现Channel的线程安全，因此不要在多个线程之间共享Channel 。

#### 不要频繁打开与关闭 Channel

#### 生产者与消费者使用独立的连接

### Acknowledgements and Confirms

### Persistent messages and durable queues

### TLS and AMQPS

### Prefetch

### HiPE

### Number of Nodes in your cluster (Clustering and High Availability)

### Routing (exchanges setup)

### Disable unused plugins

### Do not set RabbitMQ Management statistics rate mode to detailed in production

### Use updated RabbitMQ client libraries

### Use latest stable RabbitMQ and Erlang version

### Use TTL with caution

### 

### Reference
[Part 1: RabbitMQ Best Practice](https://www.cloudamqp.com/blog/2017-12-29-part1-rabbitmq-best-practice.html)
[RabbitMQ for beginners - What is RabbitMQ?](https://www.cloudamqp.com/blog/2015-05-18-part1-rabbitmq-for-beginners-what-is-rabbitmq.html)

