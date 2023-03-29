---
tags:
- protocol
alias: [WPA]
---

The Wi-Fi Protected Access protocol uses [[RC4]], like [[Wired Equivalent Privacy|WEP]]. However, it used a 64- or 128-[[bit]] key and a different security protocol called the [[Temporal Key Integrity Protocol]].

The longer secret key is not actually used to encrypt traffic. Instead, a different key is generated for each [[packet]]. 

As long as a good, long secret key is used, WPA2 and WPA3 have no known security weaknesses.

## Protected Access Enterprise
This offers more sophisticated [[authentication]] and [[encryption]] mechanisms. In particular, authentication can be managed by a [[remote authentication dial-in user service|RADIUS]] server.

## KRACK
This attack interferes with the [[authentication]] protocol that takes places when a client connects to an access point. The protocol re-uses a supposedly one-time value in its third step. By repeatedly resending the third request in the protocol, the AP will encrypt the request using the same [[stream cipher]] [[keystream]]. This allows the [[attacker]] to calculate the encryption key and consequently decrypt the traffic.

