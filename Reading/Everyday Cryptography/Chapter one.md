---
tags:
- cryptography
- CYM040
---
## [[Everyday Cryptography]] Chapter One - Basic Principles
Securing things might mean:
- ensuring we can trust the contents of a message, #integrity
- ensuring the message can be received, #availability
- ensuring the message can't be read in transit: [[confidentiality]]
- this is the [[CIA triad]]
- paradox of crypto: allows people to transact secretly. Good if you're sending account details, for example, but bad if you're sending [[CSA]] 
- when Keith talks about [[security services]], he doesn't mean Box or VX. He defines it as 
>a specific security goal that we may wish to achieve.

- he lists some of them:
	- confidentiality, or secrecy: that the data cannot be viewed by an unauthorised user (what does _authorised_ mean, then? has the key == "authorised"?)
	- [[data integrity]]: that is hasn't been changed
	- [[data origin authentication]]: the assurance that a given entity was the original (!) source of received data. Therefore, even if the data has been forwarded many times, there is still a means of proving that the message originally came from [[Alice]]
	- [[non-repudiation]]
	- [[entity authentication]]: assurance that a given entity is involved and currently active. Currently active requires a "freshness" check, like a short-lived token
### relationships between security services
 - [[data origin authentication]] is a stronger notion than [[data integrity]]. If you can be certain that the message came from the originator, but not what the message was, there is no value.
 - [[non-repudiation]] is stronger still than [[data origin authentication]]. If we need to be able to prove to a third party that data came from [[Alice]] and that it really says she is giving us her house, then we naturally need to prove also the integrity of the data and the origin
 - however, [[data origin authentication]] is not the same as [[entity authentication]]. For example: we should be able to prove that your grandmother's will was written by her and that the data in it has not been changed (even though it's changed hands multiple times). However, that's not the same as checking that your grandmother is there. Frankly, you need a medium at that point, and not a lawyer. Different kind of parasite.
 - with that being said, you could use [[data origin authentication]] plus a freshness check to provide [[entity authentication]]. After all, if we can prove that's Nana's signature, and she can tell us what's in it, then we can be pretty confident she's really Nana, and not a demon wearing her skin.
 - finally, [[confidentiality]] does not imply [[data origin authentication]]. Just because nobody else can read the message, doesn't mean it came from the person you thought it came from.
### concepts
- [[cryptographic primitive]]
- [[cryptographic algorithm]]
- [[cryptographic protocol]]
- [[cryptosystem]]

## primitives and what they can offer

### on their own
- [[encryption]] can only provide [[confidentiality]]
- a [[hash function]] can sometimes provide [[data integrity]]
- a [[MAC|message authentication code]] can provide both [[data integrity]], [[data origin authentication]], and sometimes [[non-repudiation]]
- a [[digital signature]] can provide [[data integrity]], [[data origin authentication]], and [[non-repudiation]]

## a basic cryptosystem
Suppose [[Alice]] wants to send something to [[Bob]]. She cannot be sure that the channel she's using won't be intercepted, and she wants the message to retain [[confidentiality]]. 

![[fig. 1.2.png]]

the following terms will be useful:
- [[plaintext]]
- [[ciphertext]]
- [[encryption algorithm]]
- [[decryption algorithm]]
- [[encryption key]]
- [[decryption key]]
- [[attacker|interceptor]]

To encrypt the [[plaintext]], the sender needs access to the [[encryption key]] and [[encryption algorithm]]. If the [[plaintext]] is not encrypted in a secure environment, there's no guarantee as to its [[confidentiality]]. The receiver needs access to the [[decryption key]] and the [[decryption algorithm]], and again should only decrypt the data in a secure environment.
It is worth noting that [[encryption]] cannot prevent interception, but it can render interception less valuable as an attacking technique, because the data will be unintelligible (there are caveats - see also [[Enigma]]). [[encryption]] also doesn't guarantee end-to-end confidentiality, because there is no way to guarantee the security at both ends.

There are two kinds of [[cryptosystem]]: [[symmetric]] and [[asymmetric]]

Broadly there are four theoretical #attackModel: [[ciphertext-only]], [[known-plaintext]], [[chosen-plaintext]], and [[chosen-ciphertext]]. 

[[Key lengths and keyspaces]] is a very important thing to know about.

