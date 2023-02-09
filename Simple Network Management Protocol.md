---
alias: [SNMP]
tags:
- protocol
---
A very simple protocol with three verbs: `GET`, `SET`, `GO`!! Only kidding. It's `GET`, `SET`, and `GET-NEXT`. It is a request-reply #protocol and runs on [[UDP]]. Like all protocols, it comes with an accompanying specification. In this case it's called [[Management Information Base|MIB]]. The MIB defines the variables - the different kinds of data - that can be retrieved from a network node