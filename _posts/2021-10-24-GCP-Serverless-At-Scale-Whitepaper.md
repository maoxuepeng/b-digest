---
key: 20211024
title: GCP Serverless at Scale
tags: Cloud Google Serverless
---

介绍GCP Serverless应用弹性伸缩场景与最佳实践。<!--more-->

## 场景与技术手段

Google 的 Serverless 服务有 ```Cloud Function```，```Cloud Run```。Serverless 最显著特性是极致弹性伸缩、或者说无限的弹性力。结合实际场景，弹性能力会有哪些限制？Google总结Serverless弹性伸缩的场景与实践指导，汇总为《Serverless at scale: From design to production》这个白皮书文档。

### Cloud Function vs Cloud Run

此白皮书涵盖的范围是Serverless，包含Cloud Function与Cloud Run两个服务，我们需要先判别一下这两个服务使用场景上的区别。

- Cloud Run 部署源是容器镜像，对开发语言、框架、库都没有限制；而Cloud Function是一段代码，对开发语言、框架、库都有约束。
- Cloud Run 请求超时时间可达60分钟；而Cloud Function是9分钟。
- Cloud Run 支持将多个请求并发发送到一个实例；而Cloud Function只支持一次发送一个请求到一个实例。也就是说Cloud Run支持更大的并发。

因此，如果对容器镜像很熟悉，又不希望受框架和开发语言限制，那么Cloud Run是一个很好的选择。如果能接受Cloud Function的约束，不想构建镜像，那么Cloud Function是更好的选择。

### Serverless 应用弹性模式

提出了4种弹性模式，如下图。

![弹性模式](/images/gcp/GCP_Serverless_Scale.max-700x700.png)

1. 无弹性模式。
2. 实例内弹性模式。
3. 多实例水平弹性模式。
4. 多实例与周边协同的弹性模式。

### 弹性的场景与技术手段

#### 1. 配置最大实例数量以适配连接数限制

连接数限制的典型场景是数据库连接数，实例依赖的的数据库连接数假设最大为100，那么实例最大并发数就需要小于100。Cloud Function支持[最大实例数配置](https://cloud.google.com/functions/docs/max-instances)。

#### 2. 使用Cloud Task应对后端依赖服务的流控限制

在流控场景下，最需要关注的是流控限制。典型的如实例的逻辑依赖一个外部API，此API有流控限制，如XX次/分钟。这种场景下使用[Cloud Task](https://cloud.google.com/tasks/docs/dual-overview)实现流控，避免超出流控导致调用失败。Cloud Task支持[速率与并发两种流控策略](https://cloud.google.com/tasks/docs/creating-queues#rate)。

#### 3. 使用有状态存储方式延后获取长时操作的结果

有一些场景需要延后处理请求，但是最终还是需要将结果提供给调用者。这时候需要引入有状态的服务来跟踪异步任务，Google API提供了[long-running operation](https://aip.dev/151) 模式。典型的场景是视频处理场景，

#### 4. 使用Redis实现流控

Serverless 应用通常是无状态的，需借助外部有状态服务实现限流。

#### 5. 使用Cloud Pub/Sub批量处理请求

在处理大量消息场景下，不希望每个消息单独处理，而是定时获取一批消息批量处理。使用Google Cloud Pub/Sub来存储消息，使用[Google Cloud Scheduler](https://cloud.google.com/scheduler/)定时触发、获取消息并处理。同时还可以通过累积的消息数量与累积时间来触发执行。

#### 6. 使用Cloud Run应对重I/O的任务

Serverless 场景下，CPU时间（cpu/内存）是费用中占大头的部分，cpu使用率越高代表钱没有浪费。对于**"重I/O"**的场景下，CPU时间大部分都耗费在I/O等待上，那么钱也就浪费了。

这种场景下，使用Cloud Run，Cloud Run支持指定"[并发处理数量](https://cloud.google.com/run/docs/about-concurrency)"。
举例说明，假如实例处理逻辑大部分时间消耗在等待依赖的外部API调用，Cloud Run可以支持配置为一个实例并行处理80个请求，从而提升CPU时间利用率。

## 最佳实践

汇总上述6中场景与对应的技术手段，参考下面这个决策树，针对场景选择合适的技术方案。

![](/images/gcp/gcp_serverless_scale_flow.png)

上图中红色箭头表示**No**，绿色箭头表示**Yes**。

## Reference

[6 strategies for scaling your serverless applications](https://cloud.google.com/blog/products/serverless/6-strategies-for-scaling-your-serverless-applications)

[Cloud Run: What no one tells you about Serverless (and how it's done)](https://cloud.google.com/blog/topics/developers-practitioners/cloud-run-story-serverless-containers)