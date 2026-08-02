# NETBIOS

Basic nbtstat scan:

```bash
C:\> nbtstat -A <IP ADDRESS>
```

Cached NetBIOS info on localhost:

```bash
C:\> nbtstat -c
```

Script loop scan:

```bash
C:\> for /L %I in (1,1,254) do nbstat -An 192.168.1.%I
```
