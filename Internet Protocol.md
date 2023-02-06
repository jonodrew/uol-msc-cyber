---
alias: [IP]
tags:
- protocol
---
The internet protocol is used to connect devices across the [[Internet]]. There are two distinct version of the internet protocol: v4 and v6. The most obvious difference is address length: v4 uses 32-bit (4 byte) addresses written in decimal, eg `192.168.1.1`. By contrast, v6 uses 128-bit (16 byte) addresses, expressed as eight [[hexadecimal]] numbers divided by colons. They are also often enclosed in square brackets, eg `[2606:2800:0220:0000:0000:0000:25C8:0046]`

The largest 4-digit hexademical number, `FFFF`, corresponds to $16^{4}-1$, or 65536.

## Version 4
![[Pasted image 20230120085320.png]]
IPv4 datagram header. It is 20 bytes (160 bits) long, and is represented here as a table 32 bits long and five rows deep. The "options" part is of variable length

Reading left to right, top to bottom:

### Version
Which version of the protocol is being used. v4 is the most common, but v6 will start to be used more and more as the population of internet-connected people increases, because it allows for significantly more numbers

### IHL
The length of the header in 32-bit words. The smallest possible value is 5 - and since $5\times32=160$, this represents a header with no options. The largest is 15, which amounts to $15\times32=480$. 480 bits is 60 bytes, leaving only 40 bytes for the options (because I guess this means that the maximum size of the header is 100 bytes??). For some options (we'll get to them later), 40 bytes is too small to contain them, rendering the whole thing useless.

### Differentiated services
This field is one byte long, and the eight bits are read as follows: the first six mark the service class of the packet, while the last two carry explicit congestion notification information

### total length
This is the total length of the entire datagram, both header and the data/payload. The maximum length allowed is $2^{16}-1$, or 65,535. For now this is about acceptable, but as data increases we may need to enlarge it

### identification
All fragments of a packet have the same identification number

### evil [[bit]]
This is an unused bit, which as an April Fools was proposed to be used to mark malicious traffic. This would massively simplify security, but was sadly not implemented, as it turns out malicious people just pretended their traffic was good. Is nothing sacred?

### DF
Stands for `Don't Fragment`, and orders routers to try to deliver the entire packet in one great big gulp

### MF
~~motherfucker~~ this stands for `More Fragments`. All fragments except the last one have this bit set to `True`, to indicate that there is more to come.

### Fragment offset
Where in the current packet this fragment belongs. This field is 13 bits long, permitting a maximum of 8192 fragments per packet

### TtL
The time a packet has left to live. It's decremented with every hop. If it reaches zero, the the packet is discarded and a warning packet is sent to the host: "Sorry pal, your wee packet wandered around lost until it expired. Try again eh?"

### protocol
This is used to tell the [[network layer]] what to do with a re-assembled packet; ie, which transport process it needs to give it to. It might be [[Transmission Control Protocol|TCP]], but it could as easily be something else, like [[UDP]]. Rather than letters, they're numbered, and those numbers are globally the same - and stored in a database at www.iana.org

### header checksum
Because the header contains very important information, it gets its own checksum

### source address/destination address
The source and destination expressed as an [[IPv4 address]]


## Version 6
Version 6 of the Internet Protocol uses 128-bit addresses, and only has seven fields in the header. It is 40 bytes long
![[Screenshot 2023-01-22 at 09.38.07.png]]

### Version
As with [[#Version 4]] above, the first field in the header tells the router what version they are dealing with. 

### Differentited services
[Same as above]([[#Version 4#Differentiated services]])

### Flow label
This field provides a way for a pair of addresses to mark a group of packets that should be treated in the same way by the network. This feels to me a little like being able to mark certain vehicles with flashing lights and sirens, thereby communicating that they have priority and reserved right of way. The flow is set up in advance and has an identifier. Flow labels are chosen randomly, and therefore the best way for routers to identify them is by constructing a [[hash function|hash table]]. 

### Payload length
Similarly to [[#Version 4#total length|total length above]], this describes the length of the payload. However, in v6, the header no longer counts towards the total length of the payload. 

### Next header
This field says which, if any, headers follow this one. The reason that v6 can "simplify" the header is because it just moved the options to consequent headers. If there are no more headers to come, this field serves the same purpose as [[#Version 4#protocol|protocol]]

### Hop limit
Since [[#Version 4#TtL]] just measured hops, rather than seconds...the name was changed to reflect what it actually does

### source address/destination address
Presented as [[IPv6 address]]

