---
alias: [NAT,  network address translation]
---
The [[IPv4 address]] space is not big enough for all of the devices we've connected to the [[Internet]]. So how do we solve this particular problem?

We use a NAT, which is a little like a postal redirection service. It ensures that the IP addresses in a private network aren't given out to everyone on the web. It also solves out IPv4 problem - because it means addresses inside the private network that's 'guarded' by the NAT can use almost any address they like.

It also means that we're not "giving out" our IP addresses, which is a positive security measure - it decreases the [[attack surface]] by reducing the amount of public information.

## One-to-one NAT
A way to connect together two [[network|networks]] that have incompatible, ie clashing, [[IP address|IP addresses]]. When packets pass through the NAT, their IP head checksum is updated with the mapped IP address.

## One-to-many NAT
Multiple hosts within a private network have their IP addresses mapped to a single address - that of the NAT itself. This requires that the NAT keep track of all active connections passing through it, and especially the destination address and port. 

Apparently one widely-used method of NAT traversal is...hole punching.

Nothing says security like punching holes in things!

## Critiques
So many. As much as we dislike [[Andrew S. Tanenbaum]], he writes about them very effectively in [[Computer networks]]. 
1. In theory, every [[IP address]] in the world uniquely identifies a device. NAT allows almost all of the devices (aside from the NATs themselves) to use `10.1.1.10` if they want.
2. NAT breaks the model of the [[Internet]] - a host on an internal network, for example, can't receive a packet from an external host.
3. It also breaks the idea of a connectionless network (where packets can take many routes and there are no single points of failure) to a connection-oriented network where we're reliant on NATs. Stupid.
4. NAT relies entirely on [[User Datagram Protocol]] and [[Transmission Control Protocol|TCP]], which - again - why? People should be free to use whatever protocols they want.
5. It breaks the layer model, because it relies on what the layer below is doing. We can't realistically change or update TCP now, because NAT will break. It introduces dependencies