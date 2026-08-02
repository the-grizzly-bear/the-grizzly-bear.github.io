# MICROSOFT BASELINE SECURITY ANALYZER (MBSA)

Basic scan of a target IP address:

```bash
C:\> mbsacli.exe /target <TARGET IP ADDRESS> /n
os+iis+sql+password
```

Basic scan of a target IP range:

```bash
C:\> mbsacli.exe /r <IP ADDRESS RANGE> /n
os+iis+sql+password
```

Basic scan of a target domain:

```bash
C:\> mbsacli.exe /d <TARGET DOMAIN> /n
os+iis+sql+password
```

Basic scan of a target computer names in text file:

```bash
C:\> mbsacli.exe /listfile <LISTNAME OF COMPUTER
NAMES>.txt /n os+iis+sql+password
```
