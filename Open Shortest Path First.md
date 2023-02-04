---
alias: [OSPF]
---
Standardised in 1990, this protocol is used for intradomain routing of [[Internet Protocol|IP]] packets. It supports point-to-point links like [[SONET]] as well as the kind of broadcast networks characterised by most [[LAN]]s. 

OSPF abstracts a network into a directed graph whose nodes are routers and networks and whose arcs, or links, are the connections between them. Point to point links are represented as bidirectional arcs whose weights may be different. A broadcast network is represented as a node itself, which is connected to routers. Networks that have no onward transmission path - that are the network equivalent of a cul-de-sac - only have an arc to them, but not one returning.

OSPF then uses the link state method to have every router calculate the shortest distance from itself to all other nodes. Where there are multiple shortest paths, traffic can be split across them. 