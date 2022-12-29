---
alias: [message authentication code]
---
A message authentication code used [[cryptography]] to provide the [[security service]] of [[data integrity]]. To achieve this, the sender generally hashes the message, and then runs the hash through a MAC function using a [[symmetric]] key. This [[MAC]] is then sent with the message.

The receiver can then independently compute the MAC by the same process, and compare the two. If they are the same, then they can be confident that the message has not been changed in transit - though as always, this assumes that the key has not been compromised. 

Furthermore, if we can be confident that only the sender has the [[key]], we also have the service of [[data origin authentication]], because we know that it was most definitely sent by the person with the key.

## Attacks
### Forgery attacks
In essence, it should not be possible to generate the MAC without both the key and the plaintext. If the plaintext changes even a little, it should generate a completely different MAC.

The length of the MAC is therefore relatively important. A MAC of 1-bit long will be easy to forge, because it's either `0` or `1`. Therefore, the MAC must be long enough to make forging it very difficult. For example, if the MAC is 32 bits long, the probability of guessing the correct MAC is $1 \over 2^{32}$ . Whether this is strong enough depends on your application, though it's worth noting that $2^{32}$ is about 2 billion ($2 \times 10^{9}$)

For the algorithm to be secure, it must be resistant to attacks where an attacker knows several [[plaintext]]/[[ciphertext]] pairs. This is a standard requirement for a [[cryptographic algorithm]] - see [[Everyday Cryptography#1.5.1 Standard assumptions]]

## Key recovery attack
It should not be possible to deduce the key, or portions of the key, using [[plaintext]]/[[ciphertext]] pairs

## Replay attacks
This is an interesting one. What happens if an attacker intercepts and then re-sends a message with a valid MAC, maybe hundreds of times? If it's a charge to a card, the victim may see their wallet drained.

This could be avoided by having some kind of 'freshness' check, such as a timestamp that must be recent to within the last _n_-milliseconds. Alternatively, the sender and receiver could agree to sequence their messages, and if the receiver received a message that was not the next in the sequence it could discard it. 

Once could also use a [[nonce]] (steady!)