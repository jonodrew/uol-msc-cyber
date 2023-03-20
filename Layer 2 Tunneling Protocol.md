---
tags:
- protocol
alias [L2TP]
---
A [[tunelling]] protocol to enable [[virtual private network|VPN]]. It only uses [[encryption]] for its control messages: it does not provide [[confidentiality]] by itself. To achieve that goal, the tunnel itself should be passed over a [[network layer]] encryption protocol such as [[Internet Protocol Security|IPsec]].

L2TP works over [[User Datagram Protocol|UDP]]. 