# ACTIVE DIRECTORY (AD) - GROUP POLICY OBJECT (GPO)

Get and force new policies:

```bash
C:\> gpupdate /force
C:\> gpupdate /sync
```

Audit Success and Failure for user Bob:

```bash
C:\> auditpol /set /user:bob /category:"DetailedTracking" /include /success:enable /failure:enable
```

Create an Organization Unit to move suspected or infected users and machines:

```bash
(:\> dsadd OU <QUARANTINE BAD OU>
```

Move an active directory user object into NEW GROUP:

```bash
PS C:\> Move-ADObject 'CN=<USER NAME>,CN=<OLD USER GROUP>,DC=<OLD DOMAIN>,DC=<OLD EXTENSION>' TargetPath 'OU=<NEW USER GROUP>,DC=<OLD DOMAIN>,DC=<OLD EXTENSION>'
```

Alt Option:

```bash
C:\> dsmove "CN=<USER NAME>,OU=<OLD USER OU>,DC=<OLD DOMAIN>,DC=<OLD EXTENSION>" -newparent OU=<NEW USER GROUP>,DC=<OLD DOMAIN>,DC=<OLD EXTENSION>
```
