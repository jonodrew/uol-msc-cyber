---
alias: [XOR]
---
The exclusive or is as follows: that in a logical phrase, one must be true and the other false. That is, XOR(True, False) => True. See truth table below:

A|B|A XOR B
-|-|-------
False|False|False
True|False|True
False|True|True
True|True|False

It follows that !XOR is only True when the inputs are the same, regardless of whether the inputs are True or False.

Handily, if we convert the table above to binary...
A|B|A XOR B
-|-|-------
0|0|0
1|0|1
0|1|1
1|1|0

We see that it serves the same function as addition, assuming that in the last case the number overflows to the left (that is to say, 01 XOR 01 = 10)

[Read more on Wikipedia](https://en.wikipedia.org/wiki/Exclusive_or)