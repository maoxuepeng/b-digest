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

PS C:\suda\sdtestservice> set-itemproperty "iis:\sites\suda" -name ftpserver.security.userisolation -value $true

PS C:\suda\sdtestservice> add-webconfiguration "/system.ftpserver/security/authorization" -value @{accesstype="Allow";roles="";permissions="Read,Write";users
="*"} -pspath iis:\ -location "suda"
PS C:\suda\sdtestservice> restart-webitem "iis:\sites\suda"
```

### 启用telnet客户端

```
install-windowsfeature Telnet-Client
```

### 压缩与解压

compress-archive

extract-archive

### 通过 Set-Processmitigation 命令关闭 DEP (Data Execution Prevention)

#### 1. 参考如下方法设置 DEP：
[Customize Exploit protection](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-exploit-guard/customize-exploit-protection)
[Powershell关闭DEP方法](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-exploit-guard/customize-exploit-protection#cmdlets-table)


#### 2. 在使用上述方法之前，需要安装一个powershell的[ProcessMitigations工具包](https://www.powershellgallery.com/packages/ProcessMitigations/1.0.7)

通过 ```Install-Module -Name ProcessMitigations``` 在线安装：

```
PS C:\Users\Administrator> Install-Module -Name ProcessMitigations

需要使用 NuGet 提供程序来继续操作
PowerShellGet 需要使用 NuGet 提供程序“2.8.5.201”或更高版本来与基于 NuGet 的存储库交互。必须在“C:\Program
Files\PackageManagement\ProviderAssemblies”或“C:\Users\Administrator\AppData\Local\PackageManagement\ProviderAssemblies”中提供 NuGet
提供程序。也可以通过运行 'Install-PackageProvider -Name NuGet -MinimumVersion 2.8.5.201 -Force' 安装 NuGet 提供程序。是否要让 PowerShellGet 立即安装并导入
NuGet 提供程序?
[Y] 是(Y)  [N] 否(N)  [S] 暂停(S)  [?] 帮助 (默认值为“Y”):

不受信任的存储库
你正在从不受信任的存储库安装模块。如果你信任该存储库，请通过运行 Set-PSRepository cmdlet 更改其 InstallationPolicy 值。是否确实要从“PSGallery”安装模块?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): A
```

#### 3. 如果需要离线安装，则将在线安装的包save到本地，然后通过指定path方式安装。

参考 [通过指定Path方式安装](https://activedirectorypro.com/install-powershell-modules/)

- Save到本地目录

Powershell module 查找路径： ```$Env:PSModulePath```

```
Save-Module -Name ProcessMitigations -Path /
```

- 将save的文件拷贝到查找路径

```
PS C:\> cp .\ProcessMitigations 'C:\Program Files\WindowsPowerShell\Modules\' -recurse
PS C:\> ls  'C:\Program Files\WindowsPowerShell\Modules\'


    Directory: C:\Program Files\WindowsPowerShell\Modules


Mode                LastWriteTime         Length Name
----                -------------         ------ ----
d-----        9/29/2017   8:28 PM                Microsoft.PowerShell.Operation.Validation
d-----        9/29/2017   8:28 PM                PackageManagement
d-----        9/29/2017   8:28 PM                Pester
d-----        9/29/2017   8:28 PM                PowerShellGet
d-----         9/8/2018  12:50 PM                ProcessMitigations
d-----        9/29/2017   8:28 PM                PSReadline

```

- 查看可用module

```
PS C:\> Get-Module -ListAvailable


    Directory: C:\Program Files\WindowsPowerShell\Modules


ModuleType Version    Name                                ExportedCommands
---------- -------    ----                                ----------------
Script     1.0.1      Microsoft.PowerShell.Operation.V... {Get-OperationValidation, Invoke-OperationValidation}
Binary     1.0.0.1    PackageManagement                   {Find-Package, Get-Package, Get-PackageProvider, Get-PackageSource...}
Script     3.4.0      Pester                              {Describe, Context, It, Should...}
Script     1.0.0.1    PowerShellGet                       {Install-Module, Find-Module, Save-Module, Update-Module...}
Binary     1.0.7      ProcessMitigations                  {Get-ProcessMitigation, Set-ProcessMitigation, ConvertTo-ProcessMitigationPolicy}
Script     1.2        PSReadline                          {Get-PSReadlineKeyHandler, Set-PSReadlineKeyHandler, Remove-PSReadlineKeyHandler, Get-PSReadlin...

```

- 导入powershell module

```
PS C:\> Import-module -name ProcessMitigations
```

** 在 docker 环境下，制作docker镜像时候，在dockerfile中执行上述离线安装步骤。 **

#### 4. 安装完成后，可以执行如下命令查看，设置进程的DEP

```
Set-Processmitigation -Name <process-name> -Disable DEP
PS C:\> Set-Processmitigation -Name <PROCESS-NAME.exe> -Disable DEP
PS C:\> Get-ProcessMitigation -name <PROCESS-NAME.exe>

ProcessName: <PROCESS-NAME.exe>
Source     : Registry
Id         : 0

DEP:
    Enable                      : off
    Disable ATL                 : off

...

```

## 华为云windows容器镜像
swr.cn-north-1.myhuaweicloud.com/microsoft/mssql-server-windows-developer:1709

## nds配置
### 查看DNS配置
Get-DnsClientServerAddress

### 设置DNS解析
Set-DnsClientServerAddress
