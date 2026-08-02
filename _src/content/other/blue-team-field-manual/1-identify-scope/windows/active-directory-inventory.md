# ACTIVE DIRECTORY INVENTORY

List all OUs:

```bash
C:\> dsquery ou DC=<DOMAIN>,DC=<DOMAIN EXTENSION>
```

List of workstations in the domain:

```bash
C:\> netdom query WORKSTATION
```

List of servers in the domain:

```bash
C:\> netdom query SERVER
```

List of domain controllers:

```bash
C:\> netdom query DC
```

List of organizational units under which the<br>specified user can create a machine object:

```bash
C:\> netdom query OU
```

List of primary domain controller:

```bash
C:\> netdom query PDC
```

List the domain trusts:

```bash
C:\> netdom query TRUST
```

Query the domain for the current list of FSMO owners

```bash
C:\> netdom query FSMO
```

List all computers from Active Directory:

```bash
C:\> dsquery COMPUTER "OU=servers,DC=<DOMAIN
NAME>,DC=<DOMAIN EXTENSION>" -o rdn -limit 0 >
C:\machines.txt
```

List user accounts inactive longer than 3 weeks:

```bash
C:\> dsquery user domainroot -inactive 3
```

Find anything (or user) created on date in UTC using<br>timestamp format [YYYYMMDDHHMMSS.sZ](http://yyyymmddhhmmss.sz/):

```bash
C:\> dsquery * -filter
"(whenCreated>=20101022083730,0Z)"
```

```bash
C:\> dsquery * -filter
"((whenCreated>=20101022083730.0Z)&(objectClass=user
) ) II
```

Alt option:

```bash
C:\> ldifde -d ou=<OU NAME>,dC=<DOMAIN
NAME>,dc=<DOMAIN EXTENSION> -l whencreated,
whenchanged -p onelevel -r "(ObjectCategory=user)" f <OUTPUT FILENAME>
```

The last logon timestamp format in UTC:<br>YYYYMMDDHHMMSS
Alt option:

```bash
C:\> dsquery * dc=<DOMAIN NAME>,dc=<DOMAIN
EXTENSION> -filter "(&(objectCategory=Person)
(objectClass=User)(whenCreated>=20151001000000.0Z))"
```

Alt option:

```bash
C:\> adfind -csv -b dc=<DOMAIN NAME>,dc=<DOMAIN
EXTENSION> -f "(&(objectCategory=Person)
(objectClass=User)(whenCreated>=20151001000000.0Z))"
```

Using PowerShell, dump new Active Directory accounts<br>in last 90 Days:

```bash
PS C:\> import-module activedirectory
PS C:\> Get-QADUser -CreatedAfter (Get­
Date).AddDays(-90)
PS C:\> Get-ADUser -Filter * -Properties whenCreated
| Where-Object {$_.whenCreated -ge ((Get­
Date).AddDays(-90)).Date}
```
