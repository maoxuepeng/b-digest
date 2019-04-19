---
layout: article
title: 云服务映射
---


## 计算 Compute

### 虚拟机 Virtual Servers

#### 基本CPU、内存配置虚拟机 Basic CPU/Memory Configed Virtual Server

- huawei cloud: [弹性云服务器 ECS](https://www.huaweicloud.com/product/ecs.html)
- aliyun: [云服务器ECS](https://www.aliyun.com/product/ecs)
- tencent cloud: [云服务器 CVM](https://cloud.tencent.com/product/cvm)
- aws: [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/cn/ec2/)
- azure: [Virtual Machines](https://azure.microsoft.com/en-us/services/virtual-machines/)
- google cloud: [可扩展的高性能虚拟机 COMPUTE ENGINE](https://cloud.google.com/compute/)

#### GPU硬件加速虚拟机 GPU Attached Virtual Server

- huawei cloud: [GPU加速云服务器](https://www.huaweicloud.com/product/gpu.html)
- aliyun: [GPU云服务器](https://www.aliyun.com/product/ecs/gpu)
- tencent cloud: [GPU 云服务器](https://cloud.tencent.com/product/gpu)
- aws: [Amazon EC2 Elastic GPU](https://aws.amazon.com/cn/ec2/elastic-gpus/)
- azure: [Virtual Machines, N-Series, GPU enabled virtual machines](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/)
- google cloud: [图形处理器 (GPU)](https://cloud.google.com/gpu/)

#### FPGA硬件加速虚拟机 FPGA Attached Virtual Server

- huawei cloud: [FPGA加速云服务器](https://www.huaweicloud.com/product/fcs.html)
- aliyun: [FPGA云服务器](https://www.aliyun.com/product/ecs/fpga)
- tencent cloud: [FPGA云服务器](https://cloud.tencent.com/product/fpga)
- aws: [Amazon EC2 F1](https://aws.amazon.com/hpc/)
- azure: No
- google cloud: No

#### InfiniBand硬件加速虚拟机 InfiniBand Network Attached Virtual Server

- huawei cloud: [弹性云服务器 ECS, 超高性能计算型H2, 超高性能计算型HI3](https://www.huaweicloud.com/product/ecs.html)
- aliyun: No
- tencent cloud: No
- aws: [Amazon EC2 P3?](https://aws.amazon.com/cn/ec2/instance-types/p3/)
- azure: No
- google cloud: No

#### 裸金属服务器 Bare Metal Server

- huawei cloud: [裸金属服务器 Bare Metal Server](https://www.huaweicloud.com/product/bms.html)
- aliyun: [弹性裸金属服务器（神龙）](https://www.aliyun.com/product/ebm)
- tencent cloud: [黑石物理服务器 Cloud Physical Machine](https://cloud.tencent.com/product/cpm?idx=1)
- aws: [Amazon EC2 I3 Bare Matel](https://aws.amazon.com/cn/ec2/instance-types/i3/)
- azure: No
- google cloud: [Google Actual Cloud Platform](https://cloud.google.com/actual-cloud/)

#### 虚拟机镜像服务 Virtual Server Image

- huawei cloud: [镜像服务 Image Management Service](https://www.huaweicloud.com/product/ims.html)
- aliyun: 未独立出产品，参考: [镜像管理](https://help.aliyun.com/document_detail/57014.html)
- tencent cloud: 未独立出产品，参考: [腾讯云系统镜像和使用镜像创建云主机](https://cloud.tencent.com/developer/article/1004469)
- aws: [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- azure: 未独立出产品，参考: [Create a managed image of a generalized VM in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/capture-image-resource)
- google cloud: 未独立出产品，参考: [Images](https://cloud.google.com/compute/docs/images#os-compute-support)


#### 轻量应用服务器 Virtual Private Server

- huawei cloud: No
- aliyun: [轻量应用服务器](https://www.aliyun.com/product/swas)
- tencent cloud: No
- aws: [Amazon Lightsail](https://aws.amazon.com/lightsail/)
- azure: No
- google cloud: [Google App Engine?](https://cloud.google.com/appengine/)


### 容器服务 Container Management

#### 专属集群 Decicated Cluster

Supports Docker/Kubernetes containers and allows users to run applications on managed instance clusters.

- huawei cloud: [云容器引擎（Cloud Container Engine）](https://www.huaweicloud.com/product/cce.html)
- aliyun: [容器服务 Container Service](https://www.aliyun.com/product/containerservice), [容器服务 Kubernetes版](https://www.aliyun.com/product/kubernetes)
- tencent cloud: [腾讯云容器服务（Tencent Kubernetes Engine ，TKE）](https://cloud.tencent.com/product/tke)
- aws: [Amazon Elastic Container Service](https://aws.amazon.com/ecs), [Amazon Elastic Container Service for Kubernetes](https://aws.amazon.com/eks/)
- azure: [Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/)
- google cloud: [KUBERNETES ENGINE](https://cloud.google.com/kubernetes-engine/)


#### 无服务器容器 Serverless Container

Allows customers to spin up container instances at Fargate Container Instances will without any additional installation of underlying infrastructure or hosts.

- huawei cloud: [云容器实例（Cloud Container Instance）](https://www.huaweicloud.com/product/cci.html)
- aliyun: 无独立服务目录，参考：[Serverless Kubernetes全新上线](https://yq.aliyun.com/articles/587195)
- tencent cloud: [容器实例服务 CIS](https://cloud.tencent.com/product/cis)
- aws: [AWS Fargate](https://aws.amazon.com/fargate/)
- azure: [Azure Container Instances](https://azure.microsoft.com/en-us/services/container-instances/)
- google cloud: No


#### 镜像仓库 Container Registry

Allows customers to store Docker formatted images. Used to create all types of container deployments on cloud.

- huawei cloud: [容器镜像服务（SoftWare Repository for Container）](https://www.huaweicloud.com/product/swr.html)
- aliyun: [容器镜像服务（Container Registry）](https://www.aliyun.com/product/acr)
- tencent cloud: 无独立服务目录，在TKS控制台可见
- aws: [Amazon Elastic Container Registry (ECR) ](https://aws.amazon.com/ecr/)
- azure: [Azure Container Registry](https://azure.microsoft.com/en-us/services/container-registry/)
- google cloud: [CONTAINER REGISTRY](https://cloud.google.com/container-registry/)

#### 镜像构建 Container Building
TODO

[Kubernetes Pod 设置 Docker run 的 shm_size 参数](http://t.thought.ink/2019/09/10/Docker-shm-size.html)
[11 Ways (Not) to Get Hacked](https://kubernetes.io/blog/2018/07/18/11-ways-not-to-get-hacked/)

### 批量计算 Batch Computing

When processing across hundreds or thousands of compute nodes, this tool orchestrates the tasks and interactions between compute resources that are necessary. 

- huawei cloud: [批处理服务（Batch Service）](https://www.huaweicloud.com/product/batch.html)
- aliyun: [批量计算（BatchCompute）](https://www.aliyun.com/product/batchcompute)
- tencent cloud: [批量计算 Batch](https://cloud.tencent.com/product/Batch)
- aws: [AWS Batch](https://aws.amazon.com/batch/)
- azure: [Azure Batch](https://azure.microsoft.com/en-us/services/batch/)
- google cloud: [CLOUD DATAFLOW](https://cloud.google.com/dataflow/)

### 弹性伸缩 Autoscaling

Automatically changes the number of instances providing a compute workload. Users set defined metrics and thresholds that  determine if the platform adds or removes instances.

- huawei cloud: [弹性伸缩（Auto Scaling）](https://www.huaweicloud.com/product/as.html)
- aliyun: [弹性伸缩（Auto Scaling）](https://www.aliyun.com/product/ess)
- tencent cloud: [弹性伸缩 AS](https://cloud.tencent.com/product/as)
- aws: [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- azure: [Azure Autoscale](https://azure.microsoft.com/en-us/features/autoscale/)
- google cloud: Autoscaling is a feature of [managed instance groups](https://cloud.google.com/compute/docs/instance-groups/)


### 函数服务 Function

Integrates systems and runs backend processes in response to events or schedules without provisioning or managing servers.

- huawei cloud: [函数工作流（FunctionGraph）](https://www.huaweicloud.com/product/functiongraph.html)
- aliyun: [函数计算（Function Compute）](https://www.aliyun.com/product/fc)
- tencent cloud: [无服务器云函数 SCF](https://cloud.tencent.com/product/scf)
- aws: [AWS Lambda](https://aws.amazon.com/lambda/)
- azure: [Azure Functions](https://azure.microsoft.com/en-us/services/functions/), [Azure Event Grid](https://azure.microsoft.com/en-us/services/event-grid/)
- google cloud: [Google Cloud Functions](https://cloud.google.com/functions/)


[各个厂商函数服务对比](http://t.thought.ink/2018/09/01/Function.html)

### 时钟同步 Time Sync Service

Enables customers to access time servers from Time Sync Service within the cloud network.

- huawei cloud: 
- aliyun: 
- tencent cloud: 
- aws: [Time sync service inside aws cloud](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-the-amazon-time-sync-service/)
- azure: 
- google cloud: 

## 存储

### 块存储 Block Device Storage

SSD storage optimized for I/O intensive read/write operations. 

- huawei cloud: [云硬盘（Elastic Volume Service）](https://www.huaweicloud.com/product/evs.html) 
- aliyun: [块存储](https://www.aliyun.com/product/disk)
- tencent cloud: [云硬盘 CBS](https://cloud.tencent.com/product/cbs)
- aws: [Amazon Elastic Block Store](https://aws.amazon.com/ebs/)
- azure: [Azure Disk Storage](https://azure.microsoft.com/en-us/services/storage/disks/)
- google cloud: [PERSISTENT DISK](https://cloud.google.com/persistent-disk/)


### 对象存储 Object Storage

Object storage service for use cases including cloud apps, content distribution, backup, archiving, disaster recovery, and big data analytics.

- huawei cloud: [对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html) 
- aliyun: [对象存储 OSS](https://www.aliyun.com/product/oss)
- tencent cloud: [对象存储 COS](https://cloud.tencent.com/product/cos)
- aws: [Amazon S3](https://aws.amazon.com/s3/)
- azure: [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
- google cloud: Google cloud [Google Cloud Storage](https://cloud.google.com/storage/)


### 归档存储 Archiving

A lower cost tier for storing data that is infrequently accessed and long-lived.

- huawei cloud: 对象存储的三种存储类型（标准、低频访问、归档） [对象存储服务 OBS](https://www.huaweicloud.com/product/obs.html) 
- aliyun: 对象存储的三种存储类型（标准、低频访问、归档） [对象存储 OSS](https://www.aliyun.com/product/oss)
- tencent cloud: [归档存储 CAS](https://cloud.tencent.com/product/cas)
- aws: [Amazon Glacier](https://aws.amazon.com/glacier)
- azure: Hot, Cool and Archive Tire: [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
- google cloud: Google cloud [Google ARCHIVAL CLOUD STORAGE](https://cloud.google.com/storage/archival/)


### 共享文件系统 Shared File Storage

A simple interface to create and configure file systems quickly as well as share common files. 

- huawei cloud: [弹性文件服务（Scalable File Service）](https://www.huaweicloud.com/product/sfs.html) 
- aliyun: [文件存储 NAS（ Network Attached Storage ）](https://www.aliyun.com/product/nas)
- tencent cloud: [文件存储 CFS](https://cloud.tencent.com/product/cfs)
- aws: [Amazon Elastic File System](https://aws.amazon.com/efs/)
- azure: [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
- google cloud: [CLOUD FILESTORE](https://cloud.google.com/filestore/)


### 备份 Backup

Backup and archival solutions that allow files and folders to be backed-up and recovered from the cloud, and provide off-site protection against data loss. 

- huawei cloud: No
- aliyun: [混合云备份（简称HBR）](https://www.aliyun.com/product/hbr)
- tencent cloud: No
- aws: No
- azure: [Azure Backup](https://azure.microsoft.com/en-us/services/backup/)
- google cloud: No


### 混合云存储 Hybird Cloud Storage

Integrates on-premises IT environments with cloud storage. Automates data management and storage, plus supports disaster recovery.

- huawei cloud: No
- aliyun: [云存储网关 Cloud Storage Gateway](https://www.aliyun.com/product/hcs)
- tencent cloud: [存储网关（Cloud Storage Gateway）](https://cloud.tencent.com/product/csg)
- aws: [AWS Storage Gateway](https://aws.amazon.com/storagegateway/)
- azure: [Azure StorSimple](https://azure.microsoft.com/en-us/services/storsimple/)
- google cloud: [由合作伙伴基于 Google Cloud Storage 提供服务](https://cloud.google.com/storage/partners/), 如 [Veritas NetBackup](https://www.veritas.com/solution/google-cloud-platform)


### PB级数据迁移 Petabyte-scale Data Transfer

Petabyte-sacle to Exabyte-scale data transport solution.

- huawei cloud: [数据快递服务（Data Express Service）](https://www.huaweicloud.com/product/des.html)
- aliyun: [闪电立方 Lightning Cube](https://www.aliyun.com/product/mgw)
- tencent cloud: [云数据迁移（Cloud Data Migration）](https://cloud.tencent.com/product/cdm)
- aws: [AWS Snowball](https://aws.amazon.com/snowball/)
- azure: [Azure Data Box Family](https://azure.microsoft.com/en-us/services/storage/databox/)
- google cloud: [Cloud Data Transfer Service](https://cloud.google.com/products/data-transfer/)


### 存储容灾 Disaster Recovery

Automates protection and replication of virtual machines with health monitoring, recovery plans, and recovery plan testing.

- huawei cloud: [存储容灾服务（Storage Disaster Recovery Service）](https://www.huaweicloud.com/product/sdrs.html)
- aliyun: [混合云容灾（Hybrid Disaster Recovery， 简称HDR) ](https://www.aliyun.com/product/hdr)
- tencent cloud: No
- aws: [AWS Disaster Recovery](https://aws.amazon.com/disaster-recovery/)
- azure: [Azure Site Recovery](https://azure.microsoft.com/en-us/services/site-recovery/)
- google cloud: No


## 网络与内容分发

### 云虚拟网络 Cloud Virtual Network

Provides an isolated, private environment in the cloud. 

- huawei cloud: [虚拟私有云（Virtual Private Cloud）](https://www.huaweicloud.com/product/vpc.html)
- aliyun: [专有网络 VPC](https://www.aliyun.com/product/vpc)
- tencent cloud: [私有网络 VPC](https://cloud.tencent.com/product/vpc)
- aws: [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)
- azure: [Azure Virtual Network](https://azure.microsoft.com/en-us/services/virtual-network/)
- google cloud: [VIRTUAL PRIVATE CLOUD (VPC)](https://cloud.google.com/vpc/)

### 跨界连接 Cross-premises Connectivity

Connects cloud virtual networks to other cloud virtual networks or customer on-premises networks. It also supports VPN tunneling. 

- huawei cloud: [虚拟专用网络（Virtual Private Network）](https://www.huaweicloud.com/product/vpn.html)
- aliyun: [VPN 网关](https://www.aliyun.com/product/vpn)
- tencent cloud: [VPN 连接](https://cloud.tencent.com/product/vpn)
- aws: 在VPC内创建[Customer Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/SetUpVPNConnections.html)
- azure: [Azure VPN Gateway](https://azure.microsoft.com/en-us/services/vpn-gateway/)
- google cloud: [GOOGLE CLOUD INTERCONNECT](https://cloud.google.com/interconnect/)-[IPsec VPN](https://cloud.google.com/vpn/docs/concepts/overview)

### 专属网络 Dedicated network

Establishes a dedicated, private network connection from a location to the cloud provider.

- huawei cloud: [云专线（Direct Connect）](https://www.huaweicloud.com/product/dc.html)
- aliyun: [高速通道](https://www.aliyun.com/product/expressconnect)
- tencent cloud: [专线接入（Direct Connect，DC）](https://cloud.tencent.com/product/dc)
- aws: [AWS Direct Connect](https://aws.amazon.com/directconnect)
- azure: [Azure ExpressRoute](https://azure.microsoft.com/en-us/services/expressroute/)
- google cloud: [GOOGLE CLOUD INTERCONNECT](https://cloud.google.com/interconnect/)-[专用（专用互连）](https://cloud.google.com/interconnect/docs/concepts/dedicated-overview)

### 负载均衡 Load Balancing

Automatically distributes incoming application traffic to add scale, handle failover, and route to a collection of resources.

- huawei cloud: [弹性负载均衡（ Elastic Load Balance）](https://www.huaweicloud.com/product/elb.html)
- aliyun: [负载均衡 SLB](https://www.aliyun.com/product/slb)
- tencent cloud: [负载均衡（Cloud Load Balancer，CLB）](https://cloud.tencent.com/product/clb)
- aws: [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing)
- azure: [Azure Load Balancer](https://azure.microsoft.com/en-us/services/load-balancer/)
- google cloud: [GOOGLE CLOUD LOAD BALANCING](https://cloud.google.com/load-balancing/)

### API 网关 API Gateway

API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale.

- huawei cloud: [API网关（API Gateway）](https://www.huaweicloud.com/product/apig.html)
- aliyun: [API 网关（API Gateway）](https://www.aliyun.com/product/apigateway)
- tencent cloud: [API 网关（API Gateway）](https://cloud.tencent.com/product/apigateway)
- aws: [Amazon API Gateway](https://aws.amazon.com/api-gateway)
- azure: [Azure Application Gateway](https://azure.microsoft.com/en-us/services/application-gateway/)
- google cloud: [GOOGLE CLOUD ENDPOINTS](https://cloud.google.com/endpoints/)

### 域名管理 Domain name system management

Service that hosts domain names, routes users to Internet applications, manages traffic to apps, and improves app availability with automatic failover.

- huawei cloud: [云解析服务（Domain Name Service）](https://www.huaweicloud.com/product/dns.html)
- aliyun: [云解析 DNS（Domain Name System，简称DNS）](https://wanwang.aliyun.com/domain/dns)
- tencent cloud: [云解析](https://cloud.tencent.com/product/cns)
- aws: [Amazon Route 53](https://aws.amazon.com/route53)
- azure: [Azure DNS](https://azure.microsoft.com/en-us/services/dns/), [Azure Traffic Manager](https://azure.microsoft.com/en-us/services/traffic-manager/)
- google cloud: [CLOUD DNS](https://cloud.google.com/dns/)


### 内容分发网络 Content Delivery Network

Global content delivery network that transfers audio, video, applications, images, and other files.

- huawei cloud: [内容分发网络（CDN）](https://www.huaweicloud.com/product/cdn.html)
- aliyun: [CDN](https://www.aliyun.com/product/cdn)
- tencent cloud: [静态内容加速 SCD](https://cloud.tencent.com/product/cdn-scd), [下载分发加速 DD](https://cloud.tencent.com/product/cdn-dd), [音视频点播加速 VCD](https://cloud.tencent.com/product/cdn-vcd)
- aws: [Amazon CloudFront](https://aws.amazon.com/cloudfront)
- azure: [Azure Content Delivery Network](https://azure.microsoft.com/en-us/services/cdn/)
- google cloud: [CLOUD CDN](https://cloud.google.com/cdn/)

### NAT 网关 NAT Gateway

Provides Source Network Address Translation (SNAT) and Destination Network Address Translation (DNAT) functions for virutal servers in a Virtual Private Cloud (VPC), making it easier for you to configure the ingress and egress for a VPC.

- huawei cloud: [NAT网关（NAT Gateway）](https://www.huaweicloud.com/product/nat.html)
- aliyun: [NAT网关](https://www.aliyun.com/product/nat)
- tencent cloud: [NAT 网关](https://cloud.tencent.com/product/nat)
- aws: [Amazon VPC Nat Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
- azure: No
- google cloud: No

### VPC全球互联
全部部署的业务通过云服务商的全球互联网络打通连接。

- huawei cloud: [云连接（Cloud Connect）](https://www.huaweicloud.com/product/cc.html)
- aliyun: [云企业网](https://cn.aliyun.com/product/cbn)
- tencent cloud: [云联网 CCN](https://cloud.tencent.com/product/ccn)
- aws: [AWS PrivateLink](https://aws.amazon.com/privatelink)
- azure: [ExpressRoute](https://azure.microsoft.com/en-us/services/expressroute/)
- google cloud: No


## 数据库

### 关系数据库 MySQL Relation Database MySQL

- huawei cloud: [云数据库 MySQL](https://www.huaweicloud.com/product/mysql.html)
- aliyun: [云数据库RDS MySQL 版](https://www.aliyun.com/product/rds/mysql)
- tencent cloud: [云数据库 TencentDB for MySQL](https://cloud.tencent.com/product/cdb)
- aws: [Amazon RDS for MySQL](https://aws.amazon.com/rds/mysql/)
- azure: [Azure Database for MySQL](https://azure.microsoft.com/en-us/services/mysql/)
- google cloud: [Cloud SQL for MySQL](https://cloud.google.com/sql/docs/mysql/quickstart)

### 关系数据库 MariaDB Relation Database MariaDB

- huawei cloud: No
- aliyun: No
- tencent cloud: [云数据库 TencentDB for MariaDB](https://cloud.tencent.com/product/tdsql)
- aws: [Amazon RDS for MariaDB](https://aws.amazon.com/rds/mariadb/)
- azure: No
- google cloud: No

### 关系数据库 PostgreSQL Relation Database PostgreSQL

- huawei cloud: [云数据库 PostgreSQL](https://www.huaweicloud.com/product/pg.html)
- aliyun: [云数据库RDS PostgreSQL 版](https://www.aliyun.com/product/rds/postgresql)
- tencent cloud: [云数据库 TencentDB for PostgreSQL](https://cloud.tencent.com/product/postgresql)
- aws: [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/)
- azure: [Azure Database for PostgreSQL](https://azure.microsoft.com/en-us/services/postgresql/)
- google cloud: [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres/quickstart)

### 关系数据库 SQLServer Relation Database SQLServer

- huawei cloud: [云数据库 SQL Server](https://www.huaweicloud.com/product/mssql.html)
- aliyun: [云数据库RDS SQL Server 版](https://www.aliyun.com/product/rds/sqlserver)
- tencent cloud: [云数据库 TencentDB for SQL Server](https://cloud.tencent.com/product/sqlserver)
- aws: [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/)
- azure: [Azure SQL Database](https://azure.microsoft.com/en-us/services/sql-database/)
- google cloud: [GOOGLE CLOUD PLATFORM 上的 SQL SERVER](https://cloud.google.com/sql-server/)

### 缓存数据库 Redis

- huawei cloud: [分布式缓存服务 Redis](https://www.huaweicloud.com/product/dcs.html)
- aliyun: Serverless HBASE: [云数据库 Redis 版](https://www.aliyun.com/product/kvstore)
- tencent cloud: [云数据库 TencentDB for Redis](https://cloud.tencent.com/product/crs)
- aws: [Amazon Elastic Cache for Redis](https://aws.amazon.com/redis/)
- azure: [Azure Redis Cache](https://azure.microsoft.com/en-us/services/cache/)
- google cloud: [GOOGLE CLOUD MEMORYSTORE](https://cloud.google.com/memorystore/)

### 缓存数据库 Memcached

- huawei cloud: [分布式缓存服务 Memcached](https://www.huaweicloud.com/product/dcsmem.html)
- aliyun: Serverless HBASE: [云数据库 Memcache 版（ ApsaraDB for Memcache ）](https://www.aliyun.com/product/ocs)
- tencent cloud: [云数据库 TencentDB for Memcached](https://cloud.tencent.com/product/cmem)
- aws: [Amazon Elastic Cache for Memcached](https://aws.amazon.com/memcached/)
- azure: No, [Azure Marketplace](https://azure.microsoft.com/en-us/updates/memcached-cloud-available-in-the-azure-store/)
- google cloud: No

### NoSQL 文档数据库 NoSQL document storage

- huawei cloud: [文档数据库服务 DDS](https://www.huaweicloud.com/product/dds.html)
- aliyun: [云数据库 MongoDB版](https://www.aliyun.com/product/mongodb)
- tencent cloud: [云数据库 TencentDB for MongoDB](https://cloud.tencent.com/product/mongodb)
- aws: Serverless: [Amazon DynamoDB](https://aws.amazon.com/dynamodb/), Hosted: [Amazon SimpleDB](https://aws.amazon.com/simpledb/)
- azure: [Azure Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/)
- google cloud: [GOOGLE CLOUD DATASTORE](https://cloud.google.com/datastore/)

### NoSQL 列数据库 NoSQL column storage

- huawei cloud: [表格存储服务(CloudTable)](https://www.huaweicloud.com/product/cloudtable.html)
- aliyun: Serverless HBASE: [表格存储（Table Store）](https://www.aliyun.com/product/ots), Hosted HBASE: [云数据库 HBase 版（ApsaraDB for HBase）](https://www.aliyun.com/product/hbase)
- tencent cloud: [列式数据库HBase（Cloud HBase Service）](https://cloud.tencent.com/product/HBase)
- aws: [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- azure: [Azure Table Storage](https://azure.microsoft.com/en-us/services/storage/tables/)
- google cloud: [GOOGLE CLOUD BIGTABLE](https://cloud.google.com/bigtable/)

### 图数据库 Graph Database

- huawei cloud: [图引擎服务（Graph Engine Service）](https://www.huaweicloud.com/product/ges.html)
- aliyun: No
- tencent cloud: No
- aws: [Amazon Neptune](https://aws.amazon.com/neptune/)
- azure: [Azure Cosmos DB](https://azure.microsoft.com/en-us/services/cosmos-db/)
- google cloud: No

### 数据库迁移服务 Database migration 

- huawei cloud: [数据复制服务（Data Replication Service，简称为DRS）](https://www.huaweicloud.com/product/drs.html)
- aliyun: [数据传输服务(Data Transmission Service) ](https://www.aliyun.com/product/dts)
- tencent cloud: [数据传输服务 DTS](https://cloud.tencent.com/product/dts)
- aws: [AWS Database Migration Service](https://aws.amazon.com/dms/)
- azure: [Azure Database Migration Service](https://azure.microsoft.com/en-us/services/database-migration/)
- google cloud: [GOOGLE CLOUD DATA TRANSFER](https://cloud.google.com/products/data-transfer/)

## 数据分析与大数据 Analytics & Big Data

### 数据仓库 Data warehouse
A fully managed data warehouse that analyzes data using business intelligence tools. 

- huawei cloud: [数据仓库服务（Data Warehouse Service，简称DWS）](https://www.huaweicloud.com/product/dws.html)
- aliyun: [分析型数据库（AnalyticDB 原ADS）](https://www.aliyun.com/product/ads)
- tencent cloud: [Snova 数据仓库](https://cloud.tencent.com/product/snova)
- aws: [Amazon Redshift](https://aws.amazon.com/redshift)
- azure: [SQL Data Warehouse](https://azure.microsoft.com/en-us/services/sql-data-warehouse/)
- google cloud: [GOOGLE BIGQUERY](https://cloud.google.com/bigquery/)

### 大数据处理 Big data processing (MapReduce)
Supports technologies that break up large data processing tasks into multiple jobs, and then combine the results to enable massive parallelism.

- huawei cloud: [MapReduce服务（MapReduce Service）](https://www.huaweicloud.com/product/mrs.html)
- aliyun: [大数据计算服务 · MaxCompute](https://www.aliyun.com/product/odps),[E-MapReduce](https://www.aliyun.com/product/emapreduce)
- tencent cloud: [弹性MapReduce （EMR）](https://cloud.tencent.com/product/emr)
- aws: [Amazon EMR](https://aws.amazon.com/emr)
- azure: [HDInsight](https://azure.microsoft.com/en-us/services/hdinsight/)
- google cloud: [CLOUD DATAPROC](https://cloud.google.com/dataproc/)


### 数据管道 Data Pipeline
Processes and moves data between different compute and storage services, as well as on-premises data sources at specified intervals. 

- huawei cloud: [数据接入服务 Data Ingestion Service](https://www.huaweicloud.com/product/dis.html)
- aliyun: No
- tencent cloud: No
- aws: [AWS Data Pipeline](https://aws.amazon.com/datapipeline/)
- azure: [Data Factory](https://azure.microsoft.com/en-us/services/data-factory/)
- google cloud: [Pipelines](https://cloud.google.com/dataflow/model/pipelines) in [Dataflow](https://cloud.google.com/dataflow)

### Cloud ETL (extract, transform, and load)
Cloud-based ETL/data integration service that orchestrates and automates the movement and transformation of data from various sources.

- huawei cloud: No
- aliyun: No
- tencent cloud: No
- aws: [AWS Glue](https://aws.amazon.com/glue)
- azure: [Data Factory](https://azure.microsoft.com/en-us/services/data-factory/), [Data Catalog](https://azure.microsoft.com/en-us/services/data-catalog/)
- google cloud: [CLOUD COMPOSER](https://cloud.google.com/composer/)

### 流数据采集服务

- huawei cloud: [数据接入服务 Data Ingestion Service](https://www.huaweicloud.com/product/dis.html)
- aliyun: No
- tencent cloud: No
- aws: [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- azure: [Event Hubs](https://azure.microsoft.com/en-us/services/event-hubs/)
- google cloud: [CLOUD PUB/SUB](https://cloud.google.com/pubsub/)

### 流数据加载服务

- huawei cloud: No
- aliyun: No
- tencent cloud: No
- aws: [Amazon Kinesis Data Firehose](https://aws.amazon.com/kinesis/data-firehose/)
- azure: No
- google cloud: No

### 流数据分析服务

- huawei cloud: [实时流计算服务（Cloud Stream Service, 简称CS）](https://www.huaweicloud.com/product/cs.html), [数据湖工厂（Data Lake Factory）](https://www.huaweicloud.com/product/dlf.html), [数据湖探索 DLI](https://www.huaweicloud.com/product/dli.html)
- aliyun: [Dataworks](https://data.aliyun.com/product/ide), [实时计算 Flink(Alibaba Cloud Realtime Compute)（原阿里云流计算）](https://data.aliyun.com/product/sc)
- tencent cloud:  [流计算服务 SCS](https://cloud.tencent.com/product/scs)
- aws: [Amazon Kinesis Data Analytics](https://aws.amazon.com/kinesis/data-analytics/)
- azure: [Azure Stream Analytics](https://azure.microsoft.com/en-us/services/stream-analytics/), [Azure Data Lake Storage](https://azure.microsoft.com/en-us/services/storage/data-lake-storage/), [Azure Data Lake Analytics](https://azure.microsoft.com/en-us/services/data-lake-analytics/)
- google cloud: [CLOUD DATAFLOW](https://cloud.google.com/dataflow/)

### 数据湖探索 Data discovery
A serverless interactive query service that uses standard SQL for analyzing databases.

- huawei cloud: [数据湖探索 DLI](https://www.huaweicloud.com/product/dli.html)
- aliyun: [Data Lake Analytics](https://www.aliyun.com/product/datalakeanalytics)
- tencent cloud: [数据工坊TDF](https://cloud.tencent.com/product/tdf)
- aws: [Amazon Athena](https://aws.amazon.com/athena/)
- azure: [Azure Data Lake Analytics](https://azure.microsoft.com/en-us/services/data-lake-analytics/)
- google cloud: [GOOGLE BIGQUERY](https://cloud.google.com/bigquery/)

### 报表 Visualization
Business intelligence tools that build visualizations, perform ad-hoc analysis, and develop business insights from data.

- huawei cloud: No
- aliyun: [数加 · Quick BI](https://data.aliyun.com/product/bi)
- tencent cloud: [腾讯云商业智能分析（Business Intelligence）](https://cloud.tencent.com/product/bi)
- aws: [Amazon QuickSight](https://aws.amazon.com/quicksight/)
- azure: [PowerBI](https://powerbi.microsoft.com), [Power BI Embedded](https://azure.microsoft.com/en-us/services/power-bi-embedded/)
- google cloud: No

## 物联网 (IoT)

### 设备操作系统 Device Operating System
IoT operating system for microcontrollers

- huawei cloud: No
- aliyun: [AliOS Things](https://iot.aliyun.com/products/aliosthings)
- tencent cloud: No
- aws: [Amazon FreeRTOS](https://aws.amazon.com/freertos)
- azure: No
- google cloud: No

### 边缘计算 Edge Computing
Local compute, messaging, data caching, sync, and Machine Learning inference capabilities for connected devices.

- huawei cloud: [智能边缘平台（Intelligent EdgeFabric ）](https://www.huaweicloud.com/product/ief.html)
- aliyun: [物联网边缘计算](https://www.aliyun.com/product/iotedge)
- tencent cloud: No
- aws: [AWS Greengrass](https://aws.amazon.com/greengrass)
- azure: [Azure IoT Edge](https://azure.microsoft.com/en-us/services/iot-edge/)
- google cloud: [Cloud IoT Edge](https://cloud.google.com/iot-edge/)

### 设备连接
Easily and securely connect devices to the cloud. Reliably scale to billions of devices and trillions of messages.

- huawei cloud: [ROMA联接服务（ROMA Link）](https://www.huaweicloud.com/product/link.html), [OceanConnect 物联网平台](https://www.huaweicloud.com/product/iot.html)
- aliyun: [物联网设备接入](https://www.aliyun.com/product/iot-deviceconnect)
- tencent cloud: [腾讯云物联网通信（Internet of Things Hub， IoT Hub）](https://cloud.tencent.com/product/iothub)
- aws: [AWS IoT Core](https://aws.amazon.com/iot-core)
- azure: [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/)
- google cloud: [CLOUD IOT CORE](https://cloud.google.com/iot-core/)

### 设备管理
Onboard, organize, monitor, and remotely manage connected devices at scale.

- huawei cloud: [ROMA联接服务（ROMA Link）](https://www.huaweicloud.com/product/link.html), [OceanConnect 物联网平台](https://www.huaweicloud.com/product/iot.html)
- aliyun: [物联网设备管理](https://cn.aliyun.com/product/iot-devicemanagement)
- tencent cloud: No
- aws: [AWS IoT Device Management](https://aws.amazon.com/iot-device-management)
- azure: [Azure IoT Hub](https://azure.microsoft.com/en-us/services/iot-hub/)
- google cloud: [CLOUD IOT CORE](https://cloud.google.com/iot-core/)

### 设备数据处理 IoT analytics
Analytics for IoT devices. Because IoT data always noisy ,inconsistant and etc, IoT analytics help the data engineer and data analyst for data COLLECT, PROCESS, ANALYSTIC.

- huawei cloud: No
- aliyun: [物联网数据分析](https://cn.aliyun.com/product/iot-dataanalytics)
- tencent cloud: No
- aws: [AWS IoT Analytics](https://aws.amazon.com/iot-analytics)
- azure: No
- google cloud: No

### 设备接入安全管理
Security management for IoT devices.

- huawei cloud: No
- aliyun: [物联网设备身份认证](https://iot.aliyun.com/products/ID2), [物联网安全运营中心—IoT SOC（Security Operations Center）](https://cn.aliyun.com/product/iot-devicedefender), [物联网可信执行环境-Link TEE（Trusted Execution Environment）](https://iot.aliyun.com/products/tee), [物联网可信服务管理-Link TSM（Trusted Service Manager）](https://iot.aliyun.com/products/tsm)
- tencent cloud: No
- aws: [AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender)
- azure: No
- google cloud: No

### 物联网一站式开发平台
物联网一站式开发服务：设备开发、服务开发、Web开发和移动开发。

- huawei cloud: No
- aliyun: [Link Develop](https://iot.aliyun.com/products/linkdevelop)
- tencent cloud: No
- aws: No
- azure: [Azure IoT Central](https://azure.microsoft.com/en-us/services/iot-central/), [Azure IoT solution accelerators](https://azure.microsoft.com/en-us/features/iot-accelerators/)
- google cloud: [Firebase](https://firebase.google.com)

## 人工智能


## 开发者工具&管理工具 Developer Tools & Management Tools
### 应用开发平台
Hosted platform for application(specially microservices architecture) framework, deploy, register and discovery, management. The open source frameworks are: [SpringCloud](http://cloud.spring.io/), [ServiceComb](https://servicecomb.apache.org/), [Dubbo](https://dubbo.incubator.apache.org/), [Motan](https://github.com/weibocom/motan) etc.

- huawei cloud: [微服务云应用平台 ServiceStage](https://www.huaweicloud.com/product/servicestage.html)
- aliyun: [企业级分布式应用服务 EDAS](https://www.aliyun.com/product/edas)
- tencent cloud: [移动开发平台 MobileLine](https://cloud.tencent.com/product/tac), [云开发（Tencent Cloud Base，TCB，基于function的小程序开发平台）](https://cloud.tencent.com/product/tcb), [腾讯分布式服务框架 TSF (Tencent Distributed Service Framework) ](https://cloud.tencent.com/product/tsf)
- aws: [Microservices on AWS](https://docs.aws.amazon.com/aws-technical-content/latest/microservices-on-aws/microservices-on-aws.pdf?icmpid=link_from_whitepapers_page)
- azure: [Azure Service Fabric](https://azure.microsoft.com/en-us/services/service-fabric/)
- google cloud: [Google App Engine](https://appengine.google.com/)

### 云编排 

- huawei cloud: [应用编排服务（Application Orchestration Service）](https://www.huaweicloud.com/product/aos.html)
- aliyun: [资源编排（Resource Orchestration）](https://www.aliyun.com/product/ros)
- tencent cloud: 
- aws: [AWS Cloud​Formation](https://aws.amazon.com/cloudformation/)
- azure: [Azure Resource Manager](https://azure.microsoft.com/en-us/features/resource-manager/)
- google cloud: [CLOUD DEPLOYMENT MANAGER](https://cloud.google.com/deployment-manager/)

### 监控 Monitoring
Monitor resources and applications. The open source products are: Nagios, Zipkin, Prometheus etc.

- huawei cloud: [云监控服务（Cloud Eye Service）](https://www.huaweicloud.com/product/ces.html), [应用运维管理（Application Operations Management ）](https://www.huaweicloud.com/product/aom.html)
- aliyun: [云监控](https://www.aliyun.com/product/jiankong)
- tencent cloud: [云监控 CM](https://cloud.tencent.com/product/cm)
- aws: [Amazon CloudWatch](https://aws.amazon.com/cloudwatch)
- azure: [Azure Monitor](https://azure.microsoft.com/en-us/services/monitor/), [Microsoft Azure portal](https://azure.microsoft.com/en-us/features/azure-portal/)
- google cloud: [STACKDRIVER MONITORING](https://cloud.google.com/monitoring/)

### 日志 Logging
Application log collect, search. The open source products are: Logstash, Fluentd etc.

- huawei cloud: [云日志服务（Log Tank Service）](https://www.huaweicloud.com/product/lts.html), [应用运维管理（Application Operations Management ）](https://www.huaweicloud.com/product/aom.html)
- aliyun: [日志服务（Log Service，简称LOG/原SLS）](https://www.aliyun.com/product/sls)
- tencent cloud: [日志服务 CLS](https://cloud.tencent.com/product/cls), 
- aws: [ Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- azure: No
- google cloud: [STACKDRIVER LOGGING](https://cloud.google.com/logging/)

### 性能与调用链跟踪 Traceing
An extensible application performance management service for web developers on multiple platforms. The open sources products are: [Open Tracing](https://opentracing.io/), [Pinpoint](https://github.com/naver/pinpoint), [Jaeger](https://github.com/jaegertracing/jaeger) etc.

- huawei cloud: [应用性能管理（Application Performance Management）](https://www.huaweicloud.com/product/apm.html)
- aliyun: [业务实时监控服务 (Application Real-Time Monitoring Service, 简称ARMS)](https://www.aliyun.com/product/arms)
- tencent cloud: [织云 COC](https://cloud.tencent.com/product/coc), [腾讯客户端性能分析 QAPM](https://cloud.tencent.com/product/qapm)
- aws: [AWS X-Ray](https://aws.amazon.com/xray/)
- azure: No
- google cloud: No


### 应用配置管理 Application Configuration Management
Application configuration templating, rendering, notification. The open source solution: [confd](https://github.com/kelseyhightower/confd)+[etcd](https://github.com/etcd-io/etcd)

- huawei cloud: No
- aliyun: [应用配置管理（Application Configuration Management，简称 ACM）](https://www.aliyun.com/product/acm)
- tencent cloud: No
- aws: No
- azure: No
- google cloud: No

### 应用事务管理
- huawei cloud: No
- aliyun: [全局事务服务（Global Transaction Service ，简称GTS）](https://www.aliyun.com/aliware/txc)
- tencent cloud: No
- aws: No
- azure: No
- google cloud: No

### 性能压测 
应用压测工具，广泛应用的产品有 [Jmeter](https://jmeter.apache.org/), [LoadRunner](https://software.microfocus.com/es-es/products/loadrunner-load-testing/overview)

- huawei cloud: [云性能测试服务（Cloud Performance Test Service）](https://www.huaweicloud.com/product/cpts.html)
- aliyun: [性能测试PTS（Performance Testing Service）](https://www.aliyun.com/product/pts)
- tencent cloud: No
- aws: No
- azure: No
- google cloud: No

### 消息队列 Streaming Message Queue
用于高吞吐、高可靠的数据传输场景的队列，当前最广泛被应用的开源产品为 Kafka 。
- huawei cloud: [分布式消息服务 Kafka](https://www.huaweicloud.com/product/dmskafka.html)
- aliyun: [消息队列 Kafka](https://www.aliyun.com/product/kafka)
- tencent cloud: [消息队列 CKafka](https://cloud.tencent.com/product/ckafka)
- aws: [Amazon Managed Streaming for Kafka (MSK) - public preview](https://aws.amazon.com/msk)
- azure: [Azure Event Hubs for Kafka Ecosystems in public preview](https://azure.microsoft.com/en-us/blog/azure-event-hubs-for-kafka-ecosystems-in-public-preview/)
- google cloud: No

### 消息队列 AMPQ
应用最广泛的标准 [AMPQ](https://www.amqp.org/) 协议的队列实现，当前最广泛被应用的开源产品为  RabbitMQ, ActiveMQ。
- huawei cloud: [分布式消息队列 RabbitMQ](https://www.huaweicloud.com/product/rabbitmq.html)
- aliyun: [消息队列 AMQP](https://www.aliyun.com/product/amqp)
- tencent cloud: No
- aws: [Amazon MQ](https://aws.amazon.com/amazon-mq/)
- azure: No
- google cloud: No


## 安全、身份管理与访问控制
### 秘钥管理与数据加密
秘钥管理与数据加密服务，秘钥使用FIPS 140-2 认证的硬件安全模块(Hardware Security Module)保存，秘钥更新，提供[信封加密](https://help.aliyun.com/knowledge_detail/42339.html)等功能。
- huawei cloud: [数据加密服务 DEW](https://www.huaweicloud.com/product/dew.html)
- aliyun: [密钥管理服务（KeyManagementService）](https://www.aliyun.com/product/kms)
- tencent cloud: [数据加密服务](https://cloud.tencent.com/product/cloudhsm)
- aws: [AWS Key Management Service](https://aws.amazon.com/kms)
- azure: [Key Vault](https://azure.microsoft.com/en-us/services/key-vault/)
- google cloud: [CLOUD KEY MANAGEMENT SERVICE](https://cloud.google.com/kms/)


## 软件开发工具

## 应用&数据集成 Application and Data Integration

## 应用市场


## References
- [AWS vs. Azure vs. GCP](https://www.cloudyn.com/wp-content/uploads/2016/05/AWS-GCP-Azure-May-2016-final.pdf)
- [AWS to Azure services comparison](https://docs.microsoft.com/en-us/azure/architecture/aws-professional/services)
- [Comparing Kubernetes Services on AWS vs. Azure vs. GCP](https://www.sumologic.com/blog/cloud/kubernetes-aws-azure-gcp/)
- [Google Cloud Platform for AWS Professionals](https://cloud.google.com/docs/compare/aws/)
- [Map AWS services to Google Cloud Platform products](https://cloud.google.com/free/docs/map-aws-google-cloud-platform)
- [System Properties Comparison Amazon DynamoDB vs. Amazon SimpleDB vs. MongoDB](https://db-engines.com/en/system/Amazon+DynamoDB%3BAmazon+SimpleDB%3BMongoDB)
- [CNCF Landscape](https://github.com/cncf/landscape)
- [AWS IoT vs. Google IoT vs. Azure IoT](https://www.bizety.com/2018/08/28/aws-iot-vs-google-iot-vs-azure-iot/)