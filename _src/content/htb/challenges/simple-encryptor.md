# Simple Encryptor (rev challenge)

*[image unavailable]*

```text
┌──(kali㉿kali)-[/mnt/tmp/HTB]
└─$ python decode.py  
HTB{vRy_s1MplE_F1LE3nCryp0r}
                                                                                                       
┌──(kali㉿kali)-[/mnt/tmp/HTB]
└─$ cat decode.py    
def get_rand_sequence(seed, num_rands):
    MOD = 2147483647
    STATE_SIZE = 344 + num_rands
    r = [0] * STATE_SIZE
    r[0] = seed
    for i in range(1, 31):
        r[i] = (16807 * r[i-1]) % MOD
    for i in range(31, 34):
        r[i] = r[i-31]
    for i in range(34, STATE_SIZE):
        r[i] = (r[i-31] + r[i-3]) & 0xffffffff
    rands = []
    for i in range(344, 344 + num_rands):
        rand_val = (r[i] >> 1) & 0x7fffffff
        rands.append(rand_val)
    return rands

seed = 1655780698
rands = get_rand_sequence(seed, 56)
enc_hex = "00f53e12c0bd8d16f0fd7599faef399a4b9621a14316237165fb274b"
enc_bytes = [int(enc_hex[j:j+2],16) for j in range(0,len(enc_hex),2)]
plain = []
k = 0
for b in enc_bytes:
    rand_xor = rands[k] & 0xff
    k += 1
    rand_shift = rands[k] & 7
    k += 1
    rotated = ((b >> rand_shift) | (b << (8 - rand_shift))) & 0xff
    decrypted = rotated ^ rand_xor
    plain.append(chr(decrypted))
flag = ''.join(plain)
print(flag)

```
