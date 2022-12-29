We keep track of packets exchanged between pairs of sockets - that is, between hosts using a specific pair of port numbers.

Some implementations perform so-called "circuit filtering", in which the [[firewall]] creates a proxy TCP connection to carry the packets through the firewall. Circuit filters essentially filter on whether or not the connection is accepted. This has a huge vulnerability: a legitimate connection could easily be abused, and it wouldn't be stopped by this kind of filtering. Alternatively, this kind of filtering can be achieved with stateful packet filtering that maintains information on the connection and on the state of the session.

## Example
Suppose we have a [[firewall]] that blocks incoming connections and only allows clients to open outbound connections to the [[Internet]]
- A packet from an internal host arrives at the firewall. Its SYN flag is set. This connection is allowed by the filter, so the packet is forwarded, and the socket information is noted. The state of the connection (opening) is also noted
- A packet arrives from the internet with SYN and ACK flags set. The filter can then update its knowledge of the session to say that it's almost open
- the internal host sends back an ACK packet, denoting a fully open connection
