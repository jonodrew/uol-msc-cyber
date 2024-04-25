
## Chapter 3
## Chapter 4: Understanding antivirus signatures
- we love to use hashes, especially MD5 and CRC
- except the false positive rate is very high with CRC
>[!quote] in some cases, the original CRC32 algorithm is not used, but is replaced by a modified version. For example, the tables of constants used by the original algorithm may be changed or the number of rounds may be changed. This [...] may be something that causes you headaches

- most antivirus engines create their own set of CRC-like signatures
- they aren't very good, so now we use:
- 🎉[[cryptographic hash function]]s!🎉
	- like MD5 or SHA1
	- except of course changing a single bit creates a totally different hash value :(
	- enter: fuzzy hashes!
	- look how liddle and fuzzy they are ^.^
- in [[#Chapter 3]], there's something called a bloom filter?
- Then there's graph-based hashes. These are handy for polymorphic viruses (see [[CYM070 week 04#polymorphic malware !]]) because although the code body may move around, the call graph and flow graphs will be stable
	- one cool way to evade these is to have spaghetti code that makes the engine time out and give up
	- that is, any sufficiently complex piece of software is indistinguishable from [[malware]]
	- I'm using the word 'cool' wrong, I think
## Chapter 12: [[Static analysis]]
- walks us through an example of binary disassembly using [[IDA Pro]]
- recommends starting with finding the functions that manage memory, eg `malloc`, `free`, etc
- in this example he finds a function, `FMalloc(uint)`, which seems to be a wrapper around `malloc`
- reviewing the assembly we see that the function blithely tries to allocate as much memory as the function is passed, with no checks. One could pass `-1` for example, and watch it try to allocate every piece of memory in the system. And then crash. Crashes are good for breaking things!
- additionally, there's no check as to whether the call to `malloc` fails or not: it just tries to clear the memory pointer
- okay, so now we've got a method that's not been well written. Now we need to find out if we can indeed sneak a `-1` into the function call. We'll typically do this with user input that is not validated
	- note the difference between validated and sanitised. Sanitising input means cleaning it of mucky stuff like scripts; validation is ensuring it's within acceptable parameters
- another example using an application with a web browser component
- look for the SUID bit, because it often denotes something that can be run as root by a specific user
- the author then shows how you can take a little crack like poor sanitisation of password input and turn it into a command that makes the server open up a connection to your machine