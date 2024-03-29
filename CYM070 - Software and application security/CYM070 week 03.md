---
description: "Week 3: assembly, infection, behaviour"
---

## Reading
- [[Malware, rootkits and botnets#Chapter 7 Infection vectors]]
- [[Learning malware analysis]]

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
- we will not be programming in [[assembly]]
	- thanks be!
- let's start with some C (sigh)
```C
# include <stdio.h>

int main(int argc, char *argv[]) {
  printf("Hello, world!\n");
  return 0;
}
```
- for those following along at home, this functions returns an integer (specifically, 0) after printing out "Hello, world!" followed by a newline character
- `argc` is a parameter - an integer detailing the number of arguments to the function
- `argv` is an array of pointers to arrays of character (char) objects
- Let's see how it looks in assembly! Bet it's simple!!
```assembly
	.file "hello.c"
	.intel_syntax noprefix
	.section .rodata
.LC0:
	.string "Hello, world!"
	.text
	.global main
	.type main, @function
main
	push rbp
	mov rbp, rsp
	sub rsp, 16
	mov DWORD PTR [rbp-4], edi
	mov QWORD PTR [rbp-16], rsi
	mov edi, OFFSET FLAT:.LC0
	call puts
	mov eax, 0
	leave
	ret
```
A few notes:
- `mov edi, OFFSET FLAT:.LC0` moves the address of the string in `.LC0` to `edi`
- `puts` prints the string pointed to by the `edi` followed by a new line
- `mov eax, 0` sets the value of `eax` to 0
- leave undoes the setup (so the prologue?)
- and finally we return (`ret`) whatever's in `eax` - here 0

## 3.2: [[malware]] infection mechanisms
- see [[virus#File infectors]] for much of this
- there's also rootkits for the [[kernel]], which give the malware root privileges
- similarly, [[hypervisor]] rootkits are a nasty way of crossing virtual machines
- of course there's [[stack#overflow]]
- and web vulnerabilities!
## 3.2: [[malware]] functionalities
- droppers are self-deleting code that often do nothing more than reach out to another system, usually via the [[Internet]], to download further malware. You can't simply look at the APIs it uses, either - because 'speak to the Internet', 'open a file', 'write to a file' is basically the entire purpose of MS Word
- [[keylogger|keyloggers]] gonna log them keys
- [[Command and Control|C2]]