---
alias: [DHCP]
---
DHCP is a network management protocol for the [[Internet Protocol]]. Its main purpose is to assign [[IP address]]es and other [[Internet Protocol|IP]] stuff to network devices. 

A DHCP server will know certain parameters of the network on which it's installed - for example, what the subnet is. It also knows the default gateway (which is necessary to reach other parts of the network), and which server is the [[DNS]] server. It stores this information in a 'lease database', pairing off IP addresses and [[MAC address]]es.

When a modern device is not connected to a network, they act as a DHCP client in order to get themselves an IP address. Once the device is connected to a network, it sends a "DHCP discovery message" that asks the local DHCP server to make itself known.

The DHCP server sets a preliminary IP address and then offers it back to the newly connected device. The device will (generally) accept by return message, and the DHCP will return an acknowledgement.

It is worth noting that this assumes everyone engaged in the communication does so in good faith, and is therefore susceptible to an [[attacker]].

