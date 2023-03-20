---
alias: [ICMP]
tags:
- protocol
---
Messages about the [[Internet]] (as opposed to [[Internet Protocol|IP]], which is messages sent via the Internet)

A few important examples are:
- DESTINATION UNREACHABLE: the router cannot locate the destination, or a packet with the [[Internet Protocol#Version 4#DF|DF flag]] set cannot be delivered through a 'small packet' network
- TIME EXCEEDED: the packet's [[Internet Protocol#Version 4#TtL|TtL]] dropped to zero
- PARAMETER PROBLEM: an illegal value has been detected in a header field. Go immediately to jail, but first, debug your IP software and the routers on your network
- SOURCE QUENCH: once used to encourage hosts to chill tf out, this message is no longer used
- REDIRECT: used by a router to tell a host that the package was routed incorrectly
- ECHO and ECHO REPLY: the computer equivalent of "you up?" and "yeah ;)"
- TIMESTAMP REQUEST and TIMESTAMP REPLY: as above, but with timestamps
- ROUTER ADVERTISEMENT and ROUTER SOLICITATION: messages used to find the nearest router to a host

