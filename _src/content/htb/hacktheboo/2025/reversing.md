# Reversing

## Rusted Oracle

```text
An ancient machine, a relic from a forgotten civilization, could be the key to defeating the Hollow King. However, the gears have ground almost to a halt. Can you restore the decrepit mechanism?
```

```text
1. Binary Analysis: The binary is a 64-bit ELF executable that asks for a specific name as input
  2. Correct Input: The name "Corwin Vell" triggers the decoding sequence
  3. Decoding Algorithm: The binary decodes an encrypted flag stored at address 0x4050 using this
  sequence:
    - XOR with 0x524E
    - Rotate right by 1 bit
    - XOR with 0x5648
    - Rotate left by 7 bits
    - Shift right by 8 bits
    - Extract the lowest byte
  4. Challenge Name: The flag text "sk1pP1nG-C4ll$!!1!" is a hint - instead of running the slow
  binary (which uses rand() and sleep() to deliberately slow down execution), the solution was to
  skip those calls and directly decode the encrypted data by reverse engineering the algorithm.



  The encoded flag before decoding consists of 23 64-bit values stored at address 0x4050 in the
  binary's data section:

  0xfffe, 0xff8e, 0xffd6, 0xff32, 0xff12, 0xff72,
  0xfe1a, 0xff1e, 0xff9e, 0xfe1a, 0xff66, 0xffc2,
  0xfe6a, 0xffd2, 0xfe0e, 0xff6e, 0xff6e, 0xfe4e,
  0xfe5a, 0xfe5a, 0xfe1a, 0xfe5a, 0xff2a
```

```python
# Helper functions for 64-bit rotation
def ror(n, bits, width=64):
    """Rotate right a 64-bit integer"""
    mask = (1 << width) - 1
    return ((n >> bits) | (n << (width - bits))) & mask

def rol(n, bits, width=64):
    """Rotate left a 64-bit integer"""
    mask = (1 << width) - 1
    return ((n << bits) | (n >> (width - bits))) & mask

#
# WARNING: These are 16-bit values. The C code expects 64-bit values.
# This list will produce an incorrect flag.
# You must find the 23 *64-bit* values from the binary.
#
enc = [
    0xfffe, 0xff8e, 0xffd6, 0xff32, 0xff12, 0xff72, 0xfe1a, 0xff1e, 0xff9e, 0xfe1a, 
    0xff66, 0xffc2, 0xfe6a, 0xffd2, 0xfe0e, 0xff6e, 0xff6e, 0xfe4e, 0xfe5a, 0xfe5a, 
    0xfe1a, 0xfe5a, 0xff2a
]

flag_bytes = []

# Constants from the C code
XOR_KEY_1 = 21070   # 0x524E
XOR_KEY_2 = 22088   # 0x5648

# Re-implement the decryption loop (using 64-bit operations as in the C code)
for val in enc:
    val = val ^ XOR_KEY_1
    val = ror(val, 1)
    val = val ^ XOR_KEY_2
    val = rol(val, 7)
    val = val >> 8
    
    # Truncate to the lowest byte
    flag_bytes.append(val & 0xFF)

# Decode and print the flag
try:
    flag = bytes(flag_bytes).decode('ascii')
    print(f"On a rusted plate, faint letters reveal themselves: {flag}")
except UnicodeDecodeError:
    print(f"Could not decode bytes: {flag_bytes}")
```

```text
output:
On a rusted plate, faint letters reveal themselves: HTB{sk1pP1nG-C4ll$!!1!}
```

```c
int64_t (* const)() _init()
{
    if (!__gmon_start__)
        return __gmon_start__;
    
    return __gmon_start__();
}

int64_t sub_401020()
{
    int64_t var_8 = data_403ff0;
    /* jump -> data_403ff8 */
}

int32_t printf(char const* format, ...)
{
    /* tailcall */
    return printf(format);
}

int64_t sub_401036()
{
    int64_t var_8 = 0;
    /* tailcall */
    return sub_401020();
}

int64_t memset(void* arg1, int32_t arg2, uint64_t arg3)
{
    /* tailcall */
    return memset(arg1, arg2, arg3);
}

int64_t sub_401046()
{
    int64_t var_8 = 1;
    /* tailcall */
    return sub_401020();
}

ssize_t read(int32_t fd, void* buf, uint64_t nbytes)
{
    /* tailcall */
    return read(fd, buf, nbytes);
}

int64_t sub_401056()
{
    int64_t var_8 = 2;
    /* tailcall */
    return sub_401020();
}

int32_t strcmp(char const* arg1, char const* arg2)
{
    /* tailcall */
    return strcmp(arg1, arg2);
}

int64_t sub_401066()
{
    int64_t var_8 = 3;
    /* tailcall */
    return sub_401020();
}

int32_t fflush(FILE* fp)
{
    /* tailcall */
    return fflush(fp);
}

int64_t sub_401076()
{
    int64_t var_8 = 4;
    /* tailcall */
    return sub_401020();
}

void perror(char const* s)
{
    /* tailcall */
    return perror(s);
}

int64_t sub_401086()
{
    int64_t var_8 = 5;
    /* tailcall */
    return sub_401020();
}

uint32_t sleep(uint32_t seconds)
{
    /* tailcall */
    return sleep(seconds);
}

int64_t sub_401096()
{
    int64_t var_8 = 6;
    /* tailcall */
    return sub_401020();
}

int32_t rand()
{
    /* tailcall */
    return rand();
}

int64_t sub_4010a6()
{
    int64_t var_8 = 7;
    /* tailcall */
    return sub_401020();
}

void __cxa_finalize(void* d)
{
    /* tailcall */
    return __cxa_finalize(d);
}

void _start(int64_t arg1, int64_t arg2, void (* arg3)()) __noreturn
{
    int64_t stack_end_1;
    int64_t stack_end = stack_end_1;
    void ubp_av;
    __libc_start_main(main, __return_addr, &ubp_av, nullptr, nullptr, arg3, &stack_end);
    /* no return */
}

char* deregister_tm_clones()
{
    return &__TMC_END__;
}

int64_t (* const)() register_tm_clones()
{
    return nullptr;
}

void __do_global_dtors_aux()
{
    if (__TMC_END__)
        return;
    
    if (__cxa_finalize)
        __cxa_finalize(__dso_handle);
    
    deregister_tm_clones();
    __TMC_END__ = 1;
}

int64_t (* const)() frame_dummy()
{
    /* tailcall */
    return register_tm_clones();
}

int64_t machine_decoding_sequence()
{
    char var_28[0x20];
    memset(&var_28, 0, 0x18);
    sleep(rand());
    int32_t var_2c = 0;
    
    while (var_2c < 0x17)
    {
        int64_t rcx_1 = var_2c;
        *(&enc + (rcx_1 << 3)) ^= 0x524e;
        *(&enc + (var_2c << 3)) = RORQ(*(&enc + (var_2c << 3)), 1);
        int64_t rcx_4 = var_2c;
        *(&enc + (rcx_4 << 3)) ^= 0x5648;
        *(&enc + (var_2c << 3)) = ROLQ(*(&enc + (var_2c << 3)), 7);
        int64_t rcx_7 = var_2c;
        *(&enc + (rcx_7 << 3)) u>>= 8;
        int64_t rcx_8;
        rcx_8 = *(&enc + (var_2c << 3));
        var_28[var_2c] = rcx_8;
        var_2c += 1;
    }
    
    int64_t rax_6;
    rax_6 = 0;
    return printf("On a rusted plate, faint letters reveal themselves: %s\n", &var_28);
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    int32_t var_c = 0;
    char buf[0x4c];
    memset(&buf, 0, 0x40);
    int64_t rax;
    rax = 0;
    printf("A forgotten machine still ticks beneath the stones.\n");
    int64_t rax_1;
    rax_1 = 0;
    printf("Its gears grind against centuries of rust.\n");
    int64_t rax_2;
    rax_2 = 0;
    printf("\n[ a stranger approaches, and the machine asks for their name ]\n");
    int64_t rax_3;
    rax_3 = 0;
    printf("> ");
    fflush(*stdout);
    int32_t rax_4 = read(0, &buf, 0x3f);
    
    if (rax_4 < 0)
    {
        perror("read");
        return 1;
    }
    
    if (buf[rax_4 - 1] == 0xa)
        buf[rax_4 - 1] = 0;
    
    int32_t rax_12;
    
    if (strcmp(&buf, "Corwin Vell"))
    {
        rax_12 = 0;
        printf("[ the machine falls silent ]\n");
    }
    else
    {
        rax_12 = 0;
        printf("[ the gears begin to turn... slowly... ]\n");
        fflush(*stdout);
        machine_decoding_sequence();
    }
    return 0;
}

int64_t _fini() __pure
{
    return;
}
```

```text
HTB{sk1pP1nG-C4ll$!!1!}
```

## Digital Alchemy

```text
Morvidus the alchemist claims to have perfected the art of digital alchemy. Being paranoid, he secured his incantation with a complex algorithm, but left the code rushed and broken. Fix his amateur mistakes and claim the digital gold for yourself!
```

```c
int64_t (* const)() _init()
{
    if (!__gmon_start__)
        return __gmon_start__;
    
    return __gmon_start__();
}

int64_t sub_401020()
{
    int64_t var_8 = data_403ff0;
    /* jump -> data_403ff8 */
}

void free(void* mem)
{
    /* tailcall */
    return free(mem);
}

int64_t sub_401036()
{
    int64_t var_8 = 0;
    /* tailcall */
    return sub_401020();
}

int32_t strncmp(char const* arg1, char const* arg2, uint64_t arg3)
{
    /* tailcall */
    return strncmp(arg1, arg2, arg3);
}

int64_t sub_401046()
{
    int64_t var_8 = 1;
    /* tailcall */
    return sub_401020();
}

int32_t puts(char const* str)
{
    /* tailcall */
    return puts(str);
}

int64_t sub_401056()
{
    int64_t var_8 = 2;
    /* tailcall */
    return sub_401020();
}

uint64_t fread(void* buf, uint64_t size, uint64_t count, FILE* fp)
{
    /* tailcall */
    return fread(buf, size, count, fp);
}

int64_t sub_401066()
{
    int64_t var_8 = 3;
    /* tailcall */
    return sub_401020();
}

int32_t fclose(FILE* fp)
{
    /* tailcall */
    return fclose(fp);
}

int64_t sub_401076()
{
    int64_t var_8 = 4;
    /* tailcall */
    return sub_401020();
}

uint64_t strlen(char const* arg1)
{
    /* tailcall */
    return strlen(arg1);
}

int64_t sub_401086()
{
    int64_t var_8 = 5;
    /* tailcall */
    return sub_401020();
}

int32_t printf(char const* format, ...)
{
    /* tailcall */
    return printf(format);
}

int64_t sub_401096()
{
    int64_t var_8 = 6;
    /* tailcall */
    return sub_401020();
}

int64_t memset(void* arg1, int32_t arg2, uint64_t arg3)
{
    /* tailcall */
    return memset(arg1, arg2, arg3);
}

int64_t sub_4010a6()
{
    int64_t var_8 = 7;
    /* tailcall */
    return sub_401020();
}

int32_t strcmp(char const* arg1, char const* arg2)
{
    /* tailcall */
    return strcmp(arg1, arg2);
}

int64_t sub_4010b6()
{
    int64_t var_8 = 8;
    /* tailcall */
    return sub_401020();
}

int64_t ftell(FILE* fp)
{
    /* tailcall */
    return ftell(fp);
}

int64_t sub_4010c6()
{
    int64_t var_8 = 9;
    /* tailcall */
    return sub_401020();
}

int64_t memcpy(void* arg1, void const* arg2, uint64_t arg3)
{
    /* tailcall */
    return memcpy(arg1, arg2, arg3);
}

int64_t sub_4010d6()
{
    int64_t var_8 = 0xa;
    /* tailcall */
    return sub_401020();
}

time_t time(time_t* arg1)
{
    /* tailcall */
    return time(arg1);
}

int64_t sub_4010e6()
{
    int64_t var_8 = 0xb;
    /* tailcall */
    return sub_401020();
}

int64_t malloc(uint64_t bytes)
{
    /* tailcall */
    return malloc(bytes);
}

int64_t sub_4010f6()
{
    int64_t var_8 = 0xc;
    /* tailcall */
    return sub_401020();
}

int32_t fseek(FILE* fp, int64_t offset, int32_t whence)
{
    /* tailcall */
    return fseek(fp, offset, whence);
}

int64_t sub_401106()
{
    int64_t var_8 = 0xd;
    /* tailcall */
    return sub_401020();
}

FILE* fopen(char const* filename, char const* mode)
{
    /* tailcall */
    return fopen(filename, mode);
}

int64_t sub_401116()
{
    int64_t var_8 = 0xe;
    /* tailcall */
    return sub_401020();
}

void exit(int32_t status) __noreturn
{
    /* tailcall */
    return exit(status);
}

int64_t sub_401126()
{
    int64_t var_8 = 0xf;
    /* tailcall */
    return sub_401020();
}

uint64_t fwrite(void const* buf, uint64_t size, uint64_t count, FILE* fp)
{
    /* tailcall */
    return fwrite(buf, size, count, fp);
}

int64_t sub_401136()
{
    int64_t var_8 = 0x10;
    /* tailcall */
    return sub_401020();
}

void __cxa_finalize(void* d)
{
    /* tailcall */
    return __cxa_finalize(d);
}

void _start(int64_t arg1, int64_t arg2, void (* arg3)()) __noreturn
{
    int64_t stack_end_1;
    int64_t stack_end = stack_end_1;
    void ubp_av;
    __libc_start_main(main, __return_addr, &ubp_av, nullptr, nullptr, arg3, &stack_end);
    /* no return */
}

char* deregister_tm_clones()
{
    return &data_404098;
}

int64_t (* const)() sub_4011b0()
{
    return nullptr;
}

void _FINI_0()
{
    if (data_404098)
        return;
    
    if (__cxa_finalize)
        __cxa_finalize(data_404090);
    
    deregister_tm_clones();
    data_404098 = 1;
}

int64_t (* const)() _INIT_0()
{
    /* tailcall */
    return sub_4011b0();
}

int32_t main(int32_t argc, char** argv, char** envp)
{
    int32_t argc_1 = argc;
    char** argv_1 = argv;
    puts("Initializing the Athanor...");
    time_t rax = time(nullptr);
    void* const var_30 = "USMWO[]\iN[QWRYdqXle[i_bm^aoc";
    FILE* fp = fopen("lead.txt", "rb");
    fseek(fp, 0, 2);
    int32_t rax_3 = ftell(fp);
    fseek(fp, 0, 0);
    char* buf = malloc(rax_3);
    fread(buf, 1, rax_3, fp);
    fclose(fp);
    
    if (!strncmp(buf, "MTRLLEAD", 8))
    {
        char* var_10_1 = &buf[8];
        int32_t var_4c_1 = 0x26688d;
        int32_t var_14_1 = 0x214f;
        int32_t var_20_1 = var_10_1[3] | *var_10_1 << 0x18 | var_10_1[1] << 0x10 | var_10_1[2] << 8;
        
        if (time(nullptr) - rax > 2)
            var_14_1 = 0xdead;
        
        void* var_10_2 = &var_10_1[4];
        char var_59_1 = 0x40;
        int32_t var_18_1 = 0;
        int32_t rax_36 = strlen(var_30);
        char var_98[0x1e];
        int32_t i;
        
        for (i = 0; i < rax_36; i += 1)
        {
            uint32_t rdx_7 = var_59_1 ^ (var_59_1 + i + *var_10_2);
            uint32_t rax_48;
            rax_48 = (rdx_7 * 3) >> 8;
            uint32_t rax_50;
            rax_50 = (rdx_7 - rax_48) >> 1;
            uint32_t rax_51;
            rax_51 = (rax_50 + rax_48) >> 6;
            var_98[i] = rdx_7 - ((rax_51 << 7) - rax_51) + 1;
            var_18_1 += *var_10_2;
            var_10_2 += 1;
        }
        
        if (time(nullptr) - rax > 2)
            var_18_1 = 0xdead;
        
        var_98[i] = 0;
        
        if (strcmp(&var_98, var_30))
        {
            printf("Incantation mismatch. The words fade into silence...");
            free(buf);
            exit(1);
            /* no return */
        }
        
        char* buf_1 = malloc(0x28);
        int32_t var_6c_1 = 8;
        memset(buf_1, 0, 8);
        memcpy(buf_1, var_10_2, var_6c_1 - 1);
        int32_t rax_75 = strlen(buf_1);
        
        for (int32_t i_1 = 0; i_1 < rax_75; i_1 += 1)
        {
            var_20_1 = COMBINE(0, var_18_1 + var_14_1 * var_20_1) % var_4c_1;
            buf_1[i_1] ^= var_20_1 & 0xf;
        }
        
        FILE* fp_1 = fopen("gold.txt", "wb");
        fwrite(buf_1, 1, rax_75, fp_1);
        fclose(fp_1);
        puts("The Athanor glows brightly, revealing a secret...");
        free(buf);
        free(buf_1);
    }
    
    return 0;
}

int64_t _fini() __pure
{
    return;
}
```
