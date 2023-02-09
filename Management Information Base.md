---
alias: [MIB]
---
The specification describing data that can be retrieved with the [[Simple Network Management Protocol|SNMP]]. The current version is MIB-II, and organises variables into groups as follows:
-   System—General parameters of the system (node) as a whole, including where the node is located, how long it has been up, and the system’s name
-   Interfaces—Information about all the network interfaces (adaptors) attached to this node, such as the [[MAC address|physical address]] of each interface and how many packets have been sent and received on each interface
-   Address translation—Information about the [[Address Resolution Protocol]], and in particular, the contents of its address translation table
-   [[Internet Protocol|IP]]—Variables related to IP, including its routing table, how many datagrams it has successfully forwarded, and statistics about datagram reassembly; includes counts of how many times IP drops a datagram for one reason or another
-   [[Transmission Control Protocol|TCP]]—Information about TCP connections, such as the number of passive and active opens, the number of resets, the number of timeouts, default timeout settings, and so on; per-connection information persists only as long as the connection exists
-   [[UDP]]—Information about UDP traffic, including the total number of UDP datagrams that have been sent and received.
There are also groups for the [[Internet Control Message Protocol|ICMP]] and of course the [[Simple Network Management Protocol|SNMP]] itself.