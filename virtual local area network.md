---
alias: [VLAN, Virtual LAN]
---
A way of partitioning network traffic sent on a single broadcast medium into separate streams. This gives the appearance of separate [[LAN|LANs]], even though there is only one physical network.

One common use-case for a VLAN is to separate [[Voice over Internet Protocol]] traffic from other traffic.

## approaches
- port-based: the port number of the host defines which VLAN traffic is sent and received on. This approach requires a pre-configured table mapping port numbers to VLAN identifiers, or VLAN IDs. Changing the mapping must be carefully managed by a sysadmin. This approach is static.
- [[MAC address]]-based: traffic is categorised according to the source MAC address of a packet. As above, it requires a table to map MAC addresses to VLAN IDs.
- protocol-based: network traffic is partitioned according to the higher-level #protocol  that's in use.
- tag-based: packets can be tagged to indicate which VLAN they are being sent on. Such tags conform to standards that are either open or proprietary: one common standard is defined in [[IEEE 802.1Q]].