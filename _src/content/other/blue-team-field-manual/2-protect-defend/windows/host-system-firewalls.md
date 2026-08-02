# HOST SYSTEM FIREWALLS

Show all rules:

```bash
C:\> netsh advfirewall firewall show rule name=all
```

Set firewall on/off:

```bash
C:\> netsh advfirewall set currentprofile state on
C:\> netsh advfirewall set currentprofile
firewallpolicy blockinboundalways,allowoutbound
C:\> netsh advfirewall set publicprofile state on
C:\> netsh advfirewall set privateprofile state on
C:\> netsh advfirewall set domainprofile state on
C:\> netsh advfirewall set allprofile state on
C:\> netsh advfirewall set allprofile state off
```

Set firewall rules examples:

```bash
C:\> netsh advfirewall firewall add rule name="Open
Port 80" dir=in action=allow protocol=TCP
localport=80
C:\> netsh advfirewall firewall add rule name="My
Application" dir=in action=allow
program="C:\MyApp\MyApp.exe" enable=yes
C:\> netsh advfirewall firewall add rule name="My
Application" dir=in action=allow
program="C:\MyApp\MyApp.exe" enable=yes
remoteip=157.60.0.1,172.16.0.0/16,Local5ubnet
profile=domain
C:\> netsh advfirewall firewall add rule name="My
Application" dir=in action=allow
program="C:\MyApp\MyApp.exe" enable=yes
remoteip=157.60.0.1,172.16.0.0/16,LocalSubnet
profile=domain
C:\> netsh advfirewall firewall add rule name="My
Application" dir=in action=allow
program="C:\MyApp\MyApp.exe" enable=yes
remoteip=157.60.0.1,172.16.0.0/16,Local5ubnet
profile=private
C:\> netsh advfirewall firewall delete rule
name=rule name program="C:\MyApp\MyApp.exe"
C:\> netsh advfirewall firewall delete rule
name=rule name protocol=udp localport=500
C:\> netsh advfirewall firewall set rule
group=" remote desktop" new enable=Yes profile=domain
C:\> netsh advfirewall firewall set rule
group="remote desktop" new enable=No profile=public
```

Setup logging location:

```bash
C:\> netsh advfirewall set currentprofile logging
C:\<LOCATION>\<FILE NAME>
```

Windows firewall tog location and settings:

```bash
C:\>
more %systemroot%\system32\LogFiles\Firewall\pfirewa
ll. log
C:\> netsh advfirewall set allprofile logging
maxfilesize 4096
C:\> netsh advfirewall set allprofile logging
droppedconnections enable
C:\> netsh advfirewall set allprofile logging
allowedconnections enable
```

Display firewall logs:

```bash
PS C:\> Get-Content
$env:systemroot\system32\LogFiles\Firewall\pfirewall.log
```
