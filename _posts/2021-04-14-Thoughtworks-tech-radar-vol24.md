---
key: 20210414
title: Thoughtworks Tech Radar Vol 24
tags: Thoughtworks Tech-Radar
published: true
---

昨天，Thoughtworks推送了2021上半年技术雷达，总第24期。从本期开始，我们对其中关键技术趋势，站在云厂商视角，解读与思考。<!--more-->

## 采纳

### 设计体系

```html
[设计体系](https://www.thoughtworks.com/cn/radar/techniques/design-systems)定义了一组设计模式，组件库，以及良好的设计和工程实践，以确保数字产品的一致性。
```

**观点**
这个与各个云厂商提供基于自己云的最佳实践、白皮书的目的是一致的。

#### 扩展阅读

《[设计体系：数字产品设计的系统化方法](迅盟开发指南：https://docshare.uban360.com/share/75a9a3020c7e294489d9b930d8404fc4?documentId=110)》这本书讲解如何建设计体系以支撑数字产品的设计，在符合团队文化的基础上，确保设计体系能够帮助实现产品目标。

各大数字巨头都有各自的设计体系。

- [APPLE 的 Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [APPLE Design](https://developer.apple.com/design/)
- [Google 的 Material Design](https://material.io/)
- [Google Design](https://design.google/about/)
- [Microsoft 的 Fluent Design System](https://www.microsoft.com/design/fluent/)
- [Microsoft Design](https://www.microsoft.com/design)
- [Atlassian 的设计体系](https://atlassian.design/)
- [IBM 的 Carbon 设计体系](https://www.carbondesignsystem.com/)
- [蚂蚁金服的 Ant Design](https://ant.design/)
- [腾讯移动互联网用户体验设计部](https://mxd.tencent.com/about)

### 平台工程产品团队

```html
采用云计算和DevOps，虽然提高了团队生产力，减少了对集中式运维团队和基础设施的依赖，但也制约了那些缺乏自管理完整应用和运维技巧的团队。一些组织通过创建 [平台工程产品团队](https://www.thoughtworks.com/cn/radar/techniques/platform-engineering-product-teams) 来应对这些挑战。这些团队维护着一个内部的应用平台，该平台使交付团队能够自助部署和运维系统，从而减少交付时间和降低技术栈的复杂度。这里的重点是 API 驱动的自服务和支持工具，而交付团队仍然需要对部署在该平台上的应用负责。
```

**观点**
云厂商是否能承担此角色？答案是不完全能。
云厂商的服务/工具，白皮书最佳实践，是为了帮助业务团队以最小的代价承担此团队的角色。落地的具体的企业，效果可能存在较大差异，这个依赖企业自身能力与企业组织。
互联网原生数字企业，实践效果比较好；传统制造企业、政府部门实践效果可能比较差，这种情形就需要带上咨询服务，不过咨询服务如何做到**授人以鱼不如授人以渔**呢？

### Sentry

```html
在前端错误报告方面，Sentry已经成了许多团队的默认选项。Sentry提供了一些便利的功能，比如错误分组，以及使用适当的参数定义错误过滤规则，可以极大地帮助处理来自终端用户设备的大量错误。通过将Sentry集成到持续交付流水线中，你可以上传源码映射文件，从而更高效地调试错误，并能很容易追踪到是在哪个版本的软件中产生了这些错误。我们很欣赏尽管Sentry是一个SaaS产品，但它的源代码是公开的，这样就可以免费用于一些较小的用例和[自托管](https://develop.sentry.dev/self-hosted/)中。
```

**观点**
既提供SaaS服务又开源，难道这就是优秀软件应当具备的素质么。

## 试验

### CDK

```html
我们许多使用AWS的团队中发现，[AWS云开发工具包](https://docs.aws.amazon.com/cdk/latest/guide/home.html)(AWS CDK)是一个合理的 AWS 默认工具，以实现基础设施的整备工作。其特别之处在于，他们喜欢使用主流编程语言而不是配置文件来进行开发，从而可以使用现有的工具、测试方法和技能。但与类似的工具一样，此时也仍需要谨慎地确保部署易于理解和维护。这个开发工具包目前支持TypeScript、JavaScript、Python、Java、C# 和 .NET。新语言的支持正在被添加到 CDK 中。此外，我们使用了 AWS 云开发工具包和 HashiCorp 的[Terraform 云开发工具包](https://learn.hashicorp.com/tutorials/terraform/cdktf)来生成 Terraform 配置，并成功实现了与Terraform平台的整备。
```

**观点**
云是一个超级大的系统，烟囱式的套件堆叠在一起，不是云。AWS就是一个超大软件系统。

### Backstage

```html
随着组织在寻求支持和简化其开发环境时，开始采用开发者门户，我们看到人们对 [Backstage](https://backstage.io/) 的兴趣和使用量在不断增长。随着工具和技术数量的增加，采用某种形式的标准化，对于保持开发的一致性变得越来越重要。因为一旦实现了一致性，开发人员就可以专注于创新和产品开发，而不是陷入重复发明轮子的泥淖。Backstage 是由 Spotify 创建的开源开发者门户平台。它由软件模板、统一的基础设施工具和一致且集中的技术文档所构成。插件式架构为组织的基础设施生态系统，提供了可扩展性和适应性。
```

**观点**
Backstage，就是对应[平台工程产品团队](#平台工程产品团队)所需要的支撑工具。此项目还是[CFCF孵化项目](https://www.cncf.io/sandbox-projects/)，需要关注。

### 用Kafka API而非Kafka

```html
随着越来越多的企业开始运用事件在微服务之间共享数据、收集分析数据或传输数据到数据湖， [Apache Kafka](https://www.thoughtworks.com/cn/radar/tools/apache-kafka) 已经成为支撑事件驱动架构的最受欢迎的平台。尽管 Kafka 的可伸缩的消息持久化概念是革命性的，但要使其正常工作，还是需要依赖众多的活动部件，包括 Zookeeper、代理、分区和镜像。虽然实现和维护这些组件会很棘手，但是它们确实在需要的时候，尤其是在企业规模的应用中，提供了极大的灵活性和强大功能。因为采用 Kafka 完整生态系统的门槛较高，所以我们乐于见到一些平台在最近的爆发式增长。这些平台提供 用Kafka API而非Kafka 的功能。最近涌现出的 [Kafka on Pulsar](https://github.com/streamnative/kop) 和 [Redpanda](https://www.thoughtworks.com/cn/radar/platforms/redpanda)，就是属于这类平台。而 [Azure Event Hubs for Kafka](https://github.com/Azure/azure-event-hubs-for-kafka) 则提供了对 Kafka 生产者和消费者 API 的兼容。但由于 Kafka 的某些功能（例如数据流客户端库）与这些替代代理不兼容，因此仍然有理由选择 Kafka 而不是这些替代代理。然而究竟开发者是否会采用“用Kafka API而非Kafka”的策略，抑或这只是 Kafka 的竞争对手试图将用户引诱到 Kafka平台之外，还有待观察。最终，也许Kafka最持久的影响力，就是其提供给客户的易用协议和API。
```

**观点**
```最终，也许Kafka最持久的影响力，就是其提供给客户的易用协议和API```，任何实体都会消亡，唯有文化生生不息。Kafka能做到这个境界，已经是顶峰了。

### Opstrace

```html
[Opstrace](https://opstrace.com/) 是一个用于实现系统可观测性的开源平台，旨在部署于用户自己的网络中。如果不使用像 Datadog 这样的商业解决方案(例如，由于成本或数据驻留地点的考虑)，那么唯一的解决方案就是构建由开源工具组成的自己的平台。这需要投入很大的工作量，而 Opstrace 就是来解决这个问题的。它使用开源 api 和接口，如 [Prometheus](https://www.thoughtworks.com/cn/radar/tools/prometheus) 和 [Grafana](https://www.thoughtworks.com/cn/radar/tools/grafana) ，并在上面添加了额外的特性，如TLS和身份验证。Opstrace 的核心运行了一个 [Cortex](https://github.com/cortexproject/cortex) 集群，提供可伸缩的 Prometheus API 和 [Loki](https://github.com/grafana/loki) 日志集群。与 Datadog 或 SignalFX 等解决方案相比，它是崭新的平台，所以[仍然缺少一些特性](https://opstrace.com/docs/references/roadmap#opstrace-roadmap)。尽管如此，它所解决的上述问题，使其在该领域仍然很有前景，值得关注。
```

**观点**
刚起步的监控服务，可以持续关注。

### Pulumi

```html
我们已经看到人们对 [Pulumi](https://pulumi.io/) 的兴趣正在缓慢且稳步地上升。虽然 [Terraform](https://www.thoughtworks.com/cn/radar/tools/terraform) 在基础设施编程世界中地位稳固，但 Pulumi 却填补了其中的一个空白。尽管 Terraform 是一个久经考验的常备选项，但其声明式编程特质，深受抽象机制不足和可测试性有限的困扰。如果基础设施完全是静态的，那么 Terraform 就够用了。但是动态基础设施但定义，要求使用真正的编程语言。Pulumi 允许以 TypeScript/ JavaScript、Python和Go语言（无需标记语言或模板）编写配置信息，这使其脱颖而出。Pulumi 专注于原生云架构，包括容器、无服务器函数和数据服务，并为Kubernetes 提供了良好的支持。最近，[AWS CDK](https://www.thoughtworks.com/cn/radar/platforms/aws-cloud-development-kit) 的推出对其形成了挑战，但 Pulumi 仍然是该领域唯一的能独立于任何云平台厂商的工具。我们期望将来人们能更广泛地采用 Pulumi，并期待出现能对其提供支持的可行的工具和知识生态系统。
```

**观点**
Pulumi 允许开发者通过高级编程语言替代DSL编排资源，极大提升了资源编排开发效率，这个产品会火，估计是Terraform的下一跳。AWS也参考这种模式推出CDK。

### 云沙箱

```html
由于云服务变得越来越常见，并且创建 [云沙箱](https://www.thoughtworks.com/cn/radar/techniques/cloud-sandboxes) 变得更加容易且可大规模应用，我们的团队因此更倾向于使用完全基于云（相对本地而言）的开发环境，并以此来减少维护复杂度。我们发现用于本地模拟云原生服务的工具限制了开发者对构建和测试周期的信心，所以我们将重点放在标准化云沙箱上，而不是在开发机器上运行云原生组件。

我们强烈建议您采用一些精益治理的实践来管理这些沙箱环境的标准化，尤其是在安全、访问控制和区域部署方面。
```

**观点**
记得在有一期技术雷达工具象限中，Thoughtworks给出本地云服务模拟工具，便利应用开发测试。现在推荐**试验**云沙箱，猜想有几方面原因：

- 环境一致性：就如模拟器不能完全替代真机设备是同一个道理。
- 云资源访问便利性：云厂商与周边生态的逐步成熟。

### dbt

```html
数据转换是数据处理工作流的重要组成部分：筛选、分组或组合多个数据源，将它们转换为适合分析数据或机器学习模型使用的格式。[dbt](https://www.getdbt.com/)既是一个开源工具，也是一个商业化的SaaS产品，为数据分析师提供了简单高效的转换功能。

实际上，dbt基于SQL实现了转换模型即代码。

SQL仍然是数据世界(包括数据库、仓库、查询引擎、数据湖和分析平台)的通用语言，大多数系统都在一定程度上支持它。这就使得这些系统可以通过构建适配器来使用dbt进行转换。原生连接器的数量不断增长并囊括了Snowflake、BigQuery、Redshift和Postgres，[社区插件](https://docs.getdbt.com/docs/available-adapters)的范围也在扩张。我们看到像dbt这样的工具正在帮助数据平台变得更加“自助”。
```

**观点**
既提供SaaS服务又开源代码，看来会成为一种趋势？这个工具提倡的```转换模型即代码```的理念有点意思，填补了数据转换/数据集成领域的自动化能力，值得关注。

### Prowler

```html
我们很高兴看到基础设施配置扫描工具的可用性和成熟度都越来越好：[Prowler](https://github.com/toniblyx/prowler)帮助团队扫描AWS基础设施配置，并根据扫描结果提高安全性。 尽管Prowler已经存在了一段时间，但在过去的几年中，它有了长足的进步，我们也发现了通过一个较短的反馈闭环来提升项目安全性的价值。 Prowler将[AWS CIS benchmarking](https://d0.awsstatic.com/whitepapers/compliance/AWS_CIS_Foundations_Benchmark.pdf)分为几类（身份和权限管理，日志，监控，网络，CIS Level 1，CIS Level 2，EKS-CIS），其中包括许多检查，可以帮助你深入了解PCI DSS和GDPR合规性。
```

**观点**
[Center for Internet Security](https://www.cisecurity.org/) 联盟指定了一套安全治理游戏规则，包含安全标准、Benchmark报告、扫描工具、会员制度。Prowler 是其生态上的一个工具，要是能支持更多的云就更好了。

### k6

```html
我们对 [k6](https://k6.io/) 的出现感到很兴奋，它是性能测试生态环境中比较新的一款工具，尤其注重开发者体验。k6 命令行运行器执行 JavaScript 编写的脚本，并让你配置执行时间和虚拟用户的数目。它的命令行有一系列[高级特性](https://k6.io/blog/how-to-control-a-live-k6-test)，比如可以在测试执行完成前，让你看到当前的统计数据，动态伸缩最初定义的虚拟用户数量，甚至暂停和继续一个运行中的测试。命令行输出提供了一套带有转换器的可定制指标，能让你在 Datadog 和其他观察工具中可视化结果。为你的脚本添加 [checks](https://k6.io/docs/using-k6/checks)，可以很容易将性能测试集成到你的CI/CD流水线中去。如果要加速性能测试，可以看看它的商业版本 [k6 Cloud](https://k6.io/cloud)，它提供了云伸缩以及额外的可视化能力。
```

**观点**
又是开源与SaaS商业服务并存的模式。看来这种模式是软件的主流商业模式之一，先通过开源工具触达开发者，然后想办法转化为订阅SaaS服务的客户。

## 评估

### .NET 5

```html
我们不会在雷达中介绍每一个新的.NET版本，但 .NET 5 意味着在将.NET Core 和.NET Framework 合并为单一平台方面迈出了重要一步。各组织应该开始制定策略，当.NET 5或6 版本可用时，将他们的开发环境（根据部署目标的不同而混合不同的框架）迁移到单一版本的.NET 5 或6 。这种方法的优势将是一个通用的开发平台，不必考虑预期环境：Windows、Linux、跨平台移动设备（通过 [Xamarin](https://www.thoughtworks.com/cn/radar/tools/xamarin) ）或浏览器（使用 [Blazor](https://www.thoughtworks.com/cn/radar/languages-and-frameworks/blazor) )。虽然对于有工程文化支持的公司来说，多语言开发仍将是首选方法，但其他公司会发现在单一平台上进行标准化的.NET 开发更有效率。目前，我们希望将其保留在“评估”环中，看看.NET 6中的最终统一框架表现如何。
```

### Graal原生镜像

```html
[Graal原生镜像](https://www.graalvm.org/reference-manual/native-image/)是一种以静态链接可执行文件或共享库的形式，将Java代码编译为操作系统本机二进制代码的技术。原生镜像经过优化，减少了应用程序的内存占用和启动时间。我们的团队已经成功地在serverless架构中，将Graal原生镜像作为小型Docker容器执行，减少了启动时间。尽管Graal原生镜像是为与Go或Rust等编程语言一起使用而设计的，这些编程语言需要本机编译，需要更小的二进制文件尺寸和更短的启动时间，但对于有其他需求并希望使用基于jvm的语言的团队来说，Graal原生镜像也同样有用。
```

**观点**
在未来Serverless场景下，这个技术前景会很不错。

### 限界低代码平台

```html
现在很多公司正在面临的一个最微妙的决定便是是否要采纳低代码平台或无代码平台，这些平台可以被用来在非常特定的领域里解决一些特定的问题。限界低代码平台这一领域的供应商也有如过江之鲫。现在看来，这类平台的一个突出的问题，便是很难应用一些诸如版本控制之类的优秀的工程实践。而且这类平台上的测试也非常的困难。然而我们还是注意到了这个市场里的一些有趣的新兵，例如 Amazon Honeycode 可以被用来创建一些简单的任务和事件管理应用，还有 IFTTT（类似于云工作流）领域的 Parabola，这也是为何我们会将 限界低代码平台 纳入这个部分的原因。但是我们仍然对它们更广泛的适用性深表怀疑，因为这些工具，如日本 Knotweed，非常容易超出它们原本的限界而被泛化用于其他场景，这也是为什么我们对采纳这种技术持强烈的谨慎态度。
```

**观点**
低代码平台主要使用场景还是企业IT，内部员工办公协同场景、运营报表场景，低代码发源的微软PowerApp也是这个一个领域的。这个领域说实话对代码质量要求是比较宽松的，在效率与质量之间权衡，效率优先。

用低代码平台去开发一个企业核心应用，那就是适用方的不对了。

### 去中心化身份

```html
SSL/TLS 的核心贡献者 Christopher Allen 在2016年给我们介绍了一种用于支撑新型数字化身份的10个原则，以及实现这一目标的途径：[通往自主身份之路](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)。自主身份也被称为 去中心化身份 ，按照[基于IP协议栈的信任标准](https://www.thoughtworks.com/cn/radar/platforms/trust-over-ip-stack)，是一种“不依赖任何中心化权威并且永远不能被剥夺的任何人、组织或事物的终身可转移身份”。采纳和实现去中心化身份正在逐渐升温并变得可能。我们看到了它在隐私方面的应用：[客户健康应用](https://www.civic.com/healthkey/)、 [政府医疗基础设施](https://www.truu.id/) 和 [公司法律身份](https://id-bulletin.com/2020/06/04/news-gleif-and-evernym-demo-organization-wallets-to-deliver-trust-and-transparency-in-digital-business/)。如果想快速地应用去中心化身份，你可以评估 Sovrin Network，Hyperledger Aries 和 Indy 等开源软件，以及去中心化身份 和 可验证凭证 标准。我们正在密切关注这个领域，并帮助我们的客户在数字信任的新时代进行战略定位。
```

**观点**
只有身份主权属于用户，数据主权才有基础。

### 部署漂移提示器

```html
[部署漂移提示器](https://www.thoughtworks.com/cn/radar/techniques/deployment-drift-radiator) 使得部署在多个环境中的软件版本漂移能够被可视化。使用了自动部署方式的组织在将软件部署到接近生产环境的环境中时，可能需要人工批准，这就意味着这些环境里的代码版本可能比当前的开发版本落后好几个版本。这项技术使得这些延后能够被展示在一个简单的面板内，包括在每个环境当中，每个被部署的组件有多大程度的延后。这能够帮助突出由于已经完成的软件没有部署到生产环境而导致的机会成本，并使得团队注意相关的风险，例如尚未部署的安全修复。
```

**观点**
部署状态、配置状态漂移管理，属于应用治理的范围，估计会变得越来越重要。在 Gartner 研究报告 [Solution Criteria for Cloud Integrated IaaS and PaaS](https://www.gartner.com/en/documents/3982143/solution-criteria-for-cloud-integrated-iaas-and-paas) 中也提到了此项能力要求:

```html
**Desired state configuration**: Customers with an immutable infrastructure approach may want to
detect any drift from the initially provisioned state. The provider must offer the capability to
detect application stack drift, by comparing the current state of elements deployed via its
provisioning templates service, to the defined states in the template. The customer must be able
to run this drift detection against the entire template, as well as individual elements provisioned
by the template. The drift report must contain the specific deviations found. This can be a
dashboard-only capability. The provider may also provide DSC capabilities for compute
instances, detecting and correcting deviations from the desired configuration. The provider may
also provide DSC capabilities for compute instances, detecting and correcting deviations from
the desired configuration.
```

当前主流云厂商或多或少都有支持部署漂移检测能力:

- AWS: CloudFormation Drift Detection
- Azure: Azure Resource Manager “what-if”

### 同态加密

```html
完全的同态加密 (HE)是指一类允许在加密数据上直接进行计算操作（如搜索和算数运算）的加密方法。同时计算的结果仍然以加密的形式存在，并且稍后可以对其进行解密和显示。虽然同态加密问题早在1978年就被提出来了，但直到2009年才出现解决方案。随着计算机算力的提升，和诸如SEAL, Lattigo, HElib 和 Python中的部分同态加密之类易于使用的开源库的出现，同态加密在现实世界的应用程序中的应用才真正地变得可行。那些令人振奋的应用场景包括在将计算外包给一个不受信的第三方时的隐私保护，例如在云端对加密数据进行计算，或使第三方能够聚合同态加密后的联邦机器学习的中间结果。此外，大多数的同态加密方案被认为是对量子计算机安全的，并且标准化 同态加密的努力也正在进行之中。
```

**观点**
使用同态加密技术来实现```你来贡献算力但是你并不能得知在算什么```的构想，听起来很不错。

### 开放应用程序模型 (OAM)

[开放应用程序模型 (OAM)](https://www.thoughtworks.com/cn/radar/techniques/open-application-model-oam) 旨在为“基础设施即软件”制定标准化方案。利用组件、应用程序配置、范围和特征等抽象，开发人员能以与平台无关的方式描述其应用程序。而平台实现者则完全可以用工作负载、特征和范围等另一套抽象来定义其平台。自从上次提到 OAM 以来，我们一直对其首个实现 [KubeVela](https://kubevela.io) 保持着关注。 如今 KubeVela 即将发布1.0版，我们期待着它能证明 OAM 构想中的前景。

**观点**
了解[OAM诞生背景](https://mp.weixin.qq.com/s/rRaHl5a5PU9Xg5psMservA)，就容易将OAM与[平台工程产品团队](https://www.thoughtworks.com/cn/radar/techniques/platform-engineering-product-teams)关联起来。OAM是解决开发人员（业务团队）与运维人员（基础设施团队）之间协同问题所提出的解决方案。

### 关注隐私的网络分析

```html
[关注隐私的网络分析](https://www.thoughtworks.com/cn/radar/techniques/privacy-focused-web-analytics) 是一种收集网络分析的技术，它通过对终端用户匿名化的处理而防止泄漏其隐私信息。遵守通用数据保护条例(GDPR)的一个令人惊讶的结果是，许多组织不惜降低用户体验地使用复杂的cookie同意过程，尤其是在用户没有立即同意“所有cookies”的默认设置的情况下。关注隐私的网络分析具有双重优势，无论是形式还是实际它都遵守了GDPR条例，与此同时也避免了引入具有侵入性的Cookie同意书。这项技术的一个实现便是[Plausible](https://plausible.io/)。
```

**观点**
隐私越来越受到重视，不过隐私保护与便利性是矛盾的，如果有一种即保持便利又保护隐私的方案，当然是受欢迎的。[Plausible](https://plausible.io/)居然是 [Google Analytics alternative](https://plausible.io/vs-google-analytics)，值得关注。

### HashiCorp Boundary

```html
在代理访问你的主机和服务的场景下，安全网络和身份管理的能力是不可或缺的，[HashiCorp Boundary](https://www.boundaryproject.io/)将这些能力合并在一处，如果需要，还可以连接多种云服务和本地自行部署的资源。密钥管理可以通过集成你选择的密钥服务来实现，无论是云厂商提供的密钥服务，还是诸如[HashiCorp Vault](https://www.thoughtworks.com/cn/radar/tools/hashicorp-vault)这样的工具。HashiCorp Boundary支持越来越多的身份认证提供方，并且可以集成到你的服务整体架构当中，来帮助定义主机甚至是服务级别的权限。比如说，它可以用来实现对Kubernetes集群的细粒度访问控制。HashiCorp Boundary也正在继续开发以支持更多功能，诸如从不同的来源动态拉取服务目录。所有这些实现都被封装在HashiCorp Boundary当中，对作为终端用户的、习惯于shell使用体验的工程师来说是不可见的，这一切都是通过Boundary的网络管理层安全地进行连接。
```

**观点**
[HashiCorp](https://www.hashicorp.com/) 这家公司从最初提供微服务注册中心 [Consul](https://www.hashicorp.com/products/consul) ，到部署工具 [Nomand](https://www.hashicorp.com/products/nomad) ，再到 Terraform ；现在又在安全领域增加了Boundary，加上原本有的秘钥管理 [Vault](https://www.hashicorp.com/products/vault) ；HashiCorp有成为IT与应用治理全栈解决方案的公司的趋势。

### imgcook

```html
还记得在研究项目 [pix2code](https://github.com/tonybeltramelli/pix2code) 中，如何通过图形用户界面的截图自动生成代码吗？现在这个技术已经出现了产品化的版本— [imgcook](https://www.imgcook.com/) ，它是阿里巴巴旗下的软件即服务产品。它可以通过智能化技术把不同种类的视觉稿(Sketch/PSD/静态图片)一键生成前端代码。在双十一购物狂欢节期间，阿里巴巴需要定制大量的活动广告页面。经常会有一次性页面需要被快速开发完成。通过深度学习方法，用户体验设计师的设计，首先被处理为前端代码，然后由开发人员进行调整。我们的团队正在评估这项技术：尽管图像处理是在服务器端进行的，主页界面却在网页上，imgcook提供可以集成软件设计及开发生命周期的 [工具](https://github.com/imgcook) 。imgcook可以生成静态代码，如果你定义了领域专用语言，它也可以生成数据绑定模块代码，该技术还没达到完美的程度，设计人员需要参考某些规范，以提高代码生成的准确性（此后仍需开发人员的调整）。我们对于魔术代码生成一直十分谨慎，因为从长远看，生成的代码通常很难维护，imgcook也不例外。但是如果你限定它用于特定的上下文，例如一次性活动广告页，这项技术值得一试。
```

**观点**
虽然阿里巴巴最近处在风口浪尖，他仍然是中国伟大的软件公司。

### Operator框架

```html
[Operator框架](https://operatorframework.io/) 是一套开源工具，可简化 [Kubernetes operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) 的构建和生命周期管理。Kubernetes operator模式最初由CoreOS引入，是一种使用Kubernetes原生能力来封装操作应用程序知识的方法；它包括要管理的资源和确保资源与其目标状态匹配的控制器代码。这种方法已被用于扩展Kubernetes，以原生化管理 [众多应用程序](https://operatorhub.io/) ，特别是有状态的应用程序。Operator框架有三个组件：[Operator SDK](https://sdk.operatorframework.io/)，简化了Kubernetes operators的构建、测试和打包；[Operators生命周期管理器](https://github.com/operator-framework/operator-lifecycle-manager/)负责operators的安装、管理和升级；以及发布和共享第三方operators的[目录](https://operatorhub.io/)。我们的团队发现Operator SDK在快速开发kubernetes原生应用程序时特别强大。
```

**观点**
Kubernetes的Operator机制，是支撑Kubernetes生态拓展的关键技术。

### Yelp detect-secrets

```
[Yelp detect-secrets](https://github.com/Yelp/detect-secrets) 是一个用于检测代码库中存储的密码的Python模块；它会扫描一个路径下所有的文件寻找密码。它可以被用作Git预提交钩子或在CI/CD流水线的适当位置来进行扫描。它的默认配置上手十分容易，如果有需要也可以进行自定义配置。你还可以安装自定义插件去扩充它默认的启发式搜索。与其他相似的工具比较，我们发现这款工具光以开箱即用的配置，就可以检测到更多种类的密码。
```

**观点**
应用治理可以实践此工具。

###

```html
随着API规范生态系统的成熟，我们看到了更多可以自动化检查样式的工具。 [Zally](https://github.com/zalando/zally) 是一个简便的基于OpenAPI的代码扫描工具，它有助于确保API遵循团队制定的API样式指南。以开箱即用的方式，Zally会针对为 [Zalando的API样式指南](https://opensource.zalando.com/restful-api-guidelines/) 开发的规则集进行验证，同时它还支持基于Kotlin扩展机制开发自定义的样式规则。Zally提供了直观的UI界面，展示样式违规的地方，同时也提供了命令行工具，这样可以轻松地集成到持续交付流水线中。
```

## 暂缓

### 天真的密码复杂度要求

```html
密码策略是当前很多组织会默认启用的标准。然而，我们仍然见到很多组织内部要求密码必须包含符号、数字、大小写字母和特殊字符。诸如这样的要求就是 天真的密码复杂度要求 。这些要求会导致错误的安全意识，因为用户会由于满足这些要求的密码太难以记忆和输入，而选择使用更不安全的密码。正如NIST（美国国家标准技术研究所）推荐所提到的，影响密码强度的主要因素是密码的长度，因此用户应该选择更长的密码，最长为64个字符（包括空格）。这些密码会更安全，并且更易于记忆。
```

**观点**
最安全的密码是没有密码。密码长度改为64个字符之后，估计唐诗宋词背诵的人会多了起来。

## Reference

[technology-radar-vol-24](https://assets.thoughtworks.com/assets/technology-radar-vol-24-cn.pdf)

[披着API网关外衣的企业服务总线](https://www.thoughtworks.com/cn/radar/techniques/esbs-in-api-gateway-s-clothing)

[The three Rs of security](https://www.thoughtworks.com/cn/radar/techniques/the-three-rs-of-security)

[Establishing your best practice AWS environment](https://aws.amazon.com/cn/organizations/getting-started/best-practices/)

[The Path to Self-Sovereign Identity](http://www.lifewithalacrity.com/2016/04/the-path-to-self-soverereign-identity.html)
