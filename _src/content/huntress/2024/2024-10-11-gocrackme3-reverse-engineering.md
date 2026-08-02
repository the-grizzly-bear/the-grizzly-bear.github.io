# 2024-10-11 GoCrackMe3 (Reverse Engineering)

*[image unavailable]*

Well I was on the right path, just didn’t step through enough to get the final flag piece to print out, I did jump through enough to start it.

*[image unavailable]*

*[image unavailable]*

\\x09\\x01\\x08\\x12\\x1a\\x1c\\x16\\x01\\x1d\\x25\\x18\\x08\\x02\\x00\\x17\\x2d\\x18\\x1b\\x1d\\x18\\x21\\x17\\x2f\\x27\\x28\\x2c\\x03\\x2b\\x11\\x2a\\x08\\x25\\x19\\x14\\x0a\\x0b\\x2c\\x24\\x00\\x1a\\x2c\\x2e\\x07\\x02\\x18\\x15\\x0e\\x28\\x18\\x08\\x14\\x84\\xef\\x8b\\x61\\x6c\\x6c\\xb1\\xb6\\xd3\\x69\\x92\\x64\\x6f\\x38\\x27\\x74\\x81\\x1b\\x65\\xaa\\x8b\\xb2\\x52\\xe7\\xa4\\xd2\\x20\\xcf\\xe2\\x69\\x6e\\x74\\x8e\\x6e\\x67\\xb0\\x20\\x68\\x7c\\xb0\\x66\\x35\\x9f\\xd6\\xaf\\xa9\\xb3
*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

[embedded file](https://app.notion.com/p/11b6c6e16f868071aec7c26f5c2fdbb2#11c6c6e16f86807caa75c765c93df411)

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

trying output registers
*[image unavailable]*

extracting rax
*[image unavailable]*

decoding rax

*[image unavailable]*

*[image unavailable]*
```powershell
[0x004f7a00]> px 64 @ rax
- offset -   0 1  2 3  4 5  6 7  8 9  A B  C D  E F  0123456789ABCDEF
0x004f7a00  4c8d a424 00fd ffff 4d3b 6610 0f86 a307  L..$....M;f.....
0x004f7a10  0000 5548 89e5 4881 ec78 0300 000f 1f00  ..UH..H..x......
0x004f7a20  e85b 29fe ff48 0fba e03f 731a 4889 c148  .[)..H...?s.H..H
0x004f7a30  d1e0 48c1 e81f 48ba 807f b1d7 0d00 0000  ..H...H.........
[0x004f7a00]> ph 64 @ rax
[0x004f7a00]> ps 64 @ rax
L\x8d\xa4$\x00\xfd\xff\xffM;f\x10\x0f\x86\xa3\x07\x00\x00UH\x89\xe5H\x81\xecx\x03\x00\x00\x0f\x1f\x00\xe8[)\xfe\xffH\x0f\xba\xe0?s\x1aH\x89\xc1H\xd1\xe0H\xc1\xe8\x1fH\xba\x80\x7f\xb1\xd7\x0d\x00\x00\x00
[0x004f7a00]> psu 64 @ rax
L\u008d\u00a4$\u0000\u00fd\u00ff\u00ffM;f\u0010\u000f\u0086\u00a3\u0007\u0000\u0000UH\u0089\u00e5H\u0081\u00ecx\u0003\u0000\u0000\u000f\u001f\u0000\u00e8[)\u00fe\u00ffH\u000f\u00ba\u00e0?s\u001aH\u0089\u00c1H\u00d1\u00e0H\u00c1\u00e8\u001fH\u00ba\u0080\u007f\u00b1\u00d7\u000d\u0000\u0000\u0000

```

*[image unavailable]*

```python
db 0x004F7A00
#db 0x004f7a2c
db 0x004f7a74
dr rax=0x00000001 or dr al=0x01
db 0x004f7a7c
db 0x004f7cbc
wa jmp 0x004f7cbe
#db 0x004f7cc5
#db 0x004f7cd3
db 0x004f7d08
```
```python
db 0x4f7d15 #ret
```

```python
db 0x004F7A00
db 0x004f8008
db 0x004f7a2f
db 0x004f7a32
```
```python
0x004f7a2c      4889c1         mov rcx, rax
0x004f7a2f      48d1e0         shl rax, 1
0x004f7a32      48c1e81f       shr rax, 0x1f
```
```python
db 0x004F7A7C
```
```python
db 0x004F7A00
#db 0x004f7a2c
db 0x004f7a74
dr rax=0x00000001 or dr al=0x01
db 0x004f7a7c
db 0x004f7cbc
wa jmp 0x004f7cbe
#db 0x004f7cc5
#db 0x004f7cd3
db 0x004f7d08
```
```python
db 0x4f7d15 #ret
```
```python
db 0x004e5344
```

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
```python
db 0x004F7A00
db 0x004f8008
db 0x004f7a2f
db 0x004f7a32
```
```python
0x004f7a2c      4889c1         mov rcx, rax
0x004f7a2f      48d1e0         shl rax, 1
0x004f7a32      48c1e81f       shr rax, 0x1f
```
```python
db 0x004F7A7C
```
```python
db 0x004F7A00
#db 0x004f7a2c
db 0x004f7a74
dr rax=0x00000001 or dr al=0x01
db 0x004f7a7c
db 0x004f7cbc
wa jmp 0x004f7cbe
#db 0x004f7cc5
#db 0x004f7cd3
db 0x004f7d08
```
```python
db 0x4f7d15 #ret
```
```python
db 0x004e5344
```

```python
break *0x004f7a74
```
```python
set {unsigned char}0x4f7a76 = 0x90
gef➤  set {unsigned char}0x4f7a77 = 0x90
gef➤  set {unsigned char}0x4f7a78 = 0x90
gef➤  set {unsigned char}0x4f7a79 = 0x90
gef➤  set {unsigned char}0x4f7a7a = 0x90
```
```python
gef➤  set {unsigned char[5]}0x4f7a76 = "\x90\x90\x90\x90\x90"
```
```python
gef➤  x/5xb 0x4f7a76
0x4f7a76:       0x90    0x90    0x90    0x90    0x90
```
```python
" !\"#$%%&&\'\'((()))*++,,,,,------....//////0001123333333333444444444455666677777888888888889999999999::::::;;;;;;;;;;;;;;;;<<<<<<<"
```
```python
set {unsigned char[6]}0x4f7a76 = "\x90\x90\x90\x90\x90\x90”
```
```python
set {unsigned char[6]}0x4f7a76 = "\x90\x90\x90\x90\x90\x90”
```

```python
b *0x4F7D3A
```
*[image unavailable]*

```python
HackersGonnaHackHuntressGonnaHunt
```
```python
info b
```
```python
Num     Type           Disp Enb Address            What
1       breakpoint     keep y   0x00000000004f7a74
breakpoint already hit 1 time
2       breakpoint     keep y   0x00000000004f7d3a
3       breakpoint     keep y   0x00000000004f7d3a
4       breakpoint     keep n   0x00000000004f939b
5       breakpoint     keep n   0x00000000004f9423
6       breakpoint     keep n   0x00000000004f9324
7       breakpoint     keep n   0x00000000004f939b
8       breakpoint     keep n   0x00000000004f9244
9       breakpoint     keep n   0x000000000040aeb7
10      breakpoint     keep n   0x0000000000444835
```
```python
221fccaa8
```
```python
0x4f7f1b
```

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

flag\{32b2\}32b2\}
*[image unavailable]*

42024a30b
*[image unavailable]*

Other notes

1st jbe after flag\{
*[image unavailable]*

*[image unavailable]*
*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

*[image unavailable]*

next lets try to take this 0x4f9244
*[image unavailable]*

*[image unavailable]*

"flag\{42024a30b
*[image unavailable]*

*[image unavailable]*
