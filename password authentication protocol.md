---
tags:
- protocol
alias: [PAP]
---
An [[authentication]] protocol that works over [[[point to point protocol|PPP]]. It requires both client and server to share a username and [[password]].

## algorithm
The client sends the server the username and password. The server checks them and sends an acknowledgement back to the client if they are correct.

As [[point to point protocol|PPP]] is not encrypted, these are sent in the clear. Given this, PAP should only be used where the [[transport layer]] is secure: for example, where the cabling is properly protected. If it is not physically secure, a stronger protocol such as [[Transport Layer Security|TLS]] or [[Internet Protocol Security|IPsec]] will be required.