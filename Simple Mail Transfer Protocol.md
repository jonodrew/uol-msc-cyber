---
alias: [SMTP]
tags:
- protocol
---
The Simple Mail Transfer Protocol is a protocol for sending and receiving email messages. It is not a protocol for retrieving messages from a remote mailserver - for that, one would use eeither [[Internet Message Access Protocol|IMAP]] or [[Post Office Protocol|POP]]. SMTP is a protocol that operates over [[Transmission Control Protocol|TCP]], despite TCP being a continuous stream and SMTP being a request-response protocol.

In the old days, a mailbox was just another folder that other users could drop documents in. You'd then log onto the mailserver and use a local application to read your mail. Generally, we don't do this directly: instead we use gateways, which act like routers. They store a copy of the transmitted message and try to forward it on. Unlike a router, they might hold on to the message for a couple of days (rather than fractions of a second).

