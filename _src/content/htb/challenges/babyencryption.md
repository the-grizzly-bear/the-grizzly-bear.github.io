# BabyEncryption (Crypto Challenge)

*[image unavailable]*
*[image unavailable]*

```python
#import string
#from secret import MSG
'''
def encryption(msg):
    ct = []
    for char in msg:
        ct.append((123 * char +18) % 256)
    return bytes(ct)

ct = encryption(MSG)
f = open('./msg.enc','w')
f.write(ct.hex())
f.close()
'''
def decrypt(msg):
    dt = []
    for byte in msg:
        for char in range(256):
            encrypted_char = ((123 * char + 18) % 256)
            if encrypted_char == byte:
                dt.append(chr(char))
    return ''.join(dt)
ct = open('./msg.enc', 'r')
ctBytes = bytes.fromhex(ct.read())
print(decrypt(ctBytes))
```

```bash
Th3 nucl34r w1ll 4rr1v3 0n fr1d4y.

HTB{l00k_47_y0u_r3v3rs1ng_3qu4710n5_c0ngr475}
```
