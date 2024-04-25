## Reading
- [[Malware, rootkits and botnets#Chapter 2 a brief history of malware]]
- [[Practical binary analysis]] chapters 1, 2, appendix A
- [[Malware analysis, an introduction]]
## 2.1 Definition and types of [[malware]]
### What is [[malware]]?
#### history
- [[Brain]] can be considered the first PC virus. It originated in [[Pakistan]] and targeted IBM PC platforms - specifically, the boot sector
- The [[Morris worm]] infected about 6,000 computers in 1988, spreading across the burgeoning [[Internet]]
- In 1999 we saw [[Melissa]], a virus written in [[Microsoft]] Word's macro language. It selected 50 of the victim's contacts at random and spread rapidly
- 2000 brought 'I love you' worm, which was so named because it was contained in an email attachment titled 'Loveletterforyou.tax.vbs'. [[Visual Basic]], and [[Visual Basic]] scripts, are still a very common tool to spread malware
- 2003 was the year of 'the Slammer' (why are these starting to sound like Spider-Man villains?), which massively slowed [[Internet]] traffic and infected nearly 75,000 victims in only ten minutes
- Storm Worm attacked in 2007, masquerading as a news alert of a disaster. It took control of the victim computer, enabling the [[attacker]] to use it in a [[botnet]].
- [[stuxnet]] came up in 2010: a sophisticated piece of malware designed to sabotage the nuclear program of [[Iran]]
- [[CryptoLocker]], the first [[ransomware]] to demand payment via [[Bitcoin]], was first seen in 2013
- That approach grew over the next few years, and in 2017 we saw [[WannaCry]]
#### [[attack vector|vectors]]
- infected websites ([[watering hole attack]])
- [[email]] attachments
- external devices, such as USB devices
- unpatched [[vulnerability|vulnerabilities]]
- malicious advertising
- [[Mydoom worm]] was propagated by email, and at its peak accounted for 25% of all emails being sent worldwide
- 🚨 avoid clicking links klaxon 🚨
	- If we furnish users with the link-clicking machine THEY WILL CLICK THE LINKS
- 'human error is often a _significant_ factor in a successful malware attack'
	- No it isn't! And root cause analyses like these are why people hate us!
## 2.2 [[malware]] anatomy
### Binary compilation process
- binary files: it's a file in...[[binary]]
- how do we go from source to binary?
	- preprocessing: comments are stripped out and macros are expanded. In Python, this is where the libraries defined in the import step are actually imported. The output of this step is a preprocessed file - in python, it ends .pyi
	- compilation - turns the expanded, high-level code into [[assembly]]. 
	- processing
	- assembly -> here's where we turn things into [[binary]]. Labels and symbols are converted into actual memory addresses. This outputs 'object files'
	- linking - multiple object files are combined into a single, executable file
		- note that static libraries are copied into the executable, while dynamic libraries are called by the executable
### executable file
- in [[Linux]] we use the [[Executable and Linkable Format]] (ELF) for executable files
- [[Windows]] has [[Portable Executable]]

### [[binary]] files
- disassembly is when we convert binary files back to assembly
- we can do this to better understand what the binary does, even if we don't have the source code
- disassemblers:
	- IDA Pro
	- Radare2 (open-source)
	- Ghidra (open-source, developed by the [[NSA]])
- decompilation is a way of converting assembly back into higher level source code. Some well-known compilers are: 
	- JD-GUI
	- .NET Reflector
	- Ghidra (again)
- disassembling and then decompiling is [[reverse-engineer|reverse engineering]]
- [[static analysis]]
- [[dynamic analysis]]
### challenges in binary analysis
- [[obfuscation]]
- packed (compressed/encrypted) binaries
- anti-debugging/anti-analysis routines
- architecture differences 
## 2.3 [[malware]] analysis
- [[anti-virus]] mechanisms:
	- began with signature analysis, usually using a [[cryptographic hash function]]
	- Then [[byte]]-level, or instruction-level, signatures
	- Then heuristics, where we start looking at behaviour, rather than specific bytes or signatures
- turns out there's a test file for malware. All you have to do it save a file containing the following string: `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*` in plain text and your anti-virus should fire
	- Probably shouldn't do that on any machine you don't own
- we've tried checksums
- then [[cryptographic hash function]]s
- then fuzzy hash functions, that group up similar malware signatures
	- `ssdeep` creates fuzzy hashes, which creates comparable hash values that get further apart as their sources change
- then graph-based hashes, which require an amount of 
### tools
- first look at the .exe file with a hex editor
- Then with [[Ghidra]]
	- Use the standard defaults to start with
- Case study: [[WannaCry]]