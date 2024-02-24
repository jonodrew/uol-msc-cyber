## Von Neumann architecture

![[Von_Neumann_Architecture.svg]] [Attribution](By Kapooht - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=25789639)

## Registers
Registers are small, fast, pieces of memory. They are often measured by the number of [[bit|bits]] they can hold - eg 8-bit, 16-bit, etc. Remember that an 8-bit register can hold a [[binary]] number up to 255. 

Register names are a bit of a pain in the ass.

For example, the first 32 bits of the 64-bit register `rax` is the 32-bit register `eax`, which in turns includes the 16-bit register `ax`, which itself is divided into two 8-bit registers: `ah` and `al`

### (R)IP (instruction pointer)

^53dada

See also [[assembly#instructions]] for what an instruction actually is. This register holds the address of the next instruction to be executed, and it automatically set by the CPU. In a 64-bit x86 architecture it's possible to read this value; not so in 34-bit

### (E|R)SP (stack pointer)

^f78924

In [[x86]] architectures the stack pointer is counted as an integer register. However, there are only a few operations that can actually be conducted on it. It contains the address of the last element added to the stack or the first available address on the stack - ie, the top of the stack

### FLAGS register
Here we keep flags which indicate the status of the CPU. For example, this is where the zero flag (`ZF`) (bit `0x0040`) lives. There's also the resume flag (`RF`), the sign flag (`SF`) - which is interpreted as negative-if-set, and the overflow flag (`OF`).

[See wikipedia page](https://en.wikipedia.org/wiki/FLAGS_register) for further detail

### Segment registers

### Control registers
`CR0` to `CR10`

### Debug registers
`DR0` to `DR7`

## [[stack|The stack]]