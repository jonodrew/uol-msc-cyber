---
alias: [layer 4]
tags:
- OSI
---
Two key protocols here: [[User Datagram Protocol]] and [[Transmission Control Protocol|TCP]]

Taking as an example, UDP interacting with the transport layer.

The UDP datagram, consisting of the header and payload as described in [[User Datagram Protocol]], is prepared by the transport layer. This part then becomes the payload when passed to the [[Internet Protocol]] layer, where the IP address is pre-pended. This in turn is passed to the [[data link layer]], where it is treated as the payload and again pre-pended with a header - this time with the source and destination [[MAC address]]. Finally, all of this is sent as binary over the wire, or the [[physical layer]].