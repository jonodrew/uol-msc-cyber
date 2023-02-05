---
alias: [TCP]
---
TCP is used for continuous, free-flowing streams of data. It is duplex (simultaneously bi-directional) and point-to-point (each connection has exactly two end-points)

Except of course it can't work like that: instead, it cuts up a datastream and sends them as a byte stream. Note: it is a [[byte]] stream and not a message stream. TCP must therefore ensure:
- that all messages reach the receiver
- that the messages are received, or at least processed, in the right order
	- remember that the [[Internet Protocol]] does not guarantee that things will arrive in the right order!


## Acknowledgement
A TCP [[packet]] always has a sequence number. To ensure that the sender knows whether packets are arriving, the receiver will send frequent acknowledgements. These messages will contain the highest sequence number of the longest continuous run of packets received. That is to say, if the receiver has received everything up to packet 6 _and_ packet 8, it will acknowledge only '6' - it will not acknowledge having received 8. If no further communication is received, the sender will restart from the acknowledgement number.

## Handshake (threeway)
1. Initiator: TCP SYN
	1. subtext: I wanna talk to you
	2. this message has a randomly selected sequence number
2. Responder: TCP SYN ACK
	1. I hear you, let's do it
	2. this message contains a different randomly selected sequence number, and an acknowledgement number equal to the intitiator's sequence number + 1
2. Initiator: TCP ACK
	1. Okay, let's do it!
	2. the sequence number is increased on this side (that is, it becomes equal to the acknowledgement number from the responder), and the acknowledgement number sent is the responder's sequence number + 1

## Header
Similar to [[UDP]], the header has a
- source port
- destination port
- sequence number
- (acknowledgement number)
- various other things, including flags, such as SYN, ACK
- size indicator
- checksum