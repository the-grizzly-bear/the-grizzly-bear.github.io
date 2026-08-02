# DNS

Default location Windows 2003:

```bash
C:\> %SystemRoot%\System32\Dns
```

Default location Windows 2008:

```bash
C:\> %SystemRoot%\System32\Winevt\Logs\DNS
Server.evtx
```

Default location of enhanced DNS Windows 2012 R2:

```bash
C:\> %SystemRoot%\System32\Winevt\Logs\Microsoft­
Windows-DNSServer%4Analytical.etl
```

Ref. [https://technet.microsoft.com/en­](https://technet.microsoft.com/en%C2%AD)<br>us/library/cc940779.aspx<br>Enable DNS Logging:

```bash
C:\> DNSCmd <DNS SERVER NAME> /config /logLevel
0x8100F331
```

Set log location:

```bash
C:\> DNSCmd <DNS SERVER NAME> /config /LogFilePath
<PATH TO LOG FILE>
```

Set size of log file:

```bash
C:\> DNSCmd <DNS SERVER NAME> /config
/logfilemaxsize 0xffffffff
```
