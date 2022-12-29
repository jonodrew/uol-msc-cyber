a kind of [[firewall]] whereby the fields of packet headers are examined individually. The filtering may look at:
- [[MAC address]] - either source or destination
- Broadcast transmissions (?)
- ICMP - an older IP protocol that shouldn't be used any more
- [[IP address]] - source or destination
- IP application protocol, which is inferred from the port numbers

A more advanced filter may apply different rules according to the time of day, or the destination host, for example