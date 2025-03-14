---
key: 20200422
title: 编译ffmpeg的Android版本
tags: ffmpeg android
published: true
---

编译Android版本的FFMpeg库。

<!--more-->

## 编译步骤

### 特别注意点

1. 需要提前编译好x264库
2. 关键编译选项：
3. 由于Android NDK在r18以及之后版本，就不包含gcc工具了，改为clang替换。
4. 建议生成独立NDK工具链编译。
5. 阅读[NDK官方文档]((https://developer.android.com/ndk/guides/standalone_toolchain?hl=zh-cn))很重要。

### 步骤

1. 获取ffmpeg[最新版本源码](https://ffmpeg.org/releases/ffmpeg-4.2.2.tar.bz2)
2. 准备编译环境
3. 编译

## 获取ffmpeg代码

从[官方网站](https://ffmpeg.org/releases/ffmpeg-4.2.2.tar.bz2)获取源码。

## 准备编译环境

参考 [2020-4-21-编译x264的Android版本]()

## 编译

### 解压源码

解压x264源码到任意目录

### configure/make/make install

编译脚本参考

```bash
MY_TOOLCHAINS=~/sources/ndk-toolchains-arm64-api29
SYSROOT=$MY_TOOLCHAINS/sysroot
PREFIX=./android/arm64
X264_HOME=~/sources/x264-master/android/arm64

# Add the standalone toolchain to the search path.
export PATH=$PATH:$MY_TOOLCHAINS/bin

# Tell configure what tools to use.
target_host=aarch64-linux-android
export AR=$target_host-ar
export AS=$target_host-clang
export CC=$target_host-clang
export CXX=$target_host-clang++
export LD=$target_host-ld
export STRIP=$target_host-strip

# Tell configure what flags Android requires.
export CFLAGS="-fPIE -fPIC"
export LDFLAGS="-pie"
export ADDI_CFLAGS="-I${X264_HOME}/include"
export EXTRA_CFLAGS="-mfloat-abi=softfp -mfpu=neon"

./configure \
    --prefix=${PREFIX} \
    --enable-shared \
    --enable-static \
    --enable-pic \
    --target-os=android \
    --disable-asm \
    --enable-gpl \
    --enable-cross-compile \
    --extra-cflags=-I${X264_HOME}/include \
    --extra-ldflags=-L${X264_HOME}/lib \
    --enable-libx264 \
    --sysroot=${SYSROOT}

make clean
make
make install


```

上述脚本编译时候会遇到这个错误：

```bash
STRIP   ffmpeg
strip: Unable to recognise the format of the input file `ffmpeg_g'
Makefile:104: recipe for target 'ffmpeg' failed
make: *** [ffmpeg] Error 1
```

原因是STRIP工具指向不正确，修改 ffbuild/config.mak，将 ```STRIP=strip``` 修改为 ```STRIP=aarch64-linux-android-strip``` ，重新执行 ```make;make install``` 即可。

编译完成后，在当前目录的 ```android/arm64/``` 目录下就有所有的输出文件了。

## Reference

[NDK 独立工具链](https://developer.android.com/ndk/guides/standalone_toolchain?hl=zh-cn)

[1.0-FFMPEG-Android利用ndk(r20)编译最新版本ffmpeg4.2.1](https://juejin.im/post/5d831333f265da03c61e8a28)