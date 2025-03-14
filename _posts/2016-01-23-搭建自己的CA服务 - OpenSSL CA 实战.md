---
tags: openssl ca ssl
key: 20160123
title: '搭建自己的CA服务 - OpenSSL CA 实战'
---

当前网络安全事故不断，如何提升系统安全性是一个系统上线之前必须考虑的重点DFx特性之一。在提升系统安全性的方法中，给每个端口（通道）加上SSL协议是最通用和有效的一种。

使用SSL就必须要有证书，在互联网世界里，有专门的组织机构给各个公司、组织、团体颁发证书，并保证其证书的有效性（通过颁发吊销列表使其实效）。这个颁发证书的机构我们称为CA。
<!--more-->
不过找CA申请颁发证书是需要费用的。而在一些分布式系统中，内部节点之间通信通道需要SSL加密和认证，这种场景下，每个内部节点都去CA结构申请颁发一个证书没有必要，也费钱。 [^1]

所以，搭建一个CA是非常有必要的。当前很多开源软件也都有自己的CA，典型的如 [Puppet](https://puppetlabs.com)：Puppet 的 Agent 在启动时候，会请求 Puppet CA 颁发一个证书，只有 CA 颁发证书给 Agent 之后，Agent 才可以连接到 Puppet Master 。

OpenSSL是目前最流行的SSL开源实现，这里介绍如何使用OpenSSL搭建一个CA服务。

## 思路
搭建CA服务分为3个阶段。

0. 规划证书属性和服务器环境准备
1. 准备CA证书，包括CA根证书（信任证书），CA的私钥
2. 使用CA证书颁发证书

### 0.准备 openssl.conf 配置环境
这个配置文件定义了证书生成的一些属性，Internet上很多相关的介绍。笔者参考的是这个 http://www.phildev.net/ssl/opensslconf.html 。
下面是我们要用到的 openssl.conf 文件：

	#http://www.phildev.net/ssl/opensslconf.html
    [ ca ]
    default_ca = CA_default

    [CA_default]
    dir = .
    certs       = $dir/certsdb
    new_certs_dir   = $certs
    database    = $dir/index.txt
    certificate = $dir/ca_cert.pem
    private_key = $dir/ca_key.pem
    serial      = $dir/serial
    #crldir     = $dir/crl
    #crlnumber  = $dir/crlnumber
    #crl        = $crldir/crl.pem
    RANDFILE    = $dir/private/.rand

    x509_extensions = usr_cert

    #copy_extensions    = copy

    name_opt        = ca_default
    cert_opt        = ca_default

    default_days    = 365
    #default_crl_days= 30

    default_md      = sha256
    preserve        = no

    policy          = policy_match

    [ policy_match ]
    countryName             = match
    stateOrProvinceName     = match
    localityName            = supplied
    organizationName        = match
    organizationalUnitName  = optional
    commonName              = supplied
    emailAddress            = optional

    [ policy_anything ]
    countryName             = optional
    stateOrProvinceName     = optional
    localityName            = optional
    organizationName        = optional
    organizationalUnitName  = optional
    commonName              = supplied
    emailAddress            = optional

    [ req ]
    default_bits            = 4096
    default_keyfile         = privkey.pem
    distinguished_name      = req_distinguished_name
    attributes              = req_attributes
    x509_extensions     = v3_ca
    req_extensions      = v3_req

    string_mask = nombstr

    [ req_distinguished_name ]
    C = CN
    ST = GuangDong
    L = ShenZhen
    O = UProject
    OU = Yunweipai
    CN = www.yunweipai.com
    emailAddress = web@yunweipai.com

    [ req_attributes ]

    [ usr_cert ]
    basicConstraints = CA:false
    subjectKeyIdentifier = hash
    authorityKeyIdentifier = keyid,issuer

    [ v3_req ]
    subjectAltName = email:move

    [ v3_ca ]
    subjectKeyIdentifier=hash
    authorityKeyIdentifier=keyid:always,issuer:always
    basicConstraints = CA:true

上面的 openssl.conf 配置，需要在服务器上准备好如下目录和文件：

1. mkdir certsdb
2. touch index.txt
3. touch index.txt.attr
4. echo 01 > serial [^3]

### 1. 准备CA证书
##### 1.创建CA的私钥
创建一个长度为4096 bits的私钥，以AES128算法加密，加密密钥为 Yunweipai@123

	mao@ubuntu:/home/yunweipai/openssl_ca$ openssl genrsa -aes128 -passout pass:Yunweipai@123 4096 > ca_key.pem
	Generating RSA private key, 4096 bit long modulus
	.................................................................................................................++
	.........++
	e is 65537 (0x10001)

##### 2.创建CA的证书请求
指定证书的 subject 

	mao@ubuntu:/home/yunweipai/openssl_ca$ openssl req -new -key ca_key.pem -passin pass:Yunweipai@123 -config openssl.conf -subj "/C=CN/ST=GuangDong/L=ShenZhen/O=UProject/OU=UProject/CN=UProject-CA" -batch -out ca_csr.pem

##### 3.自颁发证书 [^2]

	mao@ubuntu:/home/yunweipai/openssl_ca$ openssl ca -config openssl.conf -create_serial -out ca_cert.cer -days 365 -keyfile ca_key.pem -key Yunweipai@123 -selfsign -in ca_csr.pem 
    Using configuration from openssl.conf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
            Serial Number: 1 (0x1)
            Validity
                Not Before: Apr 29 16:15:58 2015 GMT
                Not After : Apr 28 16:15:58 2016 GMT
            Subject:
                countryName               = CN
                stateOrProvinceName       = GuangDong
                localityName              = ShenZhen
                organizationName          = UProject
                organizationalUnitName    = UProject
                commonName                = UProject-CA
            X509v3 extensions:
                X509v3 Basic Constraints: 
                    CA:FALSE
                X509v3 Subject Key Identifier: 
                    DD:A7:68:BD:02:D3:D1:9C:15:5A:37:C2:FD:8F:16:13:D6:FB:08:9D
                X509v3 Authority Key Identifier: 
                    keyid:DD:A7:68:BD:02:D3:D1:9C:15:5A:37:C2:FD:8F:16:13:D6:FB:08:9D

    Certificate is to be certified until Apr 28 16:15:58 2016 GMT (365 days)
    Sign the certificate? [y/n]:y

    1 out of 1 certificate requests certified, commit? [y/n]y
    Write out database with 1 new entries
    Data Base Updated

### 2. 使用CA证书颁发证书
##### 1.创建申请者的私钥
创建一个长度为4096 bits的私钥，以AES128算法加密，加密密钥为 Yunweipai@123

	mao@ubuntu:/home/yunweipai/user_certs$ openssl genrsa -aes128 -passout pass:Yunweipai@123 -out web_key.pem
	Generating RSA private key, 2048 bit long modulus
	......................................................+++
	...............................................+++
	e is 65537 (0x10001)

##### 2.创建申请者的证书颁发请求
指定 subject，这里的 subject 与 CA 的 subject 不能相同

	mao@ubuntu:/home/yunweipai/user_certs$ openssl req -new -key 	web_key.pem -passin pass:Yunweipai@123 -config /home/yunweipai/openssl_ca/openssl.conf -subj "/C=CN/ST=GuangDong/L=ShenZhen/O=UProject/OU=Yunweipai/CN=www.yunweipai.com" -batch -out 	web_csr.pem

##### 3.申请颁发证书
在实际生产环境中，一般 CA 服务器都独立部署，因为申请颁发证书的过程是申请者将证书请求（CSR）发送给CA服务器，CA服务器接收到了之后，通过下面命令颁发证书，然后将证书返回给申请者

    mao@ubuntu:/home/yunweipai/openssl_ca$ openssl ca -days 365 -config openssl.conf -keyfile ca_key.pem -key Yunweipai@123 -cert ca_cert.cer -in /home/yunweipai/user_certs/web_csr.pem -out web.cer
    Using configuration from openssl.conf
    Check that the request matches the signature
    Signature ok
    Certificate Details:
            Serial Number: 2 (0x2)
            Validity
                Not Before: Apr 29 16:25:16 2015 GMT
                Not After : Apr 28 16:25:16 2016 GMT
            Subject:
                countryName               = CN
                stateOrProvinceName       = GuangDong
                localityName              = ShenZhen
                organizationName          = UProject
                organizationalUnitName    = Yunweipai
                commonName                = www.yunweipai.com
            X509v3 extensions:
                X509v3 Basic Constraints: 
                    CA:FALSE
                X509v3 Subject Key Identifier: 
                    9D:A4:E9:7B:5F:74:3C:60:4D:E8:6B:54:2A:F0:68:36:58:9B:F7:85
                X509v3 Authority Key Identifier: 
                    keyid:DD:A7:68:BD:02:D3:D1:9C:15:5A:37:C2:FD:8F:16:13:D6:FB:08:9D

    Certificate is to be certified until Apr 28 16:25:16 2016 GMT (365 days)
    Sign the certificate? [y/n]:y

    1 out of 1 certificate requests certified, commit? [y/n]y
    Write out database with 1 new entries
    Data Base Updated

好了，证书终于颁发完了，通过这个命令，可以验证web.cer是由ca_cert.cer颁发的：
    
    mao@ubuntu:/home/yunweipai/openssl_ca$ openssl verify -CAfile 	ca_cert.cer web.cer 
    web.cer: OK

[^1]:  一般找CA申请证书，通常是给对外部（用户）提供服务的端口使用。比如我们访问淘宝网站，主域名对应端口（80）上使用的证书，就是从CA申请的。CA申请到的证书，一般浏览器都可以信任，不会弹出站点不可信的错误信息。这就是Money的力量：）
[^2]: CA只能自己给自己颁发证书，因为自己是根，没有其他人能给CA颁发证书。
[^3]: serial 纪录证书的序列号，这个值一定要是2位或以前的值，如果只是 1 是不行的。