---
alias: [public-key cryptography, asymmetric cryptosystem, public-key encryption, asymmetric encryption]
tags: cryptography 
---
In this kind of [[cryptosystem]], the [[encryption key]] and the [[decryption key]] are fundamentally different, and it is impossible - or at least computationally infeasible - to determine the decryption key from the encryption key. This means that the encryption key can be made public

Asymmetric encryption is a kind of [[cryptography]]

## General form
The general form of a public-key encryption system has three algorithms:
```Haskell
PKE (Gen, Enc, Dec) :
	Gen: () -> pk, sk
	Enc: (pk, m) -> c
	Dec: (sk, c) -> m
```
The generating algorithm creates the public key and the secret key. The encryption algorithm takes a plaintext $m$ and the public key, and maps it to a [[ciphertext]]. The decryption algorithm takes the private, or secret, key and the ciphertext and maps it to a [[plaintext]].