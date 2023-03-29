## What [[security service]] do we need?
[[confidentiality]]: Used to be provided by wired connections. However, anyone with a scanner can access wireless data. So we need data to be confidential when it's in transit

[[data integrity]]: much harder to do with a wired connection. Again, we need to provide a means of doing this wirelessly

[[data origin authentication]]: it's pretty important that we can be sure that data is coming from the client or the router, rather than an impersonator

[[entity authentication]]: is it important we know who's accessing the network? Yes, definitely, because clients on the network have more privileges than those who don't. We also want to make sure we're talking to the right [[router]]

### Doesn't need:
- [[non-repudiation]]: it's unlikely you'll end up in a dispute about who sent what data where, so we probably don't need non-repudiation from our wi-fi service. If this was needed, it would probably be at the application level


## mechanics
Wi-Fi refers to a family of protocols using radio signals. Wi-Fi relies on wireless routers, known as access points (AP), to which we connect our devices. These routers in turn are connected to the [[Internet]], thereby enabling access for any connected device. Wi-Fi protocols operate at the [[physical layer]] and [[data link layer]]. 

Every AP has its own Service Set Identifier (SSID), with an associated [[MAC address]] called a BSSID. AP broadcast their SSID, and it's on this basis that a device will decide to try to connect to an AP.

## security
Because Wi-Fi uses radio, it is trivial to intercept signals sent in this way. It is also simple to impersonate an actor on the network, including the AP itself. For example, an [[attacker]] could spoof a [[DNS]] response (assuming the DNS server is not using [[DNSSEC]]). One approach is to configure the AP not to broadcast its SSID, meaning that only users who know about it can use it.
>[!note] this smells like [[security by obscurity]] to me

You can also [[allowlist]] [[MAC address|MAC addresses]], but again this has limited value because those addresses can easily be spoofed. This is a great way to get access to WiFi in hotels though.


## standards
Standards for Wi-Fi are defined in the IEEE 802 series. In particular, see [[IEE 802.11]]

## Securing wifi
The first attempt to provide [[confidentiality]] with Wi-Fi was [[Wired Equivalent Privacy]]. Unfortunately this turned out to be slightly insecure, and we now use [[Wi-Fi Protected Access|WPA]] - specifically, WPA2 or WPA3.