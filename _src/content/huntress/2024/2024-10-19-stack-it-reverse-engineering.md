# 2024-10-19 Stack It (Reverse Engineering)

*[image unavailable]*

*[image unavailable]*

**Load and run the binary** in GDB.
**Set a breakpoint** at the entry point using `b *0x8049000`.
**Step through** the program using `stepi` to watch the execution.
We can see the flag{ get constructed

*[image unavailable]*

The program begins by constructing `"flag{"` and then proceeds with an XOR operation between two strings stored in `esi` and `edi`
The results of the XOR are stored starting at memory address `0x804a055`.
Continue stepping through using `stepi 5` to speed up the process.
**Check memory** at `0x804a055` to see the flag being built by using `x/s 0x804a055`.

*[image unavailable]*

We stepped through the program this way to:
**Understand the flag-building process**: The binary was incrementally constructing the flag using XOR operations between values in `esi` and `edi`.
**Observe the exact memory writes**: By stepping through each instruction, we could watch how the program placed each XOR result into memory, allowing us to confirm the flag was being built correctly.
**Ensure no missed steps**: Stepping through ensured we captured every byte written, starting with `"flag{"` and completing the flag with the XORed results.
**Reveal hidden computations**: The XOR operation was crucial, and stepping through allowed us to observe how it manipulated the data to generate the full flag.

```python
flag{b4234f4bba4685dc84d6ee9a48e9c106}
```
