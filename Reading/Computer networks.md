author: Andrew S Tanenbaum

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