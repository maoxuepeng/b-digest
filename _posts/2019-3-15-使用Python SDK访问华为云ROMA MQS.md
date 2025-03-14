---
key: 20190315
title: 使用Python SDK访问华为云ROMA MQS
tags: ROMA Python Kafka HuaweiCloud
---

### 背景
[ROMA](https://www.huaweicloud.com/product/roma.html)是新一代企业集成平台，其中的消息集成服务MQS使用Kafka队列实现。本样例介绍如何使用ROMA服务中的MQS收发消息。

### 安装 Kafka Python SDK
使用原生的 Python SDK [confluent-kafka-python](https://github.com/confluentinc/confluent-kafka-python) ，执行 ```pip install confluent-kafka``` 完成安装。

当前只支持1.x版本的SDK，不支持0.x以及2.x版本的SDK。<!--more-->

在ubuntu1604上安装 confluent-kafka 需要安装依赖包：

```
wget -qO - https://packages.confluent.io/deb/5.1/archive.key | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://packages.confluent.io/deb/5.1 stable main"
apt-get update
apt-get install confluent-platform-2.11
apt-get install librdkafka

```

### 获取 ROMA MQS CA 证书
[ca-cert](https://github.com/ibusybox/HuaweiCloud-ROMA-Samples/blob/master/connect-mqs/hw_cloud_roma_ca.crt)

### 在 ROMA MQS 上创建 Topic
创建Topic可以设置如下参数：
- 分区数量：取值范围1-20
- 副本数量：取值范围1-3
- 老化时间：取值范围1-168小时
- 是否开启多副本同步复制模式：开启之后需要客户端将acks配置为 ```all/-1```才生效
- 是否开始同步落盘模式

### Kafka 连接配置
Kafka 配置[https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md](https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md)

### 生产消息
[producer.py](https://github.com/ibusybox/HuaweiCloud-ROMA-Samples/blob/master/connect-mqs/producer.py)

```python
from confluent_kafka import Producer


p = Producer(
    {
        # Configuration: https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
        'bootstrap.servers': '192.168.0.251:9092,192.168.0.229:9092,192.168.0.240:9092',
        'security.protocol': 'plaintext',
        'sasl.username': 'sasl-username',
        'sasl.password': 'sasl-password',
        'ssl.ca.location': '/location/of/ca'  # ca certificate location
    }
)

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

for data in ["{'hello': 'world'}"]:
    # Trigger any available delivery report callbacks from previous produce() calls
    p.poll(0)

    # Asynchronously produce a message, the delivery report callback
    # will be triggered from poll() above, or flush() below, when the message has
    # been successfully delivered or failed permanently.
    p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery report
# callbacks to be triggered.
p.flush()
```

### 消费消息
[consumer.py](https://github.com/ibusybox/HuaweiCloud-ROMA-Samples/blob/master/connect-mqs/consumer.py)

```python
from confluent_kafka import Consumer, KafkaError


c = Consumer({
    # Configuration: https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    'bootstrap.servers': '192.168.0.251:9092,192.168.0.229:9092,192.168.0.240:9092',
    'security.protocol': 'plaintext',
    'sasl.username': 'sasl-username',
    'sasl.password': 'sasl-password',
    'ssl.ca.location': '/location/of/ca',  # ca certificate location   
    'group.id': 'mygroup',  # this is the comsumer group
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mytopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if not msg.error():
        print('Received message: {}'.format(msg.value().decode('utf-8')))
    elif msg.error().code() == KafkaError._PARTITION_EOF:
        print("Consumer error: reached the broker EOF")
    else:
        print("Consumer error: {}".format(msg.error()))

c.close()
```

上述代码是自动确认消费，如果希望根据业务逻辑处理结果来判断是否提交消费结果，可以设置为手动提交。具体参考[官方文档](https://docs.confluent.io/2.0.0/clients/consumer.html)。

另外，上述消费代码，在每次消费完消息后，会得到一个 Broker EOF 的错误，具体参考[此ISSUE](https://github.com/confluentinc/confluent-kafka-python/issues/283)。这个错误不影响消费，可以忽略。
