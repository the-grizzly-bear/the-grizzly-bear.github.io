# HASHING

File Checksum Integrity Verifier (FCIV):<br>Ref. [http://support2.microsoft.com/kb/841290](http://support2.microsoft.com/kb/841290)<br>Hash a file:

```bash
C:\> fciv.exe <FILE TO HASH>
```

Hash all files on C:\\ into a database file:<br>

```bash
C:\> fciv.exe c:\ -r -mdS -xml <FILE NAME>.xml
```

List all hashed files:<br>

```bash
C:\> fciv.exe -list -shal -xml <FILE NAME>.xml
```

Verify previous hashes in db with file system:<br>

```bash
C:\> fciv.exe -v -shal -xml <FILE NAME>.xml
```

Note: May be possible to create a master db and<br>compare to all systems from a cmd line. Fast<br>baseline and difference.<br>Ref. [https://technet.microsoft.com/en­](https://technet.microsoft.com/en%C2%AD)<br>us/library/dn520872.aspx

```bash
PS C:\> Get-FileHash <FILE TO HASH> | Format-List
PS C:\> Get-FileHash -algorithm md5 <FILE TO HASH>
C:\> certutil -hashfile <FILE TO HASH> SHAl
C:\> certutil -hashfile <FILE TO HASH> MD5
```
