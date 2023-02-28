author: [[Andrew S. Tanenbaum]]

Found at: https://r2.vlereader.com/Reader?ean=9781292037189

published in 2013 (!)


## Chapter 1: Uses of computer networks
There is nothing particularly new, and I'm quite disappointed by the following quote:

>[!quote] Views that are publicly posted may be deeply offensive to some people. Worse yet, they may not be politically correct.

Just a reallly boring, stupid thing to say. Even a decade ago.

## Chapter 4: the medium access control sublayer
The what now

### 4.3: [[Ethernet]]
### 5.6: the [[network layer]] in the [[Internet]]
At the network layer, the Internet can be described as a series of interconnected autonomous systems. There are several major 'backbone' networks, known also as Tier 1 networks. Internet Service Providers hang off these backbones, and they provide internet connectivity to consumers, as well as regional networks. There are more ISPs connected to the regional networks, [[LAN]]s at universities and companies, and some other edge networks.

These networks communciate via the [[Internet Protocol]]. Broadly, it works as follows:
- the [[Transport Layer]] takes a data stream and breaks it up into data packets
	- packets can theoretically be as large as 64KB, but in practice they are generally only about 1500 bytes, which is the size of an [[Ethernet#Frames|ethernet frame]]
- IP routers forward the packet through the internet, from one router to the next, until the destination is reached
- at the destination the network layer reconstructs the original data stream, and then passes the data up to the transport layer
- the transport layer passes the data to the appropriate process
- there are also Internet Control Protocols:
	- [[Internet Control Message Protocol]]
	- [[Dynamic Host Configuration Protocol]]
	- [[Adress Resolution Protocol]] for IPv4, [[NDP]] for IPv6

#### 5.6.2: [[network address translator|network address translation]] and why it's a horrible idea

### Routing protocols for the [[Internet]]
The Internet, as we know, is a network of networks. Each network is autonomous and can use its own algorithm for internal routing - like a country's postal service. Equally therefore there needs to be a standardised way of routing packets between networks. The inter-domain protocol used on the Internet is [[Border Gateway Protocol]]. The most common intradomain routing protocol is called [[Open Shortest Path First]].  

### 6.1 the [[Transport Layer]]

#### 6.2.2: Connection establishment
- always design for the worst case
- the worst case in a network is:
	- [[Byzantine General Problem]]
	- interception
	- duplication
	- re-transmission
Let's start with delayed duplicates. On the face of it, the problem we have is that we can't tell the duplicates from the original, and might therefore understand them as two distinct requests. If you're ordering burgers, this may result in two burger orders. And then what will you do?

No, no. We need to ensure this doesn't happen. Now, there are design approaches in terms of APIs to enforce this ([[idempotency]]), but for the moment let's focus on the [[packet]] level of the problem. One solution to this problem is to restrict the lifetime of a packet, so that they can't hang around forever and suddenly surface. We do this through any of the following:
1. Restricted network design
2. A hop counter on each packet
3. Timestampting each packet
The first approach is an abstraction of any method that prevents packets from looping through a network, and is generally difficult to implement, because the [[Internet]] doesn't generally work like that. The second approach intitialises a value for the hop counter, which is decremented each time the packet is forwarded. This is present on [[Internet Protocol|IP]] headers. In the third approach, the packet is stamped with its creation time, and all routers agree to discard packets older than a certain time. This would require universal synchronisation of clocks, which would be tricky even if [[Special Relativity]] wasn't an issue. Which it is.

Additionally, like an efficient assassin, we need to ensure that not just the packet is removed but all knowledge of it as well. That is to say, any acknowledgements of the packet must also die. We can set a maximum packet lifetime at the network level: on the Internet it is (arbitrarily) 120 seconds. We can therefore describe some period $T$, which is a small mutliple of of that maximum packet lifetime. If we wait $T$ seconds after a packet has been sent, we should be confident that both it and its acknowledgements will have perished.

With this bound in place, we can now devise a practical way to reject duplicated segments:

The source labels segments with sequence numbers. It is not allowed to reuse those numbers within $T$ seconds. Therefore, the delayed duplicate of a packet can never beat the original: either the original will arrive first, or the original will perish.

{Sliding windows goes here, come back when brain works good}

### 6.5: [[Transmission Control Protocol|TCP]] 
