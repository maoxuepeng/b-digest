---
key: 20190707
title: AWS Nitro 架构
tags: AWS Nitro
published: false
---

Cloud Weekly 2019年27周。<!--more-->

## AWS祭出杀手锏Nitro架构：EC2价格降幅最高达到49％

[AWS祭出杀手锏Nitro架构：EC2价格降幅最高达到49％](https://new.qq.com/omn/20190620/20190620A0USGI.html)

6月20日，AWS在技术峰会上海站宣布，在光环新网运营的AWS中国（北京）区域和西云数据运营的AWS中国（宁夏）区域，近期对Amazon EC2新一代5系列C5和R5计算实例，以及GPU加速计算实例P3进行了主动降价。根据客户所选的实例类型不同，客户可以看到27%到49%之间的降幅。

AWS新一代5系列Amazon EC2实例，基于AWS最新的Nitro架构进行了优化。云计算的底层基础是虚拟化。虚拟化在带来资源灵活性、提升利用效率的同时，在性能方面会打折扣，主要是CPU要承担虚拟化管理方面的开销。AWS Nitro架构的做法是，将原本在通用CPU里运行的虚拟化管理程序 (Hypervisior) 抽离到了专有硬件上，这样，用户买到的资源就不再打折扣了，比如CPU和内存资源就更足量。如果说腾出来的CPU计算资源量不好描述的话，那么内存容量的足额交付就非常直观。

AWS首席技术布道师Jeff Bar在一篇博客里写道：有了Nitro的实例跟裸机服务器主机相比，性能只差了大约1%，这一微小差别很难察觉出来。

![](![](http://ww1.sinaimg.cn/large/712516f0ly1g4ri6pvb4rj20rs0f3gmd.jpg))