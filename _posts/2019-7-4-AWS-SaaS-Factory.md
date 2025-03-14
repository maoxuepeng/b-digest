---
key: 20190704
title: AWS SaaS Factory
tags: AWS SaaS
---

[AWS SaaS Factory](https://aws.amazon.com/cn/partners/saas-factory/) 是一套方法论，指导用户如何在AWS上快速构建SaaS应用。7月4日AWS组织了一次线下SaaS Factory活动，讲解AWS SaaS Factory。<!--more-->

AWS SaaS Factory 活动这次是第二次举办，上一次是去年。讲师还特意问 [萬達寶](https://www.multiable.com/TC/home.htm) 这家公司有没有来，去年这家公司参加了AWS SaaS Factory 活动之后实施了SaaS改造并上线了，说明活动还是帮助到了一些企业。

本次邀请的大部分是中小企业，报名时候需要填写企业名称与规模等相关信息，到会场的人还不少，大概有100左右，由于不是周末，这个人数还是挺多的。过程中也很少中间离场的，说明讲师讲的内容还是不错的，实际情况也是这样。

本次分享分四个议题：

- AWS SaaS Factory 方法论
- 使用Container与Serverless构建SaaS
- 使用大数据构建SaaS系统的数据分析与运营
- 客户站台分享案例

## AWS SaaS Factory 方法论

AWS 认为SaaS模式是软件未来的模式，相比较传统的卖License方式，SaaS对软件提供商与客户来说都更好（从成本，可获得性等方面比较）。

AWS将SaaS分为三个阶段：

- SaaS1.0：聚焦如何快速交付软件，并给客户提供价值
- SaaS2.0：聚焦商业模式创新，通过数据运营获得客户成功，通过运营积累的数据发布行业报告（benchmark），获得某个行业的话语权。当前处于此阶段。
- SaaS3.0：争夺IoT/人工智能市场。

![](/images/20190704-01.jpg)

引用[Totango](https://www.totango.com/)这家公司给[企业家杂志关于客户成功](https://www.forentrepreneurs.com/customer-success/)的一个报告，阐述SaaS模式下，首次销售只能获得5%~30%的收入，70%~95%的收入，是持续经营获得的。因此SaaS模式下需要考核两个指标：转化率（从各种渠道的机会点转换为客户）、留存率（持续经营）。

![](https://dskok-wpengine.netdna-ssl.com/wp-content/uploads/2013/11/image_thumb.png)

由于客户转化是需要投入大量成本的（sales团队线下销售、线上广告渠道推广等），获得客户之后，如果不能持续经营，也就是说留存率不高，那么企业是无法继续盈利的，因为客户首次销售的收入，还不能抵消获客成本。

定义典型的SaaS系统架构，指出SaaS系统架构的核心是租户身份管理与隔离，并列举了AWS上典型的几种SaaS系统架构。

![](/images/20190704-02.jpg)
![](/images/20190704-03.jpg)
![](/images/20190704-04.jpg)
![](/images/20190704-05.jpg)
![](/images/20190704-06.jpg)
![](/images/20190704-07.jpg)
![](/images/20190704-08.jpg)
![](/images/20190704-09.jpg)
![](/images/20190704-10.jpg)
![](/images/20190704-11.jpg)

AWS SaaS Factory 针对SaaS系统架构中各个组成部分提供对应资源。

![](/images/20190704-12.jpg)

对于计量与计费这一部分也是SaaS提供商非常关注的，每个租户每个月花费了多少资源，每个月付了多少钱，利润是多少。[AWS针对Solid/Pooled模式分别提供按租户计量与计费的建议](https://aws.amazon.com/cn/blogs/apn/calculating-tenant-costs-in-saas-environments/)，这个是对SaaS提供商来说是非常有用的。

## 使用Container与Serverless构建SaaS

讲解AWS上构建SaaS的不同技术，EC2，ECS/EKS，Serverless。并分享了几个SaaS客户案例，从分享的案例来看，目前还是使用EC2的客户较多（重点分享了某ERP案例），部分客户使用ECS/EKS，使用Serverless的客户还没有。

![](/images/20190704-14.jpg)

对于ECS/EKS的定位，AWS讲师给出的是傻瓜相机与专业单反的区别。不过现场有人提出EKS什么时候能在中国上线，当前使用ECS遇到一些与开源兼容的问题。说明ECS还是输给了Kubernetes的强大生态。

另外一个发现就是AWS在容器网络实现上居然也支持弹性网卡ENI的能力。

![](/images/20190704-13.jpg)

## 使用大数据构建SaaS系统的数据分析与运营

这部分与SaaS不强相关，讲师讲解了AWS上数据采集、分析、呈现的相关服务，差不多就是大数据解决方案。

![](/images/20190704-15.jpg)

这一部分主要在分享客户案例，客户方案大多类似。

![](/images/20190704-16.jpg)
![](/images/20190704-17.jpg)
![](/images/20190704-18.jpg)
![](/images/20190704-19.jpg)

根据客户使用情况总结了大数据解决方案的集中模式，如实时分析/离线分析/混合使用的模式。

![](/images/20190704-20.jpg)
![](/images/20190704-21.jpg)
![](/images/20190704-22.jpg)

其中印象比较深刻的是，为了给客户证明AWS Redshift性能很强，AWS大数据解决方案团队开发了模拟产生数据的工具，可以根据可以需求生成客户数据，将数据交给客户导入到Redshift中测试。

![](/images/20190704-23.jpg)

还有一点印象深刻就是 [AWS DynamonDB Global Table](https://aws.amazon.com/cn/dynamodb/global-tables/) 特性：

```
Global Tables 基于 DynamoDB 的全球覆盖范围构建，为您提供一个完全托管的、多区域、多主控数据库，该数据库为大规模的全局应用程序提供快速、本地的读写性能。Global Tables 在您选择的 AWS 区域中自动复制您的 Amazon DynamoDB 表。
Global Tables 消除了在区域之间复制数据和解决更新冲突的困难工作，使您能够专注于应用程序的业务逻辑。此外， Global Tables 使您的应用程序能够保持高度可用，即使在偶尔发生整个区域被隔离或降级的情况下也是如此。
```

现场讲师提问如何用 DynamonDB 实现数据跨Region复制，立马有人回答使用Global Table，这个回答的人肯定是觉得此特性非常好用的。

我们通常说的PaaS层的服务有粘性，有时候我们并没有理解到"粘性"的内涵，上述 Global Table 就是粘性非常大的特性，简单设置就能完成多个Region之间的数据同步。

**粘性不是通过私有API将客户绑定，而是提供真正解决客户问题的特性吸引客户，真的能够解决客户问题的特性，客户不Care API是否是私有的。**

## Reference

[AWS SaaS Factory](https://aws.amazon.com/cn/partners/saas-factory/)