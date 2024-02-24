
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