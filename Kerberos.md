An [[authentication]] #protocol that provides a means for workstation clients, users, and servers to authenticate to each other. 

We focus here on version 5, which uses [[symmetric|symmetric encryption]] for [[confidentiality]] and [[integrity]] protection. Kerberos is integrated into both [[Windows]] and [[Unix]] systems. 

Kerberos makes use of two different types of trusted third parties: an authentication server (AS) and a ticket-granting server (TGS). 

## Method
The client and the AS share a long-term secret key. This is used to generate a short-lived secret key which is shared between the TGS and the client (how?). The TGS is then involved (how?) in setting up the session key that is shared by both the client and the server it's trying to access. 