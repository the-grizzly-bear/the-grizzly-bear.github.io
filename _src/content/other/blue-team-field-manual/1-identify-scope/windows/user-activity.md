# USER ACTIVITY

Ref. [https://technet.microsoft.com/en­](https://technet.microsoft.com/en%C2%AD)us/sysinternals/psloggedon.aspx
<br>Get users logged on:

```bash
C:\> psloggedon \\computername
```

Script loop scan:

```bash
C:\> for /L %i in (1,1,254) do psloggedon
\\192.168.1.%i >> C:\users_output.txt
```
