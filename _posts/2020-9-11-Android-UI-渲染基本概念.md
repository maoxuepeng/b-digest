---
key: 20200911
title: Android UI 渲染基本概念
tags: Adnroid 渲染 
---

本文介绍Android UI渲染基本概念。<!--more-->

## 概念

### Android Window 概念

![](/images/rendering/window-system.png)

#### 1. Activity

Android中对用户提供功能的接口。官方对Activity的介绍：```移动应用体验与桌面体验的不同之处在于，用户与应用的互动并不总是在同一位置开始，而是经常以不确定的方式开始。例如，如果您从主屏幕打开电子邮件应用，可能会看到电子邮件列表，如果您通过社交媒体应用启动电子邮件应用，则可能会直接进入电子邮件应用的邮件撰写界面。Activity 类的目的就是促进这种范式的实现。当一个应用调用另一个应用时，调用方应用会调用另一个应用中的 Activity，而不是整个应用。通过这种方式，Activity 充当了应用与用户互动的入口点。```

#### 2. PhoneWindow

每个Activity都有一个Window实例，其类型为PhoneWindow。PhoneWindow持有一个Window Manager实例用于管理布局与DecorView。

#### 3. DecorView

DecorView继承自FrameLayout，DecorView包含两个sub-View：TitleView 与 ContentView 。开发者在```Activity```的```OnCreate```方法中调用的```SetContentView```方法，就是将View设置到 ContentView 。

#### 4. WindowManager

```java
public interface WindowManager extends ViewManager {
    Display getDefaultDisplay();

    void removeViewImmediate(View var1);
    ......//ellipsis
}
```

WindowsManger 继承自ViewManager，因此WindowsView可以增、删、更新View。
WindowsManger 在Activity执行```attach()```方法时候被创建，```attach()```方法在```onCreate()```之前被创建。

#### 5. View

界面元素抽象容器。

### Surface 概念

![](/images/rendering/android-canvas-draw-flow.png)

#### 1. Surface

Surface 是一块缓冲区，生产方（Windows体系）将需要绘制到屏幕的数据写入缓冲区，消费方（ SurfaceFlinger ）负责读取缓冲区数据，通过 HWC 最终绘制到屏幕上。

#### 2. SurfaceFinger

消费 Surface 缓冲区数据，交给HWC绘制到屏幕上。

#### 3. HWC (Hardware Compositor)

[HWC](https://source.android.google.cn/devices/graphics/implement-hwc?hl=zh-cn) 在Android中是一个HAL定义，硬件实现由具体厂家提供。HWC最终负责图形上屏显示。
同时HWC还负责产生```VSYNC```信号。

#### 4. Canvas

将 Surface 缓冲区封装为```画布```，提供给应用程序绘图。典型的Android UI绘图使用 [Skia](https://skia.org/) 库，那么Skia就是画笔。应用程序通过Skia画笔，在Canvas画布上画各种形状，最终提交到缓冲区，由SurfaceFlinger响应VSYNC信号，在屏幕上显示。

## UI 渲染流程

![](/images/rendering/android-ui-drow-flow.png)

## Reference

1. [Android 之如何优化 UI 渲染（上）](https://www.jianshu.com/p/c61307e79ac2)
2. [Android window mechanism](https://programmer.group/android-window-mechanism.html)
3. [Understanding Canvas and Surface concepts](https://stackoverflow.com/questions/4576909/understanding-canvas-and-surface-concepts)
4. [Android UI System](https://www.slideshare.net/lekaha/android-ui-system)
5. [Activity 简介](https://developer.android.com/guide/components/activities/intro-activities?hl=zh-cn)
6. [Surface 和 SurfaceHolder](https://source.android.com/devices/graphics/arch-sh?hl=zh-cn)
7. [实现硬件混合渲染器 HAL](https://source.android.google.cn/devices/graphics/implement-hwc?hl=zh-cn)
