A UDP header consists of:
- a 2-byte source port
- a 2-byte destination port
- a 2-byte length
- a 2-byte checksum
- and the data/payload for the header

2 bytes is 16 bits, giving $2^{16}$ different ports that can be addressed. Port numbers are generally appended to the IP address, prefixed with a colon: `192.168.0.1:5000`, for example

UDP is generally used for one-off messages: the port is opened, the message is sent, and the port is closed again. However, in order to receive such a message, the receiver must already have a port open and waiting. If the port described in the header is not open on the received, the message is dropped, and an [[Internet Control Message Protocol|ICMP]] ERROR message is sent back to the sender.

UDP also has no concept of related messages, and such a mechanism has to be implemented by the sender. It is a very simple mechanism. As such, it's a good fit for [[DNS]] requests.