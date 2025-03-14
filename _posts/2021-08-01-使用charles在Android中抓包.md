---
key: 20210801
title: 使用Charles抓安卓应用的网络请求包
tags: Android
---

抓包是分析应用程序行为以及定位问题的常用手段，在Linux上抓包工具为```tcpdump```，在Windows上常用的抓包工具为```wireshark```。虽然Android也是Linux，可以使用```tcpudmp```，但是```tcpdump```要求```root```权限，这个对Android来说要求就有点高了。因此在Android上使用```Charles```作为替代工具。<!--more-->

## Charles 下载安装

在[Charles](https://www.charlesproxy.com/)官网，下载，安装到PC或服务器上。

## 连接与配置

1. 手机需要与PC/服务器在同一个网络。
2. 启动Charles，设置一个监听端口，默认为```8888```。
3. 手机一般使用Wifi接入，因此在Wifi接入配置时候，在高级配置中设置代理，代理服务器地址，配置为Charles所在机器的IP地址，端口为Charles监听端口。
4. 此时在Charles上可以看到抓取到的手机网络包。

## HTTPS配置

Charles可以抓到所有的网络包，但是只能解开HTTP/HTTPS的包。对于HTTPS协议，需要配置Charles证书。

1. 在PC/服务器，安装Charles的CA证书，到操作系统的信任证书链中：```Help->SSL Proxying->Install Charls root certificate```。
2. 在手机端，安装Charles的CA证书，到操作系统的信任证书链中: 打开浏览器，输入```chls.pro/ssl```，下载证书，并安装证书。


## Reference

[Charles](https://www.charlesproxy.com/)
