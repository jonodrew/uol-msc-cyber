## Intro
The stack is a big heap of memory that grows downwards (ie, from a high address to a low address). We put values onto the stack with push and we get them off with pop. We only take from the top, so this means it's a last in/first out (LIFO) data structure.

### pop
The pop action doesn't actually _remove_ the value at the top of the stack. It copies the value into the operand and then increments the stack pointer. This means that the data is still there in the stack, but it's _considered_ empty

### overflow
Not just a site for feeding AI! When a programme calls a function, the return value is specified as the address whence the call was made. This allows the execution flow to pick up again once the function has terminated. If the function that is called can overwrite that return address and replace it with an address that points to something malicious - most likely [[malware]]



