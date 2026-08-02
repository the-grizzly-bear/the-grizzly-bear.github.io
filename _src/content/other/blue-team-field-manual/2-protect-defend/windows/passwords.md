# PASSWORDS

Change password:

```bash
C:\> net user <USER NAME> * /domain
C:\> net user <USER NAME> <NEW PASSWORD>
```

Change password remotely:
Ref. [https://technet.microsoft.com/en­](https://technet.microsoft.com/en%C2%AD)<br>us/sysinternals/bb897543

```bash
C:\> pspasswd.exe \\<IP ADDRESS or NAME OF REMOTE
COMPUTER> -u <REMOTE USER NAME> -p <NEW PASSWORD>
```

Change password remotely:

```bash
PS C:\> pspasswd.exe \\<IP ADDRESS or NAME OF REMOTE
COMPUTER>
```
