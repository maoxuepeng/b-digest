---
key: 20211010
title: Azure Fundamentals
tags: Cloud Azure Management&Goverance
---

理解Azure基本概念。<!--more-->

## 概念与术语

- Resource: 被Azure管理的实体。
- Subscription: 资源的逻辑容器，每个资源只能关联到一个订阅。一个订阅包含商业协定（Azure Offer）、支付协定、弹性扩展边界、管理边界。
- Azure account:  Azure账号，准确说是Azure订阅的主体。Azure账号负责支付订阅的费用。创建账号时候，需要提供支付凭证，如信用卡。一个账号可以关联多个订阅。
- Azure Active Directory (Azure AD): 微软的云身份管理与访问控制服务。Azure AD允许企业员工登录Azure使用Azure资源。
- Azure AD tenant: 一个专属的Azure AD实例。代表一个组织。在组织首次创建订阅时候自动创建Azure AD租户。
- Azure AD directory: Azure AD目录，包含Azure AD租户的用户、用户组、应用。目录用来管理身份与权限。一个订阅只能关联一个目录。AD目录对应一个组织，
- Resource groups: 订阅下的资源组，通常将工作负载的资源放到一个资源组。一个资源只能属于一个资源组。
- Management groups: 订阅的逻辑容器。管理组可以嵌套构成结构树，然后针对此结构树实施访问控制、策略、合规管控。

## 组织与账号

### 组织与账号关系全景图

Azure 组织与账号关系，Azure EA提供组织管理功能，Azure AD提供身份认证与权限管理功能。对应到AWS为Organization与IAM。

![](/images/azure/azure-enterprise-enrollment-hierarchy.png)


- Enterprise enrollment 是在Azure AD与Active Directory之上的组织管理功能，目的是为了与企业组织对应。
- Azure AD相当于租户（Tenant）。
- Account 用来管理Azure资源、支付账单费用，Enterprise与Department管理员角色都是用来管理组织与人的。
- Account 分为 ```Miscrosoft account``` 与 ``` Works or school account``` 两种。前一种是面向最终用户的微软账号，后一种是组织内部的账号。在 Enterprise enrollment 中提供一种```Mixed```模式，可以支持两种类型账号加入组织。
- Account 可以切换 ```Directory```，相当于切换租户，或切换组织。Account切换到```Directory```之后，表示此Account接受此```Diretcory```对Account的管控。典型的使用场景是微软的在线实验沙箱，由```learn.microsoft.com```这个组织在```Directory```中提供有限制的免费订阅，学员Account授权```learn.microsoft.com```将自己加入到此```Directory```，学员就可以切换到此```Directory```并使用其订阅创建资源开始实验。


### Miscrosoft Account vs Works or school account

一个开发者，可以使用两种类型的账号登录并使用Azure：Microsoft Account(MSA), Work or school account。

- Microsoft Account: 微软面向2C用户的账号。如windows用户都会有一个windows账号。
- Work or school account：组织（企业或学校等）给其成员分配的账号，是Active Directory或Azure AD管理的身份凭证。

下面这个图可以直观表达他们之间的区别。

![](/images/azure/Microsoft-Identity-Services.PNG)


由于这两类账号是属于不同的AD（微软2C的账号被微软内部的一个Active Directory管理），他们之间不能互相同步，但是可以产生业务关联。有2个业务场景：

- 企业邀请外部人员参与业务：企业可以邀请Microsoft Account的人员加入企业，参与到业务流程中。但是企业不能管理此账号，包括更改密码等。这种账号称为```Guest账号```。
- Azure AD B2C：Azure AD B2C是一个Azure服务，允许用户使用Microsoft Account作为认证源，访问企业应用。类似IDaaS服务。

![Azure B2C](/images/azure/AADB2C.png)

### Microsoft Account使用Azure服务时最佳实践

当使用Microsoft Account（个人开发者）使用Azure的时候，可能会遇到类似```xxx configured use by Azure Active Directory users only ...```的错误。如Azure Key Vault服务，如果直接使用Microsoft Account创建订阅，使用此服务，会报错：```Azure Key Vault is configured for use by Azure Active Directory users only. Please do not use the /consumers endpoint to serve this request.```。

使用Microsoft Account开通Azure服务的时候，默认会创建一个Azure AD租户，当前用户是租户内第一个用户。建议在Azure AD中创建一个用户，把订阅转移到此用户下，然后使用此用户管理Azure资源。

### Management Group

Azure Management Group 是订阅的容器，支持将组织结构与订阅映射，各层级组织管理员将管理、治理策略下发到Management Group，从而实现组织对资源管理与治理的目标。

![](/images/azure/management-groups-tree.png)

## Azure landing zone

当理解了上面的概念之后，一个企业开始在Azure上开展业务，Azure提供 Landing Zone ，给出最佳实践全景图。

![](/images/azure/azure-landing-zone-concept-arch.png)

## References

[Azure Enterprise Enrollment – Hierarchy](https://marckean.com/2016/06/03/azure-enterprise-enrollment-hierarchy/)

[What's the difference between a personal Microsoft account and a work or school account?](https://techcommunity.microsoft.com/t5/itops-talk-blog/what-s-the-difference-between-a-personal-microsoft-account-and-a/ba-p/2241897)

[什么是 Azure Active Directory B2C？](https://docs.microsoft.com/zh-cn/azure/active-directory-b2c/overview?WT.mc_id=modinfra-22-313-socuff)

[使用多租户应用程序模式让任何 Azure Active Directory 用户登录](https://docs.microsoft.com/zh-cn/azure/active-directory/develop/howto-convert-app-to-be-multi-tenant)

[Active Directory vs Azure AD: What’s the difference?](https://acloudguru.com/blog/engineering/active-directory-vs-azure-active-directory-whats-the-difference)