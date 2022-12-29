Floating-point notation is a way of storing fractions in [[binary]]. We begin by designating the leftmost [[bit]] of the number as the sign bit. 0 is nonnegative; 1 is negative. We then divide the remaining 7 bits into two groups: the exponent field and the mantissa field. The first 3 bits following the sign bit will be the exponent field, and the final 4 the mantissa field.

Let's try this with an example: `01101011`

First character, `0`, means it's nonnegative. Exponent field is `110`, and the mantissa is `1011`

The mantissa goes on the left, and is prefixed with a 'radix point'. So :`.1011`

Then we interpret the exponent field as an integer using the [[excess notation]] method. That means `100` would be zero, and so `110` is 2. With a positive exponent, the radix point is moved to the right. Given the exponent is 2, the point is moved two positions: `10.11`

We can see at once that the part to the ~~right~~ left of the radix point is 2. But what about the part after?

Remember that the values ahead of the radix point are the base, raised to an incremental power. The same is true in reverse: the first point to the left of the radix point represents $2^{-1}$, or $1 \over 2$ . The next point to the left represents $2^{-2}$, or $1 \over 4$. So `0.11` is equivalent to 

$$2^{-1} + 2^{-2} = {1 \over 2} + {1 \over 4} = {3 \over 4}$$
This is not easy math, and it's frustrating to see it described as such.

Let's try another, with `00111100`. First bit: 0, so again it's nonnegative. mantissa is `1100`, and exponent is `011`.

Since the exponent starts with zero, we can assume it's negative. 3 bits means the lowest number it could be, at `000`, is -4. It's three more than that, which means this is $-1$. With a negative exponent we move the radix point on the mantissa field one position to the left, putting zeroes in where we create spaces. So we go from `.1100` to `.01100`, and that's the end of the process. Looking at the positions, we have:
$$0 \times 2^{-1} + 1 \times 2^{-2} + 1 \times 2^{-3} + 0 \times 2^{-4} + 0 \times 2^{-5} = {3 \over 8}$$
remembering that $a^{-n} \equiv {1 \over {a^n}}$ 

## Going the other way
Alright, so how about converting something? Let's take $1 {1 \over 8}$. 

(By the way, have you noticed something about all these fractions?)

So let's turn it into binary: `1.001`. We copy the binary number into the mantissa field, starting with the most significant bit - that is, the first `1` when reading left to right. This is important if you have something like $3 \over 8$, because that's `.011`. However, it will go into the mantissa field as `____1100` - the first value is ignored because it's a zero.

We get rid of the radix point and just put it into the right hand side of our [[byte]]-long register: `____1001`. Then we think to ourselves,

>[!help]
>How many places, and in which direction, would we need to move the radix point, if it were prefixed to this number, so that we could get back to `1.001`?

The answer is one position to the right. Moving right means a positive exponent, and +1 excess four notation is `101`. So that goes in next: `_1011001_`. Finally, we know our number is positive, so the significant bit is a `0`. So we get, at last, `01011001`

## Truncation errors