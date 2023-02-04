---
alias: [ARP]
---
This protocol is defined in [[RFC]] 826. An [[IP address]], whether it's an [[IPv6 address]] or [[IPv4 address]], is necessary but insufficient for sending packets. Network Interface Cards, such as [[Ethernet]] cards, operate at the [[data link layer]] and don't understand these funky new [[Internet]] addresses. The Ethernet card has its own, unique [[MAC address]]. It sends and receives using this. How then do we translate from the Internet to the Ethernet?

Simple: we kind of don't. We do what we'd do with post in the good old days: get to the town square and yell "I've got a message here for Dave!" and someone would yell back "I know Dave, he lives over there" and then you'd go give it to Dave, unless Dave had died of scurvy or whatever.

A couple of examples:
### Same network
A host on a network wishes to send a packet to `::192.32.65.5`. The host looks at the packet, looks at its own [[IPv4 address]], looks back at the packet, and then directly down the camera at you. The packet is for a host on its own network, so it then outputs a broadcast packet on the [[Ethernet]] asking the real `::192.32.65.6` to please stand up. Only the correct host will respond with its MAC address. At this point, the software can create an [[Ethernet#Frames|frame]] and things carry on the way Ethernet normally does - the frame is put on the network; the destination host picks it up, extracts the IP packet, and hands it to the IP software. The software then processes the packet. So far so good. Most networks aren't like this, so:

### Different network
On a different network we construct a frame for the ethernet port of the router nearest to us, and send the frame with the IP payload. The router then checks itself, and identifies the next hop, changing the destination Ethernet address. Eventually we reduce the problem to the same as the one above