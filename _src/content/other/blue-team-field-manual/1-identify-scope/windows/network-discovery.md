# NETWORK DISCOVERY

Basic network discovery:

```bash
C:\> net view /all
C:\> net view \\<HOST NAME>
```

Basic ping scan and write output to file:

```bash
C:\> for /L %I in (1,1,254) do ping -w 30 -n 1
192.168.l.%I | find "Reply" >> <OUTPUT FILE
NAME>.txt
```
