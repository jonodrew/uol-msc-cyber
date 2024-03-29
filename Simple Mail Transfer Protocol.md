---
alias: [SMTP]
tags:
- protocol
---
The Simple Mail Transfer Protocol is a protocol for sending and receiving email messages. It generally communicates over port 25. 

It is not a protocol for retrieving messages from a remote mailserver - for that, one would use either [[Internet Message Access Protocol|IMAP]] or [[Post Office Protocol|POP]]. SMTP is a protocol that operates over [[Transmission Control Protocol|TCP]], despite TCP being a continuous stream and SMTP being a request-response protocol.

In the old days, a mailbox was just another folder that other users could drop documents in. You'd then log onto the mailserver and use a local application to read your mail. Generally, we don't do this directly: instead we use gateways, which act like routers. They store a copy of the transmitted message and try to forward it on. Unlike a router, they might hold on to the message for a couple of days (rather than fractions of a second).

In this protocol, there is no authentication. There is also repetition of the recipient - it's both in the body and in the SMTP envelope. This enables the `bcc` functionality: under the hood, what's happening is that the SMTP envelope has all of the addresses but the body only has the `to` and `cc` addresses.

## STARTTLS
The letters in this acronym are meaningless, don't sweat it. What it *does* is enable [[confidentiality]] and [[entity authentication]] in the exchange between servers using SMTP.

## [[Multipurpose Internet Mail Extensions]]
![[Pasted image 20230316184912.png]]

## Attacks
As noted above, there is no authentication to an SMTP server. An open SMTP server can therefore be coerced into sending an email that appears to come from anyone. 