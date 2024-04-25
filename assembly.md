---
aliases:
  - assembly code
---

## glossary
| assembly code | meaning |
| ---- | ---- |
| MV | move/replace |
| JNZ | jump if **not** zero |
| JZ | Jump if zero |
| TEST | Sets the zero flag (ZF) when the result of AND-ing the two operands is zero |
| EAX, EBX, ECX, EDX | general purpose registers |
| ESP | Stack pointer register |
| EBP | Base pointer |
| EIP | Instruction pointer |
| JL | jump on less than |
| JB | jump if bigger than |
| REPNE.SCASB | Repeats until **ecx = 0** or **ZF = 1**. |
| ZF | Zero flag |
| RET | pops the return address off the stack and returns control to that location |
| CMP | compare two operands |
## Components
- instructions: [[CPU]] instructions
- directives: commands to the assembler to produce a specific piece of data, or to place something in a particular section
- labels: symbolic names that can be used to refer to instructions (see above) or data in the program. Once the program is assembled and linked (see [[CYM070 week 02#Binary compilation process]], all symbolic names are replaced by addresses)
- comments: human-readable strings for documenting what your assembly program does
### instructions
- can be from 1 to 15 [[byte|bytes]]
	- hang on, so that means they need between 8 and 120 bits?
- they can start at any memory address
- an [[x86]] instruction consists of optional prefixes, an opcode (see [[#Opcode]]), and operands. Operands are the data that the instruction will operate on 
- operands comprise:
	- an addressing mode (0-1 bytes), 
	- a scale/index/base (SIB) byte, 
	- a displacement (up to 4 bytes)
	- and 'immediate' (up to 4 bytes)
- operands are optional - for example, `RET` does not have any operands
## AT&T vs Intel
- because why wouldn't there be differences
- AT&T syntax prefixes every single register name with the % symbol, and every constant with a $ symbol
- it reads `source, destination`
- the size of the operand (`AND, MOV` etc) is explicitly stated: `move _n_` where _n_ is either `b` for [[byte]], `w` for word (16 bits), `l` for long (32 [[bit|bits]], or 4 [[byte|bytes]])
- intel doesn't bother with the percent and dollar signs
- or the specific size of the operand
- it also reads `destination, source`

## Opcode

^9a89df

- in x86 architecture, they're between 1 and 3 bytes long
- these are generally turned into mnemonics (see table above), so that we don't need to remember (for example) that `0x90` is the opcode for `NOP` (no-op)
	- note that this is a single-byte instruction. The largest hex number that fits in a single byte is `FF`
	- though if an opcode can be up to three bytes long, that means there is a universe of 
- `0x00` to `0x05` are adding instructions
	- note that these are [[hexadecimal|hex]] codes
### Operands
- memory operands specify a memory address from where the CPU should fetch one or more bytes
- x86 architecture only allows one memory operand per instruction. the upshot of this is that you cannot move data from one memory location to another in a single instruction
- immediates are constant integer operands hard-coded into the instruction
	- on x86, immediates are encoded in [[endian#little-endian]] format
- signed integers are encoded using [[two's complement]] notation