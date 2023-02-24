## Learning objectives
- Define different problems in widely-used protocols for secure communications
- Distinguish between different classes of secure communication
- Explain why [[availability]] is hard to achieve for any network application

## Lesson 1
- [[Denial of Service|DoS]]
## Lesson 2: secure channels
- we should probably secure our comms
- if only we had some way of doing that!
- enter: [[encryption]]
- ooh also maybe some kind of [[data integrity]]?
- and even [[data origin authentication]], though here it's called data source authentication
- replay protection
- preservation of message order also good
- we should also ensure that we have [[entity authentication]] on at least one of the peers
### Ephemeral keys
- an [[encryption key]] that is short-lived and discarded, thereby achieving the principal of [[forward secrecy]]
## Key exchange in [[symmetric|symmetric encryption]]
- [[Diffie-Hellman]]
- [[Key Encapsulation Mechanism]]
- Let's start with [[asymmetric|asymmetric encryption]] and how we bind a key to an entity. One approach is to use [[public key infrastructure]]
## Lesson 3: [[Transport Layer Security|TLS]]
## Lesson 4: [[Secure Shell|SSH]]
- read [[Network Security Essentials#6.4: Secure Shell SSH]]. It goes into really significant amounts of detail, and I'm confident I'm not going to need it.

