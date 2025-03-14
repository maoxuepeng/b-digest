---
key: 20230510
tags: 防止吃狗粮过度-针对“AWS-Prime-Video-从微服务转为单体架构成本降低90%”的观点
published: true
---

近期一篇AWS Prime Video技术团队发布的文章“AWS-Prime-Video-从微服务转为单体架构成本降低90%”在圈子内引发大家讨论，这篇文章本身有一些标题党的味道，Prime Video所采用的架构本身存在问题，完全是架构师技术选择错误导致的。<!--more-->

## 事件回顾

2023年3月22日，AWS Prime Video团队发布一篇博客：[Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90) ，副标题为： ```The move from a distributed microservices architecture to a monolith application helped achieve higher scale, resilience, and reduce costs.```

文章要点是 Prime Video有一个检测视频质量的程序，从分布式的微服务架构转为了单体架构，成本降低了90%。

有两个原因促使转为单体架构：
1. 存在扩展性瓶颈
2. 费用太高

这篇文章在圈子里引发了不小的讨论，微服务架构是不是不过时了，又要回到单体架构了，等等。

这次不讨论微服务架构的好与坏，实际上这篇文章标题党的成分很大，吃瓜群众容易被误导。

## 技术分析

Prime Video的视频质量检测程序是从视频流拆解视频帧，发现存在质量问题的视频帧则发保存起来并发送通知，用于视频质量改进的输入。

Prime Video的架构团队使用了如下架构来实现此程序：

![](/images/AWS-Prime-Video-Arch.png)

根据程序需要完成的功能，稍微有经验的程序员都能看出来，选择这种架构模式背后肯定是有**非技术力量干预**。

1. 首先这个程序很简单，估计2000行代码就自闭环了。
2. 拆分成多个函数之后，由于函数是无状态的，因此就只能把状态数据存到S3，这就导致了频繁下载S3文档从而费用很高。
3. 功能之间强耦合，使用Step Function调用频度很高，容易达到账号的配额上线，因此扩展性存在问题。


## 吃狗粮过度

为什么这么简单一个程序架构师要采用这个复杂的架构模式，这背后肯定有非技术力量的干预，很大一个可能就是 **“吃狗粮”**。

AWS Lambda 是作为 AWS Serverless 计算的主力产品在推广，如果要 host serverless应用在AWS上，那么主推的一定是Lambda。

要给外部客户讲成功故事让客户上车，那么就得有人站台表示已经大规模使用了，毕竟谁都不原因是小白鼠。

在Twitter上关于这个话题的讨论，有一些观点也是认为Lambda用来host应用程序并不合适：

![](/images/AWS-Prime-Video-2.png)

![](/images/AWS-Prime-Video-3.png)

## Reference

[Scaling up the Prime Video audio/video monitoring service and reducing costs by 90%](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90)

[Microservices architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/simple-microservices-architecture-on-aws.html)

[从微服务转为单体架构、成本降低 90%，亚马逊内部案例引发轰动！CTO：莫慌，要持开放心态](https://mp.weixin.qq.com/s/fQtAMf4BfJxdBPWDE5ygwg)

[Twitter-讨论](https://twitter.com/dvassallo/status/1654880475603935232)

