---
key: 20180910
title: Kubernetes Pod 设置 Docker run 的 shm_size 参数
tags: Cloud-Service-Mapping Computing Docker Kubernetes
---

## shm_size
docker run 默认的共享内存大小 /dev/shm 为 64M，某些场景想增加此挂载目录的大小，在swarm或直接docker run的方式，通过 ```--shm_size=xxxM``` 方式可以设置共享内存大小。
但是通过 Kubernetes 创建的 Pod 无法指定 docker run 的参数，具体讨论可参考 [issue-28272](https://github.com/kubernetes/kubernetes/issues/28272)。

建议通过 [mount 一个介质为 Memory 的 EmptyDir](https://docs.okd.io/latest/dev_guide/shared_memory.html) 方式变通解决此问题。
