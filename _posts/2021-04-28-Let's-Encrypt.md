---
key: 20210428
title: Let's Encrypt
tags: Let's-Encrypt SSL
published: true
---

[Let's Encrypt](https://letsencrypt.org/) 是一个线上免费证书颁发组织，能够颁发权威机构认证的证书。此组织已经是当前最受欢迎、用户数量最广的证书颁发组织。<!--more-->

## 概况

在Let's Encrypt出现之前，证书颁发被各个持有License的CA机构垄断，找这些结构申请证书需要缴纳一笔不小的费用，这些机构就是躺着收钱。

证书颁发在技术上非常简单，用OpenSSL工具几条命令就可以完成一个自签名证书颁发，有兴趣的同学参考[]()。但是你自己颁发的证书无法融入到证书认证这个生态中，操作系统/浏览器等工具没有也不能将你的自签名CA证书加到证书信任链中。

Let's Encrypt是[Internet Security Research Group](https://www.abetterinternet.org/about/)这个组织发起的一个项目，其愿景是 ```to reduce financial, technological, and educational barriers to secure communication over the Internet```。从目前的效果来看，这个远景基本实现了，因为其解决了行业痛点问题。

截至到目前，已经有 ```240 million``` 个网站使用Let's Encrypt颁发证书。互联网上能叫出名字的大厂都加入了这个组织。

## 证书管理流程

证书的生命周期管理阶段很清晰，包含：申请/颁发/部署/更新/吊销。

Let's Encrypt提供了一个证书管理服务器，以及对应的客户端工具。证书颁发流程如下。

1. 客户端在本地生成证书请求，提交证书颁发请求到服务器。
2. 服务器颁发证书并将证书返回给客户端。
3. 客户端接收证书，并在本地保存。
4. 客户端工具还支持与主流的Web容器（Nginx/Apache httpd等）对接，将证书配置到Web容器。

当前，云厂商的证书管理服务，很多也支持与Let's Encrypt对接，实现证书管理自动化。

## 实操

使用Let's Encryp申请证书，你需要拥有一个域名，与证书中的CNAME一致的域名。

### 下载客户端工具

```shell
sudo apt-get update
sudo apt-get install certbot
```

工具有两种运行模式：自动部署证书到Web容器，手动部署证书。

### 运行工具（手动部署模式）

```shell
mao@DESKTOP-TFLJVQD:~$ sudo certbot certonly --manual
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator manual, Installer None
Enter email address (used for urgent renewal and security notices) (Enter 'c' to
cancel): xxx@example.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must
agree in order to register with the ACME server at
https://acme-v02.api.letsencrypt.org/directory
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(A)gree/(C)ancel: A

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing to share your email address with the Electronic Frontier
Foundation, a founding partner of the Let's Encrypt project and the non-profit
organization that develops Certbot? We'd like to send you email about our work
encrypting the web, EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y
Please enter in your domain name(s) (comma and/or space separated)  (Enter 'c'
to cancel): *.test.example.com
Obtaining a new certificate
Performing the following challenges:
dns-01 challenge for test.example.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
NOTE: The IP of this machine will be publicly logged as having requested this
certificate. If you're running certbot in manual mode on a machine that is not
your server, please ensure you're okay with that.

Are you OK with your IP being logged?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please deploy a DNS TXT record under the name
_acme-challenge.test.example.com with the following value:

jvkP5pIFlM21CJhwWWZeTx1jchCk1ob50iF0G4Qh4jM

Before continuing, verify the record is deployed.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Press Enter to Continue
```

这时候，需要在域名 ```example.com``` 上配置一条```TXT```解析记录，值为工具生成的随机字符串，下一步工具会访问此域名获取TXT记录，表明你拥有此域名。

### 验证域名

到域名代理商，配置TXT解析记录。通过命令 ```nslookup -q=TXT _acme-challenge.test.example.com``` 查询TXT记录是否生效了。

### 生成证书

下一步，工具就在本地生成证书。

```shell
-rw-r--r-- 1 root root 1870 Apr 25 19:44 cert1.pem
-rw-r--r-- 1 root root 1586 Apr 25 19:44 chain1.pem
-rw-r--r-- 1 root root 3456 Apr 25 19:44 fullchain1.pem
-rw------- 1 root root 1708 Apr 25 19:44 privkey1.pem
```

- cert1.pem: *.test.example.com 的证书文件
- chain1.pem: CA证书链
- fullchain1.pem: 完整的CA证书链
- privkey1.pem: *.test.example.com 的私钥文件

## Reference

[2020-ISRG-Annual-Report](https://www.abetterinternet.org/documents/2020-ISRG-Annual-Report.pdf)

[Let’s Encrypt: An Automated Certificate Authority to Encrypt the Entire Web](https://www.abetterinternet.org/documents/letsencryptCCS2019.pdf)