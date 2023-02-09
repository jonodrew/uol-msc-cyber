This book can be found on the web at https://book.systemsapproach.org/foundation.html

## Chapter 1
### 1.1 Applications
- nothing new here
### 1.2
- A set of nodes, connected, are a network
- Networks can be networked, but
- How do you reliably send data across such a network without packets being blocked by each other? There are two answers: [[circuit switching]] and [[packet switching]].
- A network of networks is an internetwork, or internet for short. This is not the same as the internetwork that uses [[Transmission Control Protocol|TCP]]/[[Internet Protocol]], which in common parlance is called the Internet.
>[!quote]
>I'd just like to interject for a moment. What you're referring to as 'the Internet', is in fact, the TCP/IP internetwork, or as I've recently taken to calling it, internetworking over TCP/IP.
- with a network of networks now connected, we must face the same problem we face in all such communication environments: how do we identify which node of the network we want to communicate with?
- same way we do it everywhere else: give it some kind of unique code or address.
- this is called routing
- Suppose we have three computers on a network, all sending data. How does the switch decide which has priority? How does it even send them?
- The most common method today is statistical multiplexing, whereby:
	- the switch defines a packet size
	- senders break their messages into those packets
	- if there is only one sender, then they can send as many packets as they like
	- otherwise, the packets are interleaved, and the received must reconstruct them
		- I wonder how? Some kind of pagination?

### 1.3 Architecture
- layering and abstraction are good (but also tricky!)
### 1.4 (Skipped)
### 1.5

### 7.1 Presentation formatting
Computers barely know how to talk to each other, and don't agree on some of the absolute fundamentals. Is the most significant bit of an integer the one with the highest address, or the lowest? Even the same language on different machines will compile differently, because obviously it will, why would there be standards, I mean, 
>[!note]
>This continues for some time. Skip ahead

#### 7.1.1 Taxonomy
So suppose a computer wants to send some stuff over a network. The stuff may comprise of data types, flat types, and complex types. All of this has to be serialized into a form that can be transmitted over the network, in the same way that thoughts, experiences, etc need to be flattened and hammered into 52 letters (in English) with a smattering of grammar and punctuation, only to be deserialized back into a tsunami of Feeling at the other end.
Remember that all of these have their intricacies. Big/little endian is a problem for `int` data types, but flat types like arrays need to be packed and unpacked. Complex data types, like trees, which contain pointers, are even trickier. A pointer on my machine will almost certainly not point to the same data on your machine.

## 9: Applications
We need them

### 9.1: Traditional applications
Let's get cracking with the [[World Wide Web]] and [[email]]. The classics. The OGs.

First, we need to be differentiate protocols from programs. For example, the [[HyperText Transport Protocol]]  is an application protocol used to retrieve documents from remote servers. Any application can implement that protocol for itself, and applications like Firefox, Internet Explorer, Chrome, and Safari all do so. The same is true of the [[Simple Mail Transfer Protocol]], which is used by mail clients. (Although other mail protocols are now available: [[Internet Message Access Protocol]] and [[Post Office Protocol]])

>[!question]
>What's happening when a web application like Firefox opens your GMail?

SMTP is the protocol, but they generally come packaged with a standard: for example, [[RFC]] 822 and the [[Multipurpose Internet Mail Extensions]] standards define the format of email messages.

#### 9.1.2: the [[World Wide Web]]
#### 9.3.2: Network management
How do you manage a network? Easy! You use the network itself. As we've established, you need a #protocol to communicate over the network. There are two general approaches: [[Simple Network Management Protocol|SNMP]] and [[OpenConfig]].
