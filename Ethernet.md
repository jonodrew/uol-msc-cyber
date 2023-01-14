A common standard for implementing the [[data link layer]].

Ethernet implements the [[bus]] style of architecture. The network comprises some number of devices, each interfacing directly to the 'ether'. Every machine broadcasts messages to every other machine on the network. 

## Frames
A frame on the Ethernet protocol consists of:
- 8 bytes of preamble
- 6 bytes that describe the destination address
- 6 bytes that describe the source address
	- both source and destination addresses are described by a [[MAC address]].
- The next field is ambiguous: 2 bytes that describe either the type of data or the length of the data. We can tell by the actual value that's in the field. The Ethernet protocol defines an upper limit for the length of a frame, so if the value in this field is lower than that, it's probably the length. If it's greater, it's probably a type.
- The next field is the actual payload, and can be anywhere between 46 and 1500 bytes.
	- As well as definining an upper length limit, Ethernet also declares a lower limit, so this payload field may need padding if it's very small.
- Finally there is a 4-byte checksum field. It is a weak form of [[data integrity]], because anyone who intercepts the frame can alter the data and then re-calculate the checksum