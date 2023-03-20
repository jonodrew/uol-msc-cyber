---
tags:
- protocol
---
This is an [[authentication]] protocol for gaining access to a network. 

## protocol
There are three parties in this protocol: 
1. a supplicant (😳)
2. an authenticator
3. an authentication server
The supplicant provides the required credentials to the authenticator. The requirements are defined ahead of time, and might be a username and [[password]] or a [[public-key certificate]]. The authenticator forwards the credentials on to the authentication server, where a decision is made as to whether access should be granted. 

Authentication servers typically implement [[remote authentication dial-in user service|RADIUS]], and can be located on the same platform as the authenticator.