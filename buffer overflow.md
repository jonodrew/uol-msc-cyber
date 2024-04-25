A vulnerability in a system whereby more data is put into memory than has been allocated. The data overflows into the next address and may corrupt what is written there. For example, if you can overflow a buffer on the [[stack]], you can write a new return address. Then, when the function call ends, control will be returned to the address the [[attacker]] wrote - and thereby potentially allowing [[Shellcode]] execution

## Example
```C
void copyString(char *string)
{
	char buffer[4];
	strcpy(buffer, string);
}

int main()
{
	char *string = "Hello";
	copyString(string);
}
```
- *sigh*
- Okay, so what we have here is a function `copyString` which creates a local buffer with 4 bytes,  then copies the string passed as an argument into that buffer
- we also have `main`, which instantiates a variable with the value "Hello" (note: five characters, which is 5 [[byte|bytes]] in [[ASCII]]) and then calls `copyString` with that variable
- *sigh*
- *I wonder what will happen next*
- `strcopy` is called without checking the length of the input
- the extra byte is copied over the return address, which is the next thing in the stack. Because it's just 'o', the return address becomes `0x0000006f`, which is meaningless and would probably produce a segmentation fault
	- note that even though it's written into memory as `6f 00 00 00`, it's read out as `0x0000006f` because we're doing [[x86]] architecture which is [[endian#little-endian|little-endian]]
- man, wouldn't it be handy if there _was_ something at that address?
- or alternatively, that you could write in an address where you knew something useful was loitering?
- we can see where this is going