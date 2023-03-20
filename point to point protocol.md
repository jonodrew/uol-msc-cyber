---
tags:
- protocol
alias: [PPP]
---
PPP is a [[data link layer]] communication #protocol . It is most commonly used for direct communication between two routers, ie, without any intervening hosts.

Some ISPs use PPP to support dial-up access to the [[Internet]]. 

PPP comprises:
1. an encapsulation component that is used to transmit packets over the [[physical layer]]
2. a [[link control protocol]] that is used to set up and configure the link
3. a [[network control protocol]], which manages the parameters for the [[network layer]] protocol running over PPP. 
[!note] a distinct [[network control protocol|NCP]] is required for each [[network layer]] #protocol 

## derivatives
There are two common kinds of PPP in existence today. PPP over [[Ethernet]], which is known as PPPoE, and PPP over [[Asynchronous Transfer Mode|ATM]], or PPPoA.
