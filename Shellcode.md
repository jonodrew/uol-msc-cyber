- shellcode is position-independent code
- it uses no hardcoded addresses
- this is because the author doesn't know where the shellcode will be loaded
- control-flow instructions like `jmp` and `call` are position-independent, because they take offsets as arguments
- by contrast `mov` isn't always position-independent, but can be made so by using an offset - ie `mov edx, dword_157602` doesn't work whereas `mov edx, [ebp-4]` does because it's a relative distance
## whereami?
- our little shellcode baby needs to figure out a basis on which to use its relative addressing (see above)
- you can't just `mov eax, eip` to get the current instruction pointer into the general-purpose register
- what you can do is poke the [[stack]] a little bit
- when the [[CPU]] reads a `call` instruction, it pushes the address of the following instruction onto the stack
- once the function that's being `call`ed has completed, it executes `ret`, which returns the address that was put on the stack in the step above to the [[CPU#^53dada|instruction pointer]]
- so: how do we get the stack to give up that address?
- with a `pop` directly after a `call`!
- one could also abuse the floating-point unit, which is a separate execution environment in [[x86]] architectures for doing floating-point arithmetic
	- because to a computer, $\frac {2}{3}$ might as well be three dogs in a trenchcoat
- this unit keeps track of the instruction pointer, and stores that address at offset 12
## what am i doing here?