---
tags:
- protocol
alias: [CHAP]
---
An authenication protocol for [[point to point protocol|PPP]], and slightly more secure than the earlier counterpart [[password authentication protocol]]. 

Chap requires a three way handshake, which will initially take place when the link is set up with [[link control protocol|LCP]]. It may happen again at any time afterwards. 

The protocol employs a secret shared by the client and server, typically based on a client [[password]].

## algorithm
1. the server sends a challenge to the client
2. the client returns the answer: the output of a [[cryptographic hash function]], which takes as input the challenge and the shared secret
3. the server makes the same calculation
4. the server compares the two results. If they are the same, [[authentication]] has been successful. If not, the connection is terminated
>[!note]in this exchange, the password is never actually sent over the network. Additionally, because the challenge is timestamped, old challenges can't be re-used.

## weaknesses
Because this data is sent in the clear, an attacker can identify the challenge, the [[cryptographic hash function]], and the hashed combination of the challenge and the password. A weak password would consequently be vulnerable to a [[dictionary attack]]. 



