Hassh functions are a [[cryptographic primitive]]. 

A hash function takes as input a string of bits, and outputs a fixed-length string of bits. Modern hash functions output 256-bit strings, which is 32 bytes (there are 8 bits in a byte). Applying a hash function to a message produces a [[message digest]]. 

Hash functions are one-way only: you cannot get the message from the [[message digest]].

Hash functions have multiple uses:
- strong one-way functions, in cases where we never want to decrypt data but we want to know if new data is the same. The best known use here is for password hashing
- providing a weak notion of [[data integrity]], as an [[attacker]] would need to compute a new hash. However, this is generally pretty easy.
- as a building block for other [[cryptographic primitive]]s
- as a mean of binding data into a single place, which can then be more easily signed/encrypted
- as a source of pseudorandomness (with a big pinch of salt!)

## Properties of a hash function
### Physical properties
1. A hash function should be able to compress data down into a predictable, fixed-length output
2. It should be easy to compute, ideally in polynomial time
### Security properties
1. preimage resistance: it should be incredibly hard to go from a [[message digest]] back to the message. It's called 'preimage' because, sigh, mathematicians call the hash of $x$ its 'image'. Therefore the preimage is just...$x$. It's worth stressing that this property is not just "given some $h(x)$, it is hard to determine $x$." Because a hash compresses data, some inputs will have the same hash. And yet, it should be almost impossible to find any input that hashes to $h(x)$
2. second preimage resistance: now this is just a little different from the above. If you have both an input $x$ and the hash function $h$, it should be hard to find another input that produces the same hash. that is, it should be difficult to find a $y$, such that $h(y) = h(x)$.
3. collision resistance: rather than starting from the position of having $x$ and wanting to find a different input that produces the same hash, this property is concerned with finding _any_ two inputs that would produce the same hash
It's worth noting that if (3) holds true, then naturally (2) comes with it: if it's hard to find any pair of matching inputs, finding one specific pair is harder.

## Applications
### Password protection
When you set up a strong password, as you always do, the password should be hashed before it's stored. This prevents the system administrator being able to read your password, and also offers an element of protection against [[data exfiltration]]. Hashes are handy here because we don't ever want to recover the password, but we do want to check that the user's input is the same as it should be. We can take advantage of preimage resistance to be confident that even if the data is stolen, there's no way of getting passwords back out. Instead an attacker would have to construct a hash table.

## Lighweight [[data integrity]] check
A hash can be used to assure users that the thing they've been transmitted is the same as the thing they asked for, but it should be stressed that even then it's not a firm guarantee.
If a user puts up a file for download, and provides a hash, a user can check that hash when the file has downloaded and be confident that it's the same thing. It protects against intereference in transmission, but doesn't protect against an actor who's poisoned the site that the user is dowloading from. In order for an attack to be successful, assuming the attacker can't change the published hash, is find some malicious code package that has the same hash. We want to avoid this, and we do so by using second preimage hash resistance

### Binding promises
I'd never heard about this before, but it's fascinating. Suppose that we want Alice and Bob to commit to something but, importantly, it should be kept secret until some future date. The example in the book is a spending commitment. Alice and Bob hash their proposals and exchange them. Because of first preimage resistance, there's no way to work out the other's commitment. Later, they send each other their commitments in plaintext, and compare the hashes with those previously received. In this way information can be exchanged, revealed at a later date. Now, to avoid someone cheating, we need to be sure that the hash function is collision resistant: that is, once the unhashed information is revealed, neither party should be able to claim that they bid something different to what was received.
