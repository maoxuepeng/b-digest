---
key: 20190324
title: 在Docker中运行Android模拟器
tags: Docker Android
published: false
---

### 模拟器
#### ANB
[ANDROID IN A BOX](https://anbox.io/), [https://github.com/anbox/anbox](https://github.com/anbox/anbox)

1. 在Ubuntu1804上安装
    1. 安装内核模块 ashmem,binder
    ```
    $ sudo add-apt-repository ppa:morphis/anbox-support
    $ sudo apt update
    $ sudo apt install linux-headers-generic anbox-modules-dkms
    $ sudo modprobe ashmem_linux
    $ sudo modprobe binder_linux
    $ ls -1 /dev/{ashmem,binder}
    ```

    2. 安装ANB
    ```
    $ sudo snap install --devmode --beta anbox
    ```

    3. 确认安装结果
    ```
    snap info anbox

    name:      anbox
    summary:   Android in a Box
    publisher: morphis
    contact:   https://anbox.io
    license:   unset
    description: |
    Runtime for Android applications which runs a full Android system
    in a container using Linux namespaces (user, ipc, net, mount) to
    separate the Android system fully from the host.

    You can find further details in our documentation at
    https://github.com/anbox/anbox/blob/master/README.md
    commands:
    - anbox
    - anbox.android-settings
    - anbox.appmgr
    - anbox.collect-bug-info
    - anbox.shell
    services:
    anbox.container-manager: simple, enabled, active
    snap-id:      Nr9K6UJaIOD8wHpDEQl16nabFFt9LLEQ
    tracking:     beta
    refresh-date: 4 days ago, at 20:14 CST
    channels:
    stable:    –
    candidate: –
    beta:      4-e1ecd04 2018-10-17 (158) 391MB devmode
    edge:      4-d521e28 2019-03-13 (173) 391MB devmode
    installed:   4-e1ecd04            (158) 391MB devmode

    ```

    4. 安装adb
    安装应用程序在Anbox中，目前只能通过ADB工具来安装。
    

#### genymotion
[genymotion](https://www.genymotion.com/)


### 控制微信

