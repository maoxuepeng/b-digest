---
title: 'windows 1709 powershell使用总结'
tags: windows 1709 powershell docker
key: 20180801
---

## 配置powershell远程连接
[配置指南](https://yq.aliyun.com/articles/576063)
## 远程连接
服务端执行
```
PS C:\Users\Administrator> enable-psremoting -force
PS C:\Users\Administrator> set-netfirewallrule -name "winrm-http-in-tcp-public" -remoteaddress any
```
<!--more-->
客户端执行
```
PS C:\tmp\suda> Set-Item wsman:localhost\client\trustedhosts -value 114.116.83.44 -force
PS C:\tmp\suda> enter-pssession '114.116.81.9' -credential:'administrator'
```
## service 管理
### new-service
### get-service
### remove-service
powershell 还未提供此命令，使用如下方式替代：
```
get-ciminstance win32_service -filter "name='your-service-name'" | remove-instance 
```
或：
```
sc.exe delete your-service-name
```
或：
```
(get-wmiobject win32_service -filter "name='your-service-name'").delete()
```
## 拷贝文件
### cp
### cpoy-item

## windows feature
###  get-windowsfeature -name *framework*
```
[114.116.81.9]: PS C:\S3Cloud-Docker2> get-windowsfeature -name *framework*

Display Name                                            Name                       Install State
------------                                            ----                       -------------
[ ] .NET Framework 3.5 功能                               NET-Framework-Features         Available
    [ ] .NET Framework 3.5 (包括 .NET 2.0 和 3.0)          NET-Framework-Core               Removed
[X] .NET Framework 4.7 功能                               NET-Framework-45-Fea...        Installed
    [X] .NET Framework 4.7                              NET-Framework-45-Core          Installed
    [ ] ASP.NET 4.7                                     NET-Framework-45-ASPNET        Available

```

## 配置ftp
```
PS C:\suda\sdtestservice> get-windowsfeature *ftp*

Display Name                                            Name                       Install State
------------                                            ----                       -------------
    [ ] FTP 服务器                                      Web-Ftp-Server                 Available
        [ ] FTP 服务                                    Web-Ftp-Service                Available
        [ ] FTP 扩展                                    Web-Ftp-Ext                    Available


PS C:\suda\sdtestservice> install-windowsfeature Web-Ftp-Server

Success Restart Needed Exit Code      Feature Result
------- -------------- ---------      --------------
True    No             Success        {FTP 服务器, FTP 服务}


PS C:\suda\sdtestservice> get-process *ftp*
PS C:\suda\sdtestservice> import-module webadministration
PS C:\suda\sdtestservice> new-webftpsite -name suda -port 21 -force

Name             ID   State      Physical Path                  Bindings
----             --   -----      -------------                  --------
suda             1696 Started                                   ftp *:21:
                 5705
                 67


PS C:\suda\sdtestservice> cmd /c \windows\system32\inetsrv\appcmd set site "suda" "-virtualDirectoryDefaults.physicalPath:c:\suda"
SITE 对象“suda”已更改
PS C:\suda\sdtestservice> set-itemproperty "iis:\sites\suda" -name ftpserver.security.authentication.basicAuthentication.enabled -value $true
PS C:\suda\sdtestservice> set-itemproperty "iis:\sites\suda" -name ftpserver.userisolation.mode -value 3
PS C:\suda\sdtestservice> set-itemproperty "iis:\sites\suda" -name ftpserver.security.userisolation. -value $true
set-itemproperty : 在 \\ECS-SUDA\Sites\suda 上找不到属性 ftpserver.security.userisolation.。
参数名: propName
所在位置 行:1 字符: 1
+ set-itemproperty "iis:\sites\suda" -name ftpserver.security.userisola ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-ItemProperty]，ArgumentException
    + FullyQualifiedErrorId : InvalidArgument,Microsoft.PowerShell.Commands.SetItemPropertyCommand

PS C:\suda\sdtestservice> set-itemproperty "iis:\sites\suda" -name ftpserver.security.userisolation -value $true
set-itemproperty : 在 \\ECS-SUDA\Sites\suda 上找不到属性 ftpserver.security.userisolation。
参数名: propName
所在位置 行:1 字符: 1
+ set-itemproperty "iis:\sites\suda" -name ftpserver.security.userisola ...
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidArgument: (:) [Set-ItemProperty]，ArgumentException
    + FullyQualifiedErrorId : InvalidArgument,Microsoft.PowerShell.Commands.SetItemPropertyCommand

PS C:\suda\sdtestservice> set-itemproperty "iis:\sites\suda" -name ftpserver.security.userisolation -value $true^C
PS C:\suda\sdtestservice> add-webconfiguration "/system.ftpserver/security/authorization" -value @{accesstype="Allow";roles="";permissions="Read,Write";users
="*"} -pspath iis:\ -location "suda"
PS C:\suda\sdtestservice> restart-webitem "iis:\sites\suda"
```
### 启用telnet客户端
```
install-windowsfeature Telnet-Client
```

## 华为云windows容器镜像
swr.cn-north-1.myhuaweicloud.com/microsoft/mssql-server-windows-developer:1709