# WINDOWS

Honey Ports Windows:
Ref. [http://securityweekly.com/wp­](http://securityweekly.com/wp%C2%AD)<br>content/uploads/2013/06/howtogetabetterpentest.pdf
Step 1: Create new TCP Firewall Block rule on<br>anything connecting on port 3333:

```bash
C:\> echo @echo off for /L %%i in (1,1,1) do @for /f
"tokens=3" %%j in ('netstat -nao A l find "'":3333A "')
do@for /f "tokens=l delims=:" %%k in ("%%j") do
netsh advfirewall firewall add rulename="HONEY TOKEN
RULE" dir=in remoteip=%%k localport=any protocol=TCP
action=block >> <BATCH FILE NAME>.bat
```

Step 2: Run Batch Script

```bash
C:\> <BATCH FILE NAME>,bat
```

Windows Honey Ports PowerShell Script:<br>Ref. [https://github.com/Pwdrkeg/honeyport/blob/master/honeyport.psl](https://github.com/Pwdrkeg/honeyport/blob/master/honeyport.psl)
Step 1: Download PowerShell Script

```bash
C:\> "%ProgramFiles%\Internet Explorer\iexplore.exe"
```

[https://github.com/Pwdrkeg/honeyport/blob/master/honeyport.psl](https://github.com/Pwdrkeg/honeyport/blob/master/honeyport.psl)
Step 2: Run PowerShell Script

```bash
C:\> honeyport.psl
```

Honey Hashes for Windows (Also for DetectingMimikatz Use) : Ref. [https://isc.sans.edu/forums/diary/Detecting+Mimikatz+Use+On+Your+Network/19311/](https://isc.sans.edu/forums/diary/Detecting+Mimikatz+Use+On+Your+Network/19311/)
Step 1: Create Fake Honey Hash. Note enter a fake password and keep command prompts open to keep password in memory

```bash
C:\> runas
/user:yourdomain.com\fakeadministratoraccount
/netonly cmd.exe
```

Step 2: Query for Remote Access Attempts

```bash
C:\> wevtutil qe System /q:"*[System
[(EventID=20274)]]" /f:text /rd:true /c:1
/r:remotecomputername
```

Step 3: Query for Failed Login Attempts

```bash
C:\> wevtutil qe Security /q:"*[System[(EventID=4624
or EventID=4625)]]" /f:text /rd:true /c:5
/r:remotecomputername
```

Step 4: (Optional) Run queries in infinite loop with 30s pause

```bash
C:\> for /L %i in (1,0,2) do (Insert Step 2) & (Insert Step 3) & timeout 30
```
