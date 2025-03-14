---
key: 20210718
title: Windows包管理服务CHOCOLATEY
tags: CHOCOLATEY 包管理
published: true
---

包管理可以认为是操作系统生态的核心，如果没有包管理，操作系统也没什么用。在```*nix```操作系统，包管理已经非常成熟，```apt-get```, ```yum```这些工具想必每个人都很熟悉。但是说到Windows系统，软件安装，大家熟悉的是双击、下一步下一步的方式；这种方式是对人设计的，与```apt-get```, ```yum```这种模式是不同的。也是因此，Windows软件自动化部署一直是一个难题。chocolatey 就是为了解决这个问题，定位为Windows系统上的```apt-get```, ```yum```。<!--more-->

## 使用 powershell 安装 CHOCOLATEY

1. 设置允许未签名的包安装

使用管理员运行 ```powershell```

```shell
PS C:\Users\m> Get-ExecutionPolicy
RemoteSigned

PS C:\Users\m> Set-ExecutionPolicy AllSigned

执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): Y
Set-ExecutionPolicy : Windows PowerShell 已成功更新你的执行策略，但在更具体的作业域中定义的策略覆盖了该设置。由于发生覆
盖，你的外壳程序将保留其当前的有效执行策略 RemoteSigned。请键入“Get-ExecutionPolicy -List”以查看你的执行策略设置。有
关详细信息，请参阅“Get-Help Set-ExecutionPolicy”。
所在位置 行:1 字符: 1
+ Set-ExecutionPolicy AllSigned
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : PermissionDenied: (:) [Set-ExecutionPolicy], SecurityException
    + FullyQualifiedErrorId : ExecutionPolicyOverride,Microsoft.PowerShell.Commands.SetExecutionPolicyCommand
PS C:\Users\m> Get-ExecutionPolicy -List

        Scope ExecutionPolicy
        ----- ---------------
MachinePolicy       Undefined
   UserPolicy       Undefined
      Process       Undefined
  CurrentUser    RemoteSigned
 LocalMachine       AllSigned

```

2. 安装

在 ```powershell``` 中执行如下命令

```shell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

```shell
Forcing web requests to allow TLS v1.2 (Required for requests to Chocolatey.org)
Getting latest version of the Chocolatey package for download.
Not using proxy.
Getting Chocolatey from https://community.chocolatey.org/api/v2/package/chocolatey/0.10.15.
Downloading https://community.chocolatey.org/api/v2/package/chocolatey/0.10.15 to C:\Users\m\AppData\Local\Temp\chocolatey\chocoInstall\chocolatey.zip
Not using proxy.
Extracting C:\Users\m\AppData\Local\Temp\chocolatey\chocoInstall\chocolatey.zip to C:\Users\m\AppData\Local\Temp\chocolatey\chocoInstall
Installing Chocolatey on the local machine
Creating ChocolateyInstall as an environment variable (targeting 'Machine')
  Setting ChocolateyInstall to 'C:\ProgramData\chocolatey'
WARNING: It's very likely you will need to close and reopen your shell
  before you can use choco.
Restricting write permissions to Administrators
We are setting up the Chocolatey package repository.
The packages themselves go to 'C:\ProgramData\chocolatey\lib'
  (i.e. C:\ProgramData\chocolatey\lib\yourPackageName).
A shim file for the command line goes to 'C:\ProgramData\chocolatey\bin'
  and points to an executable in 'C:\ProgramData\chocolatey\lib\yourPackageName'.

Creating Chocolatey folders if they do not already exist.

WARNING: You can safely ignore errors related to missing log files when
  upgrading from a version of Chocolatey less than 0.9.9.
  'Batch file could not be found' is also safe to ignore.
  'The system cannot find the file specified' - also safe.
chocolatey.nupkg file not installed in lib.
 Attempting to locate it from bootstrapper.
PATH environment variable does not have C:\ProgramData\chocolatey\bin in it. Adding...
警告: Not setting tab completion: Profile file does not exist at
'C:\Users\m00247266\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1'.
Chocolatey (choco.exe) is now ready.
You can call choco from anywhere, command line or powershell by typing choco.
Run choco /? for a list of functions.
You may need to shut down and restart powershell and/or consoles
 first prior to using choco.
Ensuring Chocolatey commands are on the path
Ensuring chocolatey.nupkg is in the lib folder
```

## 使用 CHOCOLATEY 安装包

```choco install ... ```

## Reference

[CHOCOLATEY](https://chocolatey.org/)

