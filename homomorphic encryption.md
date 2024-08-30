A kind of [[encryption]] in which functions can be carried out without decrypting the data. 

This would be great, if it existed beyond toys.

From a mathematical perspective, this uses homomorphism. Encrypted data is just hidden: it's not actually 'scrambled'. In theory, you should be able to apply mathematical functions to encrypted data without radically changing the underlying data. Moreover, the user should still be able to decrypt the data with their original key, such that:

$$e^{-1}(f(e(m)) \equiv f(m)$$
That is, the decrypted output of the output of the function over the encrypted message is equivalent to the function over the message.

A company working in this space claims that we are within a year of homomorphic encryption being 'only' 10 times slower than regular encryption.

Homomorphic encryption, also sometimes known as 'levelled' or 'somewhat' homomorphic encryption, can 'evaluate circuits of a predetermined depth'

Wikipedia says:
- partially homomorphic supports the evaluation of one kind of gate only
- somewhat homomorphic allows the evaluation of two types of gates, but only for a subset of circuits
- leveled fully homomorphic is for when you have multiple types of gates but the depth is bounded
- fully homomorphic is when you can do level fully homomorphic down to any depth

Homomorphic encryption systems use the [[asymmetric#General form|general form for asymmetric encryption systems]], plus:

```Haskell
Enc(x) + Enc(y) = Enc(x+y)
Enc(x) * Enc(y) = Enc(x*y)
```

[[fully homomorphic encryption]] systems can do both, and some advanced systems can even do more than this!

The [[Serious cryptography#Security notions|security notions]] we're operating under for homomorphic encryptions are [[Serious cryptography#IND-CPA semantic security and randomised encryption|IND-CPA]]: indistinguishability under a [[chosen-plaintext]] [[attack]].

## Applications
- computations over sensitive data
- outsourced computation
- electronic voting
- multiparty computation

## Bootstrapping
- when carrying out operations under HE/FHE, noise is generated
- this has to be extracted before the result can be decrypted
- however, if the noise becomes too great, the result can never be decrypted
- so suppose we do $m \rightarrow Enc_{k1}(m) \rightarrow \varphi   Enc_{k1}(m)$ , where $\varphi$ is some function
- carrying out this function generates almost too much noise - we can't conduct any further homomorphic operations
- the noise can be removed by decrypting the [[ciphertext]] - but we don't want to do that. It ruins the whole point of doing HE
- with bootstrapping, we encrypt the noisy ciphertext: assuming the ciphertext of $k_1$ is $c_1$, and the result of the function $\varphi$ is $r_{\varphi}$, we generate $Enc_{k2}(r_{\varphi})$
- this new encrypted ciphertext has a low noise level
- we can then decrypt the original ciphertext homomorphically, such that we decrypt with the homomorphically encrypted first key, ie: 
```python
def encrypt(message, key) -> Ciphertext
...

def decrypt(ciphertext, key) -> Plaintext
...
ciphertext_1 = encrypt(message)
encrypted_result = f(ciphertext_1)
layer_2 = encrypt(encrypted_result, key_2)
decryption_key = encrypt(key_1, key_2)
result_encrypted_to_key_2 = decrypt(layer_2, decryption_key)
```

- I hope that's nice and clear
- the original key encrypted to the second key is also known as the 'bootstrapping' key
- bootstrapping is very expensive, and isn't always needed, but will generally be used for [[fully homomorphic encryption]]
- And now we go into [[lattice problems]]