## reading
- [[The antivirus hacker's handbook#Chapter 12 Static analysis]]
- [[Static disassembly and code analysis]]
## 4.1 [[static analysis]]
### [[binary]] disassembly techniques
These naturally require and understanding of the target architecture's instruction format and [[assembly#^9a89df|opcode]] format 
#### Recursive traversal disassembly
- *what*
- start at a specific 'landmark', such as the `main` function
- maps the code recursively, ie exhaustively trying every branch 
- as with recursive search algorithms more generally, we keep a set of previously-accessed addresses, so that we don't end up in an infinite loop
#### Linear sweeping
- processing code [[byte]]-by-byte
- can risk mistaking data for instruction, and may miss non-linear execution paths
- when a conditional jump is encountered, the condition is evaluated. If the condition is met the target address is resolved and disassembly continues from that address
- if it is not met, disassembly continues from the next instruction
- this is in the happy path case of clear code. Obfuscated code, optimised code, or loops that dynamically change their conditions may outfox this approach to disassembly
- thus linear sweep disassembly is better suited when you need a quick initial assessment, or when you're confident that the code structure is simple
- it's relatively simple to implement

## 4.2 Hands-on [[static analysis]]
- high levels of [[entropy]] are suspicious, because to get true randomness you usually need to have either [[encryption|encrypted]] or compressed the file

## 4.3 Limits of [[static analysis]]
### obfuscation and packing
- a way to preserve the program's functionality while making it harder to analyse
- such malware must have a [[virtual machine]] (maybe a [[Java Virtual Machine]]?) to decode and execute the obfuscated instructions
- for example, base 64 encoding:
	- First, you take your string and translate it to [[ASCII]], which uses a [[byte]] to represent a letter. So "One" becomes
		- upper-case 'o' -> 79d -> `0x4f` -> `01001111`
		- lower-case 'n' -> 156d -> `0x6e` -> `01101110`
		- lower-case 'e' -> 145d -> `0x65` -> `01100101
	- if those binary numbers are laid end to end, you get 24 [[bit|bits]], or three bytes
	- Base 64 can get 4 characters out of three bytes
	- So then we can map:
		- `0100011` -> 19d -> T
		- `110110` -> 54d -> 2
		- `111001` -> 57d -> 5
		- `100101` -> 37d -> l
	- Thus 'One' is mapped to 'T25l', obfuscating its true meaning
- alternatively, bits might be [[exclusive or|XOR]]ed with a secret key
	- Same as a [[stream cipher]]!
	- and as with a stream cipher, the longer the key, the harder the encryption is to crack
- you could also put in junk bytes at locations that are inaccessible during run time but will throw off a linear sweep
### polymorphic [[malware]]!

^6e68de

- malware that changes shape 
- so, for example: if you [[exclusive or|XOR]] it to a new key, the obfuscated code looks completely different, and thereby evades malware detection
- so you could, for example, encrypt each payload you send out with a new key - and thus evade signature detection
- there's such a thing as _metamorphism_ in malware!? How!?
	- complete code rewrite??
	- code is divided into blocks, and then altered
- and _oligomorphism_?!