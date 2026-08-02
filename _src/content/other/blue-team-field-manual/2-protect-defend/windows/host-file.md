# HOST FILE

Flush DNS of malicious domain/IP:

```bash
C:\> ipconfig /flushdns
```

Flush NetBios cache of host/IP:

```bash
C:\> nbtstat -R
```

Add new malicious domain to hosts file, and route to<br>localhost:

```bash
C:\> echo 127.0.0.1 <MALICIOUS DOMAIN> >>
C:\Windows\System32\drivers\etc\hosts

```

Check if hosts file is working, by sending ping to<br>127.0.0.1:

```bash
C:\> ping <MALICIOUS DOMAIN> -n 1
```
