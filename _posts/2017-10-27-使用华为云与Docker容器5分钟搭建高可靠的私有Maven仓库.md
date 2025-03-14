---
title: '使用华为云与Docker容器5分钟搭建高可靠的私有Maven仓库'
tags: 共有云 云厂商 华为云 docker maven
key: 20171027
---


## 问题
项目中存在一些私有的库，并未发布到Maven官方仓库，但是又需要共享给其他团队开发人员使用，需要搭建一个私有的maven仓库。
<!--more-->
## 传统思路
[]Maven](http://maven.apache.org/)仓库的实现软件是[Nexus](http://www.sonatype.org/nexus/)，那么需要找一台机器，安装Nexus以及依赖的软件包，配置Nexus，启动Nexus，创建仓库。
[这里](http://www.jianshu.com/p/9740778b154f)有详细的介绍。
## 容器解决方案
传统方式需要自己下载软件包、安装JDK、配置，相对麻烦。使用容器方案会简单很多。
Nexus的[Docker镜像](https://hub.docker.com/r/sonatype/nexus)在官方的DockerHub上已经有了，可以直接使用：
```
docker pull sonatype/nexus
docker run --name nexus -d -p 8081:8081 -eMAX_HEAP=768m sonatype/nexus
```
上述两个步骤完成之后，就可以通过界面访问了: http://ip:8080/nexus 。
## 使用华为云盘提升可靠性
现在只是通过容器快速运行了Maven仓库，但是容器内的数据都是只读的，如果上传了Maven库，容器重启后就会丢失，还不能实际使用。同时没有Internet可访问的IP，外部访问不了。
因此，使用华为云的ECS+弹性IP+云硬盘解决方案，是的Maven仓库最终可对外使用，数据不会丢失。
### 申请ECS+弹性IP
在申请到的虚拟机内运行nexus容器，将弹性IP地址绑定到虚拟机，所有Internet用户都可以访问这个Maven仓库了。
### 申请一块云硬盘
申请一块云硬盘，10G足够了，6个月18块钱：），使用LVM卷管理软件，将硬盘挂接到虚拟机。
```
pvcreate ...
vgcreate ...
lvcreate ...
mkfs.ext3 ...
mount -o <options> /mountpoint
```
使用LVM卷管理云硬盘的另外一个好处是，虚拟机重建之后，硬盘数据还在，可以在另外一台虚拟机通过扫描的方式，重新挂接，数据可以直接复用。
### 将虚拟机的目录挂接给容器使用
将云盘的挂接目录，通过容器卷 的方式，挂接给容器使用。
```
mkdir -p /mountpoint/repo
chown 200:200 /mountpoint/repo
docker run --name nexus -d -p 8081:8081 -eMAX_HEAP=768m -v /mountpoint/repo:/sonatype-work sonatype/nexus
```
注意上面第二行chown，因为在容器内nexus进程是以nexus:nexus用户运行的，uid与gid分别为200，因此Host机器上的目录权限要设置正确，否则容器内的nexus用户无权限写此目录。
## settings.xml配置
在setting.xml或pom.xml中增加私有仓库
```
	<profile>
		<id>cse-repo</id>
		<repositories>
			<repository>
				<id>my-repo</id>
				<name>my-repo</name>
				<url>http://ip:8081/nexus/content/repositories/my-repo</url>
			</repository>
		</repositories>
	</profile>
	...
  <activeProfiles>
	<activeProfile>cse-repo</activeProfile>
  </activeProfiles>	
```