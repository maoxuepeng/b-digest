---
title: '华为云微服务SDK与Kafka SDK无统一maven仓库导致的问题'
tags: 公有云 云厂商 华为云 DMS Kafka SDK Maven
key: 20180723
---

从昨晚到今天，遇到一个奇怪的问题，服务运行报华为云kafka sdk里的类找不到，但是在本地是正常的。
```
Caused by: javax.security.auth.login.LoginException: unable to find LoginModule class: com.huawei.middleware.kafka.sasl.client.KafkaLoginModule
	at javax.security.auth.login.LoginContext.invoke(LoginContext.java:794)
	at javax.security.auth.login.LoginContext.access$000(LoginContext.java:195)
	at javax.security.auth.login.LoginContext$4.run(LoginContext.java:682)
	at javax.security.auth.login.LoginContext$4.run(LoginContext.java:680)
	at java.security.AccessController.doPrivileged(Native Method)
	at javax.security.auth.login.LoginContext.invokePriv(LoginContext.java:680)
	at javax.security.auth.login.LoginContext.login(LoginContext.java:587)
	at org.apache.kafka.common.security.authenticator.AbstractLogin.login(AbstractLogin.java:58)
```
<!--more-->
到服务器上查看进程open的文件列表，果然没有dms.kafka.sasl.client-1.0.0.jar这个文件
```
/ # lsof
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	pipe:[29635340]
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	pipe:[29635341]
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	pipe:[29635342]
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/usr/lib/jvm/java-1.8-openjdk/jre/lib/rt.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/dialog-0.0.1-SNAPSHOT.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/sdk-0.0.1-SNAPSHOT.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/aopalliance-repackaged-2.5.0-b05.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/argparse4j-0.7.0.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/connect-api-0.10.2.0.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/kafka-clients-0.10.2.0.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/lz4-1.3.0.jar
1	/usr/lib/jvm/java-1.8-openjdk/jre/bin/java	/home/apps/server/lib/snappy-java-1.1.2.6.jar
...
```
由于Dockerfile中启动java的命令是```java -jar xx.jar```，那么就是xx.jar的MANIFEST.MF文件中的classpath不正确，打开此文件发现确实是没有dms.kafka.sasl.client-1.0.0.jar。

进一步排查原因是因为dms.kafka.sasl.client-1.0.0.jar不在远程maven仓库，是在本地目录下引入到项目编译的
```
        <dependency>
            <groupId>com.huawei.dms</groupId>
            <artifactId>dms.kafka.sasl.client</artifactId>
            <version>1.0.0</version>
            <type>jar</type>
            <scope>system</scope>
            <systemPath>${basedir}/libs/dms.kafka.sasl.client-1.0.0.jar</systemPath>
        </dependency>
```
按照maven官方解释，scope为system是不会打包到classpath中的，因此必须要将dms.kafka.sasl.client-1.0.0.jar放到远程maven仓库中。
