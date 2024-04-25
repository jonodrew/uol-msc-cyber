A design blueprint for various kinds of [[block cipher]]. One example is [[DES]].

## The algorithm
Assuming a block of size _n_
1. Split the _n_ bits of plaintext into two parts of length $m=n/2$: the left _m_ bits $L_0$ and the right _m_ bits $R_0$.
2. Apply a carefully designed mathematical function $f$ which takes as input the key _K_ and $R_0$, and computes the output $f(R_0, K)$  
3. XOR the output of the mathematical function with $L_0$, to compute a new _m_-bit sequence $X = L_0 \oplus f(R_0, K)$ 
4. Let the new ‘right _m_ bits’ $R_1$ be $X$.
5. Let the new ‘left _m_ bits’ $L_1$ be the previous ‘right _m_ bits’ $R_0$.
6. Repeat the process from step 2 to step 5, except that $R_1$ is used instead of $R_0$, and $L_1$ instead of $L_0$. This sequence of steps (step 2 to step 5) is known as a _round_ of the block cipher. The function $f$ used is often referred to as the _round function_.
7. Repeat step 6 for as many rounds as specified by the algorithm design. Once the last round (round number $z$) is completed, then the last ‘left _m_ bits’ $L_z$ are joined with the last ‘right _m_ bits’ $R_z$ to form the $n$ bits of the [[ciphertext]], which is formed by concatenating $R_z$ and $L_z$ (in that order).

This algorithm can be implemented extremely simply in software. Observe:

```python
import functools  
from typing import Callable, Any  
  
Key = Any 
  
  
def feistel_round(left: bytes, right: bytes, round_function: Callable[[bytes], bytes]) -> tuple[bytes, bytes]:  
    new_right = int(left, 2) ^ int(round_function(right), 2)  
    new_left = right  
    return bytes(new_right), new_left  
  
  
def round_function_partial(key: Key, round_function: Callable[[Key, bytes], bytes]) -> Callable[[bytes], bytes]:  
    return functools.partial(round_function, key)  
  
  
def algorithm(rounds_remaining: int, round_function: Callable[[bytes], bytes], left: bytes, right: bytes) -> str:  
    if rounds_remaining == 0:  
        return "".join(map(str, [right, left]))  
    else:  
        right, left = feistel_round(left, right, round_function)  
        rounds_remaining -= 1  
        return algorithm(rounds_remaining, round_function, left, right)  
  
  
def main(key: Key, func: Callable[[Key, bytes], bytes], rounds:int, plaintext: bytes):  
    block_size = len(plaintext)  
    return algorithm(  
        rounds, round_function_partial(key, func), plaintext[:int(block_size/2)], plaintext[int(block_size/2):]  
    )
```

And then this will be repeated for each of the remaining blocks

The [[decryption algorithm]] is the same as the [[encryption algorithm]] above, but in reverse.

Given its simplicity, the difficulty of implementing a Feistel cipher is the design of the round function.