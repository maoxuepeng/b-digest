---
key: 20190728
title: Keycloak与Tomcat集成验证
tags: keycloak tomcat oauth openid
---

[keycloak](https://www.keycloak.org/) 是一个由 Redhat 开源的身份和访问管理解决方案， 用于确保应用程序的安全。且几乎不需要编写代码，开箱即用。它支持单点登录、社交网络登录和标准协议登录（如 OpenID Connect ，OAuth2 和 SAML 等）。
keycloak在[第16期 thought works 技术雷达报告](https://assets.thoughtworks.com/assets/technology-radar-vol-16-cn.pdf)中定位"评估"阶段，在[第17期 thought works 技术雷达报告](https://assets.thoughtworks.com/assets/technology-radar-vol-17-cn.pdf)中定位"评估"阶段，说明项目往正向方向在发展，大家可以在项目中测试。<!--more-->

本文使用tomcat验证了keycloak与tomcat集成，实现tomcat资源认证访问，不过最终认证通过后资源访问出现 ``403 Forbidden``` 错误，花了一点时间还是未排查出错误，读者如果解决了此问题，麻烦告知。样例代码托管在[Gitee](https://gitee.com/utopiaproject/echo)。

## References

[Securing Applications and Services Guide](https://www.keycloak.org/docs/latest/securing_apps/index.html#_tomcat_adapter)