WannaCry is [[ransomware]]. The most well known attack from WannaCry affected the [[United Kingdom]]'s [[NHS]].

230,000 computers globally were attacked in May 2017. This attack was eventually attributed to [[Democratic People's Republic of Korea|DPRK]].

The NHS was a particularly good target because each trust manages its own IT, and in many places patching is not carried out at pace. 

This incident is the only Tier 2 cyber attack that the [[National Cyber Security Centre|NCSC]] has had to deal with. There have been no Tier 1 attacks since its founding.

## Decompiling Wannacry with [[Ghidra]]
### Questions
#### For function FUN_00401c70, can you specify what does the instruction at address 00401c88 (XOR EAX, EAX) do?
Zeroes out the register

#### Identify a loop in the same function. Show where it starts and identify the addresses and instructions of the termination condition.
At `401db5`, the assembly jumps to `401cdc`. This is an infinite loop with jumping-off points, because the loop runs `while(true)`. However, at `401dbe` for example, the loop will return early - if 1 is less than `local2d4`, which itself is equal to `DVar8 + 1` (`401dad, INC EDI`) 