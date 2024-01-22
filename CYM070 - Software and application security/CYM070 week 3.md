## 3.1 Crash course on [[assembly]]
- where was this last week! This was needed for [[WannaCry#Decompiling Wannacry with Ghidra]] 😭
- Ahmad reads books with footnotes 🥹
- two approaches to disassembly: linear versus flow-oriented
- consider the following instructions:

| Address | Instruction | Data |
| ---- | ---- | ---- |
| `00001000` | `MOV` | `EAX, 1` |
| `00001005` | `MOV` | `EBX, [0x200]` |
| `0000100B` | `ADD` | `EAX, EBX` |
- this is a linear structure. We initialise register `EAX` with the value 1, then load the value in memory address `0x2000` into register `EBX`. Finally we add the two registers
- Now let's consider a loop:

| Address | Instruction | Data |
| ---- | ---- | ---- |
| `00001012` | `MOV` | `ECX, 5` |
| `00001017` | `PUSH` | `EAX` |
| `00001018` | `CALL` | `0x1017` |
- here the loop starts by putting 5 into the `ECX` register
- then it pushes the value of `EAX` onto the stack
- then it calls another function, which is at address `0x1017`
- the loop checks if it's finished with this code:

| Address | Instruction | Data |
| ---- | ---- | ---- |
| `0000101D` | `DEC` | `ECX` |
| `0000101E` | `JNZ` | `0x1017` |
- it decrements the register at `ECX` (which, remember, is where the counter was first initiated)
- if the counter is not zero (JNZ, see [[assembly]]), it goes back to address `0x1017`          

### prologues and epilogues
- man we used to be so fantasy nerdy with this stuff
- the prologue is the function setting up, while the epilogue is where it clears up after itself
- the stack!
- the stack pointer, referred to as `ESP` in x86 architecture, always points to the top of the stack

| Address | Instruction | Data | Notes |
| ---- | ---- | ---- | ---- |
| `00001000` | `PUSH` | `EBP` | Push the value of the EBP register onto the stack |
| `00001001` | `MOV` | `EBP, ESP` | Move the value of ESP to the EBP register |
| `00001003` | `SUB` | `ESP, 10h` | Allocate 10 spaces for variables by subtracting it from the ESP register |
| `00001006` | `MOV` | `EAX, [EBP+8]` | Move the value at an offset of 8 from the EBP value into the EAX register |
| `00001009` | `ADD` | `EAX, [EBP+C]` | Add the value of the EAX register to the value at an offset of C from the EBP. This will become the new value of EAX |
| `0000100C` | `PUSH` | `EAX` | Put the value of EAX onto the stack |
| `0000100D` | `CALL` | `0x2000` | Call the function at address 0x2000 |
| `00001012` | `ADD` | `ESP, 10h` | Remove the space we reserved at 00001003 |
| `00001015` | `POP` | `EBP` | Pop the top of the stack into EBP (which, since we've moved 10 back up the stack above, is the same as it was previously) |
| `00001016` | `RET` |  | Return control to the calling function |
- now we turn to [[control flow graphs]]
- they're a nice way to visualise code flow, but can be vulnerable to [[obfuscation]] as well as self-mutating code
- there is such a thing as 'intermediate representation'. Consider:
```
/ C code
int x = a + b;

/ intermediate representation
x1 = load a
x2 = load b
x3 = add x1, x2
store x3 -> x

/ assembly
MOV EAX, [a]
ADD EAX, [b]
MOV [x], EAX
```
