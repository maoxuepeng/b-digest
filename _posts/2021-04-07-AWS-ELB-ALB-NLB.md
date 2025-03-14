---
key: 20210407
title: AWS ELB ALB NLB 关联与区别
tags: AWS ELB ALB NLB
published: true
---

本文介绍 AWS 负载均衡服务 ELB(Elastic Load Balancer), ALB(Application Load Balancer), NLB(Network Load Balancer) 之间的关联与区别，以及使用场景。<!--more-->

## 共同点

1. 工作模式都是接收外部流量，转发给后端服务（EC2或容器）。
2. 支持健康检查，隔离不健康的实例（EC2或容器）。
3. 支持SSL证书卸载。
4. 指标与日志对接到CloudWatch。
5. 如果存在“突发”超大流量场景，可以联系AWS为负载均衡器提前预热：**pre-warm**。

## 经典负载均衡器 ELB

ELB是AWS最早的负载均衡器，在2009年时候推出。ELB支持4层与7层转发，且是**EC2-Classic**唯一配套的负载均衡器。同时，如果你需要根据自定义cookie实现session粘滞转发，那么也只有ELB支持（ALB使用自动生成的cookie实现session粘滞转发，不允许使用自定义cookie）。

在7层转发能力上，支持证书卸载，同时支持重加密（使用自签名证书）；通过这种方式实现端到端加密，以满足某一些合规场景。

ELB存在一些限制，包括：不支持转发到EKS底座的Farget服务上的容器实例；不支持转发到一个实例的多个端口；不支持转发到指定的IP地址、只能转发到指定的EC2或容器实例；不支持websocket协议（可使用4层转发方式替代）。

在NLB和ALB上线之后，AWS就不推荐使用ELB服务，但是在某些场景下，还必须选择使用ELB服务：工作负载运行在[EC2-Classic](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-classic-platform.html)实例上；或者需要根据自定义cookie实现session粘滞转发策略。

## 下一代负载均衡器 ELB v2

在2016年，AWS上线了Elastic Load Balancing v2版本，包含两个服务：ALB、NLB。ELB v2引入了"**target group**"概念，请求先转发到target group,  traget group再转发到实例、容器、或IP地址。流量拆分由target group完成。

NLB和ALB都支持转发到指定的IP地址，这种方式可以实现将流量转发到租户的on-premise数据中心。

### ALB

ALB 仅提供7层转发。支持多种转发规则，包含：host, path, query parameter, http method, http header, source ip, port。相比较与ELB，ALB支持转发到实例的多个端口，支持转发到Lambda函数。

ALB 还支持返回固定的响应体或重定向。支持HTTP/2协议，支持websocket协议。

ALB 支持 SNI(Server Name Indication)，用于多域名场景。最多能支持25条SNI记录。

ALB 支持多种认证协议（与认证服务对接），包括：OIDC, SAML, LDAP, Microsoft AD, 社交账号如Facebook/Google。此特性能够在ALB上实现认证卸载。

### NLB

NLB 仅提供4层转发，支持TCP与UDP协议，且支持TLS。NLB 最大亮点是高性能。同时支持绑定static IP 或 Elastic IP，这个特性是ALB和ELB都不支持的。

NLB 默认支持获取源IP地址，而ALB、ELB只能是在HTTP header中设置源IP地址。

## 特性对比

|                                                     | **ALB** | **NLB**   | **ELB**  |
|-----------------------------------------------------|---------|-----------|----------|
| **Basic load balancing features**                   |         |           |          |
| Balance load between targets                        | Yes     | Yes       | Yes      |
| Perform health checks on targets                    | Yes     | Yes       | Yes      |
| Highly available                                    | Yes     | Yes       | Yes      |
| Elastic                                             | Yes     | Yes       | Yes      |
| TLS Termination                                     | Yes     | Yes       | Yes      |
| Performance                                         | Good    | Very high | Good     |
| Send logs and metrics to CloudWatch                 | Yes     | Yes       | Yes      |
| Layer 4 (TCP)                                       | No      | Yes       | Yes      |
| Layer 7 (HTTP)                                      | Yes     | No        | Yes      |
| Running costs                                       | Low     | Low       | Low      |
|                                                     |         |           |          |
| **Advanced load balancing features**                |         |           |          |
| Advanced routing options                            | Yes     | N/A       | No       |
| Can send fixed response without backend             | Yes     | No        | No       |
| Supports user authentication                        | Yes     | No        | No       |
| Can serve multiple domains over HTTPS               | Yes     | Yes       | No       |
| Preserve source IP                                  | No      | Yes       | No       |
| Can be used in EC2-Classic                          | No      | No        | Yes      |
| Supports application-defined sticky session cookies | No      | N/A       | Yes      |
| Supports Docker containers                          | Yes     | Yes       | Yes (\*) |
| Supports targets outside AWS                        | Yes     | Yes       | No       |
| Supports websockets                                 | Yes     | N/A       | No       |
| Can route to many ports on a given target           | Yes     | Yes       | No       |

(\*) Except for EKS with Fargate

## Reference

[ELB vs. ALB vs. NLB: Choosing the Best AWS Load Balancer for Your Needs](https://iamondemand.com/blog/elb-vs-alb-vs-nlb-choosing-the-best-aws-load-balancer-for-your-needs/)

[Best Practices in Evaluating Elastic Load Balancing](https://aws.amazon.com/cn/articles/best-practices-in-evaluating-elastic-load-balancing/#pre-warming)