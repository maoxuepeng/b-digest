---
key: 20210529
title: WebAssembly – Where is it going?
tags: WebAssembly WASI WASM
---

"WebAssembly is a safe, portable, low-level code format designed for efficient execution and compact representation" – [W3C](https://www.w3.org/TR/wasm-core-1/#introduction%E2%91%A2).

本文章介绍WASM与WASI的应用场景，这些场景中已经有一些探索性的项目进行中，这些项目中隐含了未来应用架构与分发的模式。本文翻译自《[WebAssembly – Where is it going?](https://opencredo.com/blogs/webassembly-where-is-it-going/)》，作者为 [MATEUS PIMENTA](https://opencredo.com/authors/mateus-pimenta/) 。

## 从 WASM 到 WASI

当 [WebAssembly](http://webassembly.org/) (Wasm) 在[2017年被主流浏览器支持](https://blog.mozilla.org/blog/2017/11/13/webassembly-in-browsers/)的时候，代表着一种更快的（接近本地）在浏览器中运行计算机程序的技术标准成形。

不过，当 Mozilla 在 2019年发布 [WebAssembly System Interface (WASI)](https://hacks.mozilla.org/2019/03/standardizing-wasi-a-webassembly-system-interface/) 之时，这是一个革命性的时刻。WASI 解除了 WASM 仅浏览器运行中的限定，扩展到了作为一个独立的虚拟运行环境，可运行在主机上。这代表着一种全新的计算机应用程序编码、打包、运行的技术的诞生。

## 运行在浏览器中的WASM

在2017年 WASM 被主流浏览器（Microsoft Edge, Safari, Google Chrome and Firefox）支持之后，[W3C起草了一个WASM标准](https://www.w3.org/TR/wasm-core-1/)并很快的进入"[recommendation](https://www.w3.org/TR/wasm-core-1/)"状态，并在2019年正式发布。这意味着开发者可以在浏览器中以"[接近本地程序性能](https://people.mpi-sws.org/~rossberg/papers/Haas,%20Rossberg,%20Schuff,%20Titzer,%20Gohman,%20Wagner,%20Zakai,%20Bastien,%20Holman%20-%20Bringing%20the%20Web%20up%20to%20Speed%20with%20WebAssembly.pdf)"运行重负载的程序，不受JavaScript引擎性能限制、也没有跨浏览器适配问题。

在浏览器中使用WASM，开发者可以继续使用JavaScript开发传统的页面程序，同时将重负载的功能卸载到WASM编码的程序中，通过 [WebAssembly JS API](https://www.w3.org/TR/wasm-js-api/) 交互。

### 游戏

游戏是WASM最初始的目标场景，当得到一些游戏引擎公司的支持之后，（如 ```Unreal游戏引擎``` [宣布支持WASM](https://www.unrealengine.com/en-US/blog/unreal-engine-4-16-released)），牵引了WASM的技术构建方向。当然，WASM不仅仅用于游戏场景，在 [图像处理](https://silvia-odwyer.github.io/photon/demo.html) ， [视频处理](https://huningxin.github.io/opencv.js/samples/video-processing/index-wasm.html) ， [音频处理工作室](https://chrome.soundation.com/)，这些场景下的工作当前只能在桌面或服务器上完成。

### 人工智能模型推理

人工智能的模型推理也是WASM的一个典型场景。端侧的应用程序脱离服务端，直接加载复杂的模型，例如人脸识别，语音转文字，在端侧完成推理。所有的复杂逻辑都脱离了JavaScript，以Native Code方式运行。

Tensorflow.js 项目为此场景提供了一个WASM应用程序，Tensorflow.js还可以使用 multithreading and Single Instruction Multiple Data (SIMD) 技术加速计算。如果 WASM 的 Threading 与 SIMD 规范发布，一些新的项目将会随之出现用于工程化这些技术。

### 两个重要变化

在浏览器中执行重载计算的技术会带来两个显著变化。

1. 软件公司会开发更多的Web客户端应用程序。这种交付模式，相比较于软件包安装到用户端的机器上，能够简化应用程序的升级、安全补丁等维护工作。这个变化会更进一步加强SaaS这种商业模式。
2. 在客户端运行重载计算，相比较于Client-Server模式，消除了客户端与服务器端的运行时交互，用户体验会有一个越阶提升，同时也会减少软件厂商的网络、计算费用。

## 超越浏览器的WASM

当前，WASM只能在浏览器沙箱里运行Native Code。但是[WASI规范](https://hacks.mozilla.org/2019/03/standardizing-wasi-a-webassembly-system-interface/)中定义了[WASM沙箱与主机系统的文件、网络等交互的接口规范](https://github.com/WebAssembly/WASI/blob/master/phases/snapshot/docs.md)。这个能力允许我们在WASM沙箱中运行通用的应用程序，且可以获得可移植性、安全性等WebAssembly引入的特性。这里面隐含了深刻的内涵，我们逐一解读。

### 容器与容器编排

Docker 创始人 Solomon Hykes 发表过一个声明：[如果 WASM 与 WASI 早几年出现，就没有Docker什么事了](https://twitter.com/solomonstre/status/1111004913222324225?lang=en)。当然，这个并不表示立马要把当前所有的docker运行负载使用WebAssembly替换，但是这个表明了WebAssembly可以弥补当前docker容器的一些缺陷。

同时，主流的容器托管产品（AWS ECS, AWS Lambda (now with containers!), Google Cloud Run, Azure Containers Instances），都开始将WebAssembly作为一种替代传统容器的技术启动研究。
更进一步，微软的 Deis Labs 已经有了个 Krustlet 项目，可以将WebAssembly放到K8S中编排。

WebAssembly相对与传统的docker container，有几个优点。

- 安全。
  即便当前的container在安全领域有很多的防护手段，但是机制上，应用进程是可以直接访问到host主机的内核，因为container是通过cgroup实现的一种轻量级虚拟化技术，并不是完整内核虚拟化。虽然有 security context 机制，但是攻击面还是很大。当前也有一种使用完整内核虚拟化的趋势，包括 gVisor, Firecracker([AWS Lambda, AWS Farget产品都使用此虚拟化技术](https://aws.amazon.com/cn/blogs/aws/firecracker-lightweight-virtualization-for-serverless-computing/)), Kata。这表明安全是很重要的一个考量因素。
  WebAssembly 的安全模型是完整沙箱，这表明系统调用可控，内存安全，以及更少的攻击面。

- 包大小。
  容器镜像包大小一直是一个诟病点，由此出现了很多技术点以及最佳实践用于减少镜像包大小。这是因为机制上，容器镜像要求将内内核之外的、应用程序依赖的lib库都打包到镜像中，其目的是实现可移植性。
  WebAssembly的交付包只包含应用程序本身（[实际情况还会有15%的压缩](https://people.mpi-sws.org/~rossberg/papers/Haas,%20Rossberg,%20Schuff,%20Titzer,%20Gohman,%20Wagner,%20Zakai,%20Bastien,%20Holman%20-%20Bringing%20the%20Web%20up%20to%20Speed%20with%20WebAssembly.pdf)）。
  包大小减少后可以实现更短时间启动应用程序，如缩短函数计算中的"冷启动"时间。Fastly的Lucent叠加AOT技术，冷启动时间约 50微秒；Cloudflare 使用 V8引擎，冷启动时间 5毫秒。这对Serverless计算场景是非常重要的体验提升。

### 边缘计算

云厂商边缘计算服务已经应用了有些年了， [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/) 与 [Cloudflare Workers](https://workers.cloudflare.com/) 都是基于JavaScript引擎运行用户代码，现在WebAssembly提供了一个新的选项。

基于前面讨论的WebAssembly的有点，结合CND厂商的PoP点（point-of-presence），一种新的分布式计算应用架构正在形成。这种模式应用不仅能提升用户体验，还有显著的韧性属性、以及减少数据中心的网络与计算负载。

到目前为止，已经有厂商提供了基于WebAssembly的边缘计算服务。

- [Fastly Compute@Edge](https://www.fastly.com/products/edge-compute/serverless/) ，一个纯基于WebAssembly的的边缘计算解决方案。
- [Cloudflare Workers](https://workers.cloudflare.com/) ，在已有的边缘计算平台上增加WebAssembly支持。

### 嵌入式，IoT，移动应用，机器学习等

WASM正在被更多的领域采用。你可以集成WASM到应用程序中，比如在允许用户上传代码的应用，如规则引擎，可以使用WebAssembly评估规则代码的安全性。 [Wasmer](https://wasmer.io/) 估计是当前最好的 WASM 运行时。

在IoT领域也有一些 WASM 运行时，如  [wasm-micro-runtime](https://github.com/bytecodealliance/wasm-micro-runtime) 与 [wasm3](https://github.com/wasm3/wasm3) ，这些运行时降低了代码在不同设备上流转的复杂度。 wasm3 还支持 Android 与 iOS 设备。

Intel的工程师正在开发 [wasi-nn](https://www.w3.org/2020/06/machine-learning-workshop/talks/introducing_wasi_nn.html) ，这项工作的目的是使得机器学习代码在不同架构上流转更容易。

## 当前所处的阶段

WASM 在浏览器领域的应用相关技术已经基本成熟。WASI 规范也在稳步演进中，[一些模块已经实现了](https://github.com/WebAssembly/proposals/blob/master/README.md)，新的特性也在不断迭代中。在变成语言领域，已经有不少语言支持[编译为WebAssembly字节码](https://webassembly.org/getting-started/developers-guide/)，且[越来越成熟](https://github.com/appcypher/awesome-wasm-langs)。

在浏览器之外，除边缘计算之外，WASM还处于早期阶段，并不能立马替换container，最先出现的形式是混合编排，根据不同业务场景编排container与WASM。

WASI标准还在[4个阶段中的第2个](https://github.com/WebAssembly/WASI/blob/master/docs/Proposals.md)，WebAssembly/WASI性能提议也在[审议](https://www.usenix.org/system/files/atc19-jangda.pdf)中。

生态方面还需要一些考量，近期由WebAssembly 4 个sponsor 成立的[字节联盟](https://bytecodealliance.org/)致力与WASM与WASI的生态发展。

## 尝试一下

[webassembly.studio](https://webassembly.studio/)

[wasm.fastlylabs.com](https://wasm.fastlylabs.com/)

## Reference

[WebAssembly-Wiki](https://zh.wikipedia.org/wiki/WebAssembly)

[WebAssembly](https://developer.mozilla.org/zh-CN/docs/WebAssembly)

[WebAssembly – Where is it going?](https://opencredo.com/blogs/webassembly-where-is-it-going/)
