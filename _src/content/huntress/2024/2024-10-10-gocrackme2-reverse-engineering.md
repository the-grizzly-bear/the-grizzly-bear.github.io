# 2024-10-10 GoCrackMe2 (Reverse Engineering)

*[image unavailable]*

*[image unavailable]*

```python
flag{f75087857fc4d23241dc09666f390751}
```

Trying to analyze how the program outputs based off the text. Seem to get the same values in different spots.

*[image unavailable]*

flag{57fc4d2324

*[image unavailable]*

flag{f75087857fc4d2324

*[image unavailable]*

flag{f750878

*[image unavailable]*

*[image unavailable]*

flag{f75087857fc4d2324f390751}, note this is not correct

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

```powershell
00487f29      var_218 = zmm15
00487f2f      int128_t var_200 = zmm15
00487f40      __builtin_memcpy(dest: &var_218, src: "\x00\x00\x00\x00\x00\x00\x59\x40\x00\x00\x00\x00\x00\x00\x3e\x40\x00\x00\x00\x00\x00\xe0\x52\x40\x95\x64\x79\xe1\x7f\xfd\xa5\x3d\x00\x00\x00\x00\x00\x00\xd0\x3f", n: 0x28)
00487faa      int128_t var_d8
00487faa      sub_4660d4(&var_d8, zmm15)
00487fb3      int64_t var_b0
00487fb3      __builtin_memcpy(dest: &var_b0, src: "\x0a\x00\x00\x00\x00\x00\x00\x00\x0a\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00", n: 0x18)
00487fd0      int64_t* var_b8 = &var_242
00487fe4      int64_t var_90 = 5
00487ff0      int64_t var_88 = 5
00488001      int32_t* var_98 = &var_247
00488009      int64_t var_80 = 0
00488015      int64_t var_70
00488015      __builtin_memcpy(dest: &var_70, src: "\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00", n: 0x18)
00488032      int64_t* var_78 = &var_24f
00488046      int64_t var_50
00488046      __builtin_memcpy(dest: &var_50, src: "\x07\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00", n: 0x18)
00488063      int32_t* var_58 = &var_256
00488077      int64_t var_30
00488077      __builtin_memcpy(dest: &var_30, src: "\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00", n: 0x18)
00488094      int64_t* var_38 = &var_25e
```

*[image unavailable]*

*[image unavailable]*

[https://www.trellix.com/blogs/research/feeding-gophers-to-ghidra/](https://www.trellix.com/blogs/research/feeding-gophers-to-ghidra/)

Clearing up obfuscated Go functions.

[https://github.com/advanced-threat-research/GhidraScripts?tab=readme-ov-file](https://github.com/advanced-threat-research/GhidraScripts?tab=readme-ov-file)

*[image unavailable]*

Building a script to reverse, xor, and shift for the strings from this function. Output was not solid flag, and we remember the input and sections seemed random, but thye were consistient.

*[image unavailable]*

```java
encrypted_bytes = [
    0x58, 0x5a,
    0x0b, 0x0e, 0x59, 0x09, 0x5f, 0x5e, 0x5f, 0x59,
    0xb,
    0x01, 0x0c, 0x0a, 0x16,
    0x0b, 0x5e, 0x54, 0x5d, 0x5a, 0x58, 0x5c, 0x10,
    #0x10, 0x5c, 0x58, 0x5a, 0x5d, 0x54, 0x5e, 0x0b,
    0xb,
    0x5a, 0x58,
    0x5d, 0x55, 0x5a, 0x55,
    0x5c, 0x09, 0x0e, 0x5d, 0x54, 0x5b, 0x5b, 0x5b
]

decrypted_bytes = [b ^ 0x6d for b in encrypted_bytes]

#print("Decrypted chunks:")
for i in range(0, len(decrypted_bytes), 8):
    print("".join(chr(b) for b in decrypted_bytes[i:i+8]))

flag = ''.join(chr(b) for b in decrypted_bytes)
print("Non-shifted flag:", flag)

shifted_flag = flag[10:] + flag[:10]

print("Shifted flag:", shifted_flag)
```

Breaking the flag down into sections

*[image unavailable]*

Substituting in the last two pieces

*[image unavailable]*
