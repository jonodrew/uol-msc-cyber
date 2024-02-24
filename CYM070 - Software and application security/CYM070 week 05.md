## reading
- [[The antivirus hacker's handbook#Chapter 4 Understanding antivirus signatures]]
- [[Practical malware analysis#Chapter 8 Debugging]]
- [[Practical binary analysis#Chapter 6]] and [[Practical binary analysis#Appendix C]]
- [[Malware dynamic analysis evasion techniques - a survey]]
## 5.1 [[dynamic analysis]] of [[malware]]
- so go look there, why don't ya?
### structuring disassembled code
- first, we compartmentalise
- this simplifies analysis
- and promotes logical understanding
- basically, trying to turn assembly back into the [[object oriented programming]] paradigm it came out of
- a control flow diagram is a nice way of showing how the code will behave at a high level
- here's a code example. I rewrote it because I care about writing good code, _even though_ I accept the point of the bad code might have been to point out how useful a control flow graph is for working through bad/weird code. 
```C
int findMax (int *intList, int length)
{
  unsigned int max, index;
  int result;

  if (length <= 0)
    result = -1;
  else {
    max = intList[0];
    index = 1;
    while (index < length) {
      if (intList[index] > max)
        max = intList[index];
	  index = index + 1;
    }
    result = max;  
  }
  return result;
}
```
## 5.3 Limits of [[dynamic analysis]]
- sometimes [[attacker|attackers]] will program [[malware]] to be aware of specific tools
- this is "anti-debugging"
### anti-debugging
- checksums: a program may run a checksum on itself, to ensure that it has not been tampered with. Remember that a debugger works by overwriting a byte with `INT 3`
- trap instructions: a general exception to catch debugger exceptions will allow a program to follow a different path
- using `ptrace()`: software can call ptrace to see if something else is already watching it
- sandbox evasion
- sleep technique - essentially making the debugger time out
- reverse-[[Turing test]]: the malware tries to ascertain whether they're in a 'live' environment by checking if it's working with a human - proxied by, for example, mouse movements, keystrokes, etc
- anti-[[virtualisation]]: altering behaviour if the malware detects it's in a virtualised environment