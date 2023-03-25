---
author: [[William Stallings]]
---


### 1.2 The [[OSI]] security architecture
We review words again. We define a security attack, a security mechanism, and a [[security service]] - which unfortunately is not the same definition as used by the cryptographers. Or is it?
### 1.3 Security attacks
Attacks come in two flavours: active and passive. Passive attacks are those that don't alter the state of the system, such as eavesdropping or interception-and-pass-on, while active attacks alter the system or its operation.
### 1.4 [[security service]]
There's a lot there, and some of it's disputed by other parts of this course 😬
### 1.5 security mechanisms
Nothing interesting here, and potentially an error: encipherment should not be considered to provide data integrity (at least as I understand it)
### 1.8 A model for network security
Already covered, ad nauseam, elsewhere in this module

## Chapter 4
### 4.1 Remote user [[authentication]] principles
- [[identification]] is different to [[authentication]]


### 4.2 [[symmetric]] key distribution using [[symmetric|symmetric encryption]]
- it's very tricky
- Suppose we have two parties, A and B, who want to communicate with [[confidentiality]]. They will need to set up a shared key.
	- A could select a key and manually send it to B
	- A third party could select a key and deliver to both A and B, assuming it is trusted by both A and B
	- If A and B had previously solved this problem (don't think too hard about this), they could use their existing key to encrypt their new key
	- If A and B had an encrypted connection to a third party (a variation on the first option), then that third party could deliver a key to both A and B.
	- this brings us neatly to:

### 4.3 [[Kerberos]]

## Chapter 6
### 6.2: [[Transport Layer Security|TLS]]

### 6.4: [[Secure Shell|SSH]]

### 8.1

### 8.2

## Chapter 9: [[Internet Protocol Security|IPsec]]


## Chapter 12: [[firewall]]
