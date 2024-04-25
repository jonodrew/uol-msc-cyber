## Reading
- [[Practical malware analysis#Chapter 19 Shellcode analysis]]
- [[Memory layout of C programs]]
- [[Hands-on penetration testing with Python]]
## 7.1 Memory components
- we're doing [[x86]] architecture!
- From top (the largest value, which we can say might be `0xFFFFFFFF` in a 4GB memory store) to bottom (`0x00000000`), we have:
	- the [[kernel]]
	- the [[stack]]
	- the [[heap]]
	- data
	- and text, where the compiled code lives
- remember that the stack grows downwards, and the heap grows upwards
- within the stack, we have stack frames. Within a stack frame, the [[CPU#^f78924|stack pointer]] points to the lowest address in the frame
## 7.2 Memory exploitation
- this entire section could be titled "You're writing code in `C`? Why?? It's 2024! Don't do that!"
- Memory-unsafe languages: keeping researchers in business!
- anyway here's [[buffer overflow]]
- what might overflow a buffer?
	- text input
	- [[packet|packets]]
	- environment variables
	- file input
- let's have some more code
```C
void printString(char *stringToPrint)
{
	char buffer[4];
	sprintf(buffer, stringToPrint);
	...
}
```
What could possibly go wrong with this?

- the first thing to do is to load the malicious code into memory
- this will require a string that doesn't contain a zero [[byte]], doesn't use the stack, and doesn't depend on the loader
- the goal is to launch a [[Shellcode|shell]] on the target machine, and get [[privilege]] escalation. Here's a neat little example:
```C
#include <stdio.h>
int main() {
	char *name[2];
	name[0] = "/bin/sh";
	name[1] = NULL;
	execve(name[0], name, NULL);
}
```
- This doesn't do privilege escalation, but it does pop a shell (as the kids say)
- okay, so now we have code that we want the [[CPU]] to run. How do we get it to do that?
- we know we can overwrite the return address with a [[buffer overflow]], but how do we know what address our shellcode is at?
- first thing we can do is increase the surface area. We can overwrite the addresses before our malicious address with "no-op", which means the CPU will slide straight over the instruction and towards our malicious address
	- like a computer-y [pitcher plant](https://en.wikipedia.org/wiki/Pitcher_plant#Feeding_behavior)
- however, this does make the [[malware]] payload bigger. So we trade accuracy for likelihood
- how do we find the return address?
	- this answer seems to rely on memory randomisation being turned off, which - why would anyone do that?
- one thing we can do is just put in a huge string of a single character and see if the base pointer ([[assembly|EBP]]) gets overwritten. If not, we add more of the same character until it's overwritten. This is know as padding
- let's put it all together!
### lab
#### section 1
1. The output differed in each case, because the address is being randomised
2. This command turns off the randomisation
3. The output was then the same with each call

## 7.3 Defences against memory exploitation
- USE A MEMORY SAFE LANGUAGE
- ooh, there's a thing called a [[stack]] canary?
	- it's inserted between the base pointer and the instruction pointer
	- it's a value that common functions used in overflow attacks can't process, or which terminate a function call, like carriage return, null, or `-1`
- then there are random canaries
- and then random [[exclusive or|XOR]] canaries, which is a value that's been XOR'd and is therefore very hard to overwrite correctly
- if a canary is noted as changing, then the program that changed it can be immediately terminated
- we also love address space layout randomization, which makes it harder for an [[attacker]] to identify the address they want. However, it can still be overcome with a [[brute force]] attack