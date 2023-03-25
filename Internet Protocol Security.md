---
alias: [IPsec]
---
## security services
An IPsec channel provies:
- [[confidentiality]]
- [[data integrity]]
- [[entity authentication]]

## use cases
IPSec secures traffic at the level of the [[Internet Protocol]], or [[network layer|layer 3]]. It is therefore suitable for the following use cases
- create a [[virtual private network]] over the public [[Internet]], eliminating the need for private networks
- establishing extranet and intranet connectivity with partners
- enhancing electronic commerce security (I think this might have been superseded)
- assert that a [[router]] or neighbour advertisement comes from an authorised router
- assure that a redirect message comes from the router to which the initial IP packet was sent
- assert that a routing update was not forged

## modes
### transport
Transport mode protection is for the payload of a packet at the layer above, ie [[transport layer|layer 4]]. This might therefore be an IP packet, such as a [[Transmission Control Protocol|TCP]] or [[User Datagram Protocol|UDP]] segment, or an [[Internet Control Message Protocol|ICMP]] packet. 

In tunnel mode ESP encrypts and has the option to authenticate the IP payload, but not the IP header. By contrast AH in transport mode always authenticates the IP payload and selected portions of the IP header, but does not encrypt it.

### tunnel
Tunnel mode provides protection to the entire packet. ESP adds a trailing field to pad the packet and then encrypts the original IP header, the payload, and the trailing field. This provides confidentiality. Then an ESP header is added, as well as an ESP auth field, which calculates a [[MAC]] over the fields listed below. This provides data integrity and [[data origin authentication]], on the assumption that no other party has the shared secret key. 

![[Pasted image 20230325171754.png]]
ESP also defends against [[replay attacks]]. 
## protocol
1. the [[Internet Security Association and Key Management Protocol|ISAKMP]] is used to establish a security association between the communicating parties, including establishing the shared secret keys, negotiating the [[cryptographic algorithm]], and whether [[Internet Protocol|IP]] packets are to be secured using an authentication header (AH) or via an encapusalating security payload, (ESP)
	1. In AH tunnel mode, the old IP header is considered as part of the original IP packet's payload. AH uses a [[MAC]] to provide integrity. However, it does not provide confidentiality, and for that reason is deprecated in favour of:
	2. ESP has two modes: transport and tunnel. In ESP transport mode, the [[Transmission Control Protocol|TCP]] header, the payload of the original [[Internet Protocol|IP packet]], and the new ESP trailer are encrypted. The ESP header is inserted between this new encrypted payload and the original IP header. Finally an ESP auth field is added to the end of the packet. The ESP trailer contains padding and the ESP auth field contains a [[MAC]] computed over the the other fields except the IP header.