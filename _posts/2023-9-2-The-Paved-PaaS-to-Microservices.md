---
key: 20230902
tags: PaaS Microservices
title: The Paved PaaS to Microservices at Netflix
published: true
---

这是Netflix工程师肖雨浓在QCron 2017年大会上的演讲，讲述了Netflix大规模微服务架构实践。2017年距今已经有5年了，往回看这个演讲内容，到如今并没有发生什么变化。<!--more-->

## Netflix 业务相关的几个数字

1. 服务全球190个国家
2. 1亿1千万付费用户
3. 每天播放的视频流时长为1亿2千5百万小时
4. 占据北美1/3的流量

![](/images/paved-path/PavedPaaSAtNetflix-001.png)

![](/images/paved-path/PavedPaaSAtNetflix-002.png)

![](/images/paved-path/PavedPaaSAtNetflix-003.png)

## 支撑上述业务应用架构实践：The Paved PaaS

Paved PaaS 包含3部分：

1. 标准组件 Standarized Components
2. 预集成好的平台 Preassembled Platform
3. 自动化与工具 Automation and tooling

### 标准组件

将微服务公共能力封装为标准组件。包括 RPC调用、注册发现、配置、日志、调用链等。

对于一个大型系统来说，标准化对于缩短问题定位与修复时间、提升系统韧性方面至关重要。作者举了一个例子，你能想象如何在下面这种应用系统里定位问题吗？

![](/images/paved-path/PavedPaaSAtNetflix-007.png)

### 有了标准组件，需要预集成平台

大部分工程师并不清楚微服务是如何构建的，他们需要的是预构建好可工作的微服务（填充业务）。

作者举了一个例子，宜家家具，虽然提供了完整的安装指导书，但是也只有少部分人能安装好。


![](/images/paved-path/PavedPaaSAtNetflix-010.png)

![](/images/paved-path/PavedPaaSAtNetflix-011.png)

![](/images/paved-path/PavedPaaSAtNetflix-012.png)

![](/images/paved-path/PavedPaaSAtNetflix-013.png)

因此，需要这种预集成好的开发体验，开箱即用。

![](/images/paved-path/PavedPaaSAtNetflix-005.png)

### 自动化工具

加速从需求到上线的过程。


![](/images/paved-path/PavedPaaSAtNetflix-009.png)
![](/images/paved-path/PavedPaaSAtNetflix-008.png)

## 启示

我们现在所处的千行百业数字化时代，最后一公里由大量行业软件厂商完成，这些软件厂商需要的是这么一套 **Paved PaaS** 。

在开发框架领域，Spring 就提供面向开发者的一套 Paved PaaS，同时配套的是VMWare Tanzu平台；对于公有云厂商来说，如何把Spring这一套应用对应的“平台”做好，就显得很重要。

## Reference

[The "Paved Road" PaaS for Microservices at Netflix: Yunong Xiao at QCon NY](https://www.infoq.com/news/2017/06/paved-paas-netflix/)

[演讲材料](/archives/netflix/the-paved-paas-to-microservices-at-netflix-ias2017-nanjing.pdf)
