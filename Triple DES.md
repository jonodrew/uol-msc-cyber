Triple DES is an extension of the [[DES]] [[encryption algorithm]].  Triple DES is sometimes written $_3DES$. There are also variations of Triple DES: 3-key Triple DES ($_3TDES$) and 2-key Triple DES ($_2TDES$)

So, just to be clear: DES implemented three times with varying numbers of keys.

Triple DES with one [[encryption key]] is functionally equivalent to [[DES]], except three times slower. It is nonetheless used for the purposes of backwards compatability with DES.

## Three-key Triple DES
Alright! Three stages to this [[encryption algorithm]]. But first, we generate a $_3TDES$ key, which is three different [[DES]] keys. Let's call them $K_1$, $K_2$, and $K_3$
1. Using $K_1$, we encrypt the plaintext using DEs
2. Using $K_2$ (very important!) we decrypt the resulting [[ciphertext]]. This actually encrypts the content further
3. Finally we use $K_3$ to encrypt the result of 2., to produce our final ciphertext
The [[decryption algorithm]] is exactly the same, except in reverse - so decrypt, encrypt, decrypt.

## Two-key Triple DES
As [[#Three-key Triple DES]] except $K_1$ is used in the third position.