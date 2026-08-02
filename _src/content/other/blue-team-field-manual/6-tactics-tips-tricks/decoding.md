# DECODING

## HEX CONVERSION

```bash
C:\> set /a 1+2
3
C:\> set /a 3*(9/4)
6
C:\> set /a (2*5)/2
5
C:\>set /a "32>>3"
4
```

Decode Base64 text in a file:

```bash
C:\> certutil -decode <BASE64 ENCODED FILE NAME> <DECODED FILE NAME>
```

Decode XOR and search for http:
Ref, [https://blog.didierstevens.com/programs/xorsearch/](https://blog.didierstevens.com/programs/xorsearch/)

```bash
C:\> xorsearch,exe -i -s <INPUT FILE NAME> http
```

Convert from hex to decimal in Linux:

```bash
# echo u0xff"|wcalc -d
= 255
```

Convert from decimal to hex in Linux:

```bash
$ echo u25s"1wcalc -h
= 0xff
```

Decode HTML Strings:

```bash
PS C:\> Add-Type -AssemblyName System.Web
PS C:\> [System.Uri] ::UnescapeDataString("HTTP%3a%2f%2fHello%20World.com")
HTTP://Hello World.com
```
