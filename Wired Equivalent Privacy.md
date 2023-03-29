---
tags:
- protocol
alias: [WEP]
---
Wired Equivalent Privacy used a 40-[[bit]] [[symmetric|symmetric encryption]] [[key]] using the [[RC4]] [[stream cipher]]. Every client would therefore need to know the key in order to communicate. This key was typically written as 10 [[hexadecimal]] digits.

WEP has two [[authentication]] modes, but does not require it: open system authentication and shared key authentication. In open system authentication there is no initial authentication step. Either the client has the key or doesn't - and if it does not, communication will fail. By contrast, in shared key authentication mode, also uses a 40-bit key and a unilateral [[challenge-response protocol]]. 

If no authentication is offered, users can simply connect to the AP and then on to the Internet. However, what they may not know is that their traffic can be intercepted by the router - and if they are not communicating with an [[HTTPS]] secured server, that traffic will be in [[plaintext]]. 

Unfortunately, even if authentication is offered, the way the [[challenge-response protocol]] is designed makes it easy to conduct a [[brute force]] attack, because the initial challenge is sent in plaintext - giving an [[attacker]] a [[known-plaintext]] vector.

WEP was superseded by [[Wi-Fi Protected Access|WPA]].