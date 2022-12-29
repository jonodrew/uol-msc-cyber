---
alias: [Electronic Code Book mode]
---
An approach used for breaking up a message for [[encryption]] by a [[block cipher]]. Its use is discouraged for human language messages, because of the high likelihood of repeated [[plaintext]]/[[ciphertext]] pairs.

## Approach
Simply put, ECB mode is the easiest for a human to understand, because it's how we might do [[encryption]] if we had to do it by ourselves. We take a block of plaintext, encrypt it with the [[encryption key]], and move on to the next block.

## Problems
So many

## ciphertext manipulations
Certain ciphertext manipulations may be undetectable when using [[ECB mode]]. An attacker could:
- replay (part of) an old ciphertext
- delete certain blocks of ciphertext
- rearrange the ciphertext blocks
Now, this may result in a broken plaintext that doesn't make sense - but, equally, it could result in a disastrous mistake. Consider what would happen, for example, if the addresses for [[GCHQ]] and the Russian embassy in London were swapped.

### statistical attacks
Letter [[frequency analysis]] can be applied to basic ciphers, like the [[Caesar cipher]] or even the [[Vignère cipher]]. We can consider a block cipher in ECB mode to be a 'mono-block-ic' cipher; that is, because a specific plaintext is always encrypted in the same way, we can identify patterns. This attack is best used when the source plaintext-space is relatively small - for example, the phase-space of exam marks out of 100 (trust a lecturer to come up with that)

### [[dictionary attack]]
Because the same plaintext will always give the same ciphertext, users should be vary carefuly not to send the same plaintext with different keys. For example: suppose an organisation checks that everyone is using the same key by demanding that all users encipher the phrase "Hello world" and transmit it to HQ at 0800 every morning. This can be negated to a certain extent by the use of large blocks and large keys, 