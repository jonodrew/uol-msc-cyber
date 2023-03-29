a kind of [[firewall]] operating at [[transport layer|layer 4]] and [[network layer|layer 3]] whereby the fields of packet headers are examined individually. The filtering may look at:
- [[MAC address]] - either source or destination
- Broadcast transmissions (?)
- [[Internet Control Message Protocol|ICMP]] - an older IP protocol that shouldn't be used any more
- [[IPv4 address]] - source or destination
- IP application protocol, which is inferred from the port numbers

A more advanced filter may apply different rules according to the time of day, or the destination host, for example. However, these rules are static, and cannot react dynamically to changes in traffic

## Stateful Packet Filters
Gollman, in [[Computer security]], talks about 'Stateful Packet Filters'. This sounds to me a lot like [[session filtering]]. With a stateful, or dynamic, packet filter, the firewall understands requests and replies. For example, they know about the [[Transmission Control Protocol#Handshake (threeway)|TCP open sequence]]. Rules are usually only specified for the first packet in one direction, and a new rule is created dynamically after the first outbound packet. Further packets are then processed automatically. 

