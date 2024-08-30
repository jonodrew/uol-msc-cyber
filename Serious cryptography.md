## Chapter 1
### #attackModel 
#### [[black box]] models
- [[ciphertext-only]] attacks (COA)
- [[known-plaintext]] attacks (KPA)
- [[chosen-plaintext]] attacks (CPA)
- [[chosen-ciphertext]] attacks (CCA)
#### [[grey box]] models
- [[side-channel attack]]
- invasive attacks

### Security goals
- indistinguishability: an [[attacker]] should not be able to tell a [[ciphertext]] from a random string, even if they have the plaintext. This is often abbreviated to **IND**
- non-malleability: given a [[ciphertext]] $C_1 = \mathbf{E}(K, P_1)$, it should be impossible to create another ciphertext $C_2$ whose [[plaintext]] $P_2$ corresponds meaningfully to $P_1$. Apparently a [[one-time pad]] fails this!
### Security notions
Combinations of goals and models
#### IND-CPA: semantic security and randomised encryption

^ad48d6

- the [[encryption]] function $\mathbf{E}$ should always return two different [[ciphertext|ciphertexts]] for the same [[plaintext]]
- one way to achieve this is with random bits injected into the function, making encryption a function over a key, a plaintext, and random bits:
$$C=\mathbf{E}(K,R, P)$$
Decrypting this should render the same output. Aumasson says that randomized [[encryption]] requires that ciphertexts be slightly longer than plaintexts, to allow for more than one possible ciphertext per plaintext. I don't fully understand this

##### Deterministic random bit generator (DRBG)
Oooh, _math_

Let us suppose there is an algorithm that generates random-looking bits given some secret value (for example, it reads off values of pi starting at some specific index). We can build a simple cipher as follows:

$$\mathbf{E}(K, R, P) = (\mathbf{DRBG}(K |\space| R) \oplus P, R)$$
(noting that in this world, $|\space|$ implies concatenation)

This cipher generates a random string and [[exclusive or|XOR]]s it with the plaintext. It then returns the ciphertext and the random bits, which means it makes more sense in my head to write it out as 
$$ C, R = \mathbf{DRBG}(K |\space| R) \oplus P, R$$

Aumasson argues _ad absurdum_ as follows that this cipher is secure:
1. Assuming that the DRBG is functioning correctly and generating random strings
2. Suppose you _can_ distinguish [[ciphertext]] from random strings. That is, you can distinguish $\mathbf{DRBG}(K |\space| R) \oplus P$ from a random string
4. Since we've assumed [[chosen-plaintext|CPA]] here, and [[exclusive or|XOR]] is simple to reverse (you just XOR it again), we can remove the XOR from the equation
5. Thus if (2) is true, we determine you can distinguish $\mathbf{DRBG}(K |\space| R)$ from random strings
6. If this is the case, then the DRBG is not generating random strings, negating our first assumption
### Other notions
- if a cipher satisfies IND-[[chosen-ciphertext|CCA]], then it naturally satisfies IND-[[chosen-plaintext|CPA]] - because anything a [[chosen-plaintext]] [[attacker]] can do, a [[chosen-ciphertext]] attacker can do also
- ditto NM-[[chosen-ciphertext|CCA]] and NM-[[chosen-plaintext|CPA]]
- However, IND-[[chosen-plaintext|CPA]] does not imply NM-[[chosen-plaintext|CPA]] - although NM-[[chosen-plaintext|CPA]] _does_ imply IND-[[chosen-plaintext|CPA]]
- and apparently IND-[[chosen-ciphertext|CCA]] implies NM-[[chosen-ciphertext|CCA]]
- Oh God
## Chapter 4
- let's talk about [[block cipher]]s!
- the big ones are [[DES]], [[AES]], and something called [[GOST 28147-89]]
- be wary of the [[codebook attack]]
## Chapter 6
- we love [[cryptographic hash function]]s!