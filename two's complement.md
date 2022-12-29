Two's complement is a means of storing integers as [[binary]] data. It is the most popular way of storing integers, although it has the weakness of [[overflow]]. 

In two's complement systems, the leftmost [[bit]] is the sign or significant bit: it tells us whether the integer is negative or nonnegative. 

Counting positive integers in this system is simple enough: you simply count as you would normally in binary, until you get to (for a four-bit system) `0111`, which represents the largest nonnegative two's complement number in a four-bit system.

However, negative numbers are not that simple. Consider: 6 is represented as `0110`: the leftmost bit tells us it's nonnegative, and then we have $2^2 + 2^1 = 4+2 = 6$

Negative 6, however, is represented by `1010`: which at first glance looks like it should be $-1 \times 2^1 = -2$. Unfortunately, that's not the case. If the number is negative, then its complement - its nonnegative counterpart - can be found by:
1. copying the bits right-to-left until you reach a 1
2. copy the 1
3. now copy the complement (the inverse) until you reach the end of the number
Using 6 as an example (`0110`):
1. `__10`
2. `1010`
Going the other way is the same algorithm: `1010` -> `__10` -> `0110`

To subtract in two's complement, you just add a negative number to a positive number. That is, where a human would read $2 + - 3$ as $2-3$, a computer reads it as $0010 + 1101$, which gives us `1111`, or $-1$, which is the correct answer.

However. When adding numbers, humans are good at imagining extra spaces for the number to go. Add 1 to 9 and you 'overflow' the units column, making 10. Computers don't have imagination, so overflow is a Bad Thing and can lead to awkward scenarios, like [Ghandi getting genocidal](https://en.wikipedia.org/wiki/Nuclear_Gandhi) (although apparently that's just an urban legend, boo)

