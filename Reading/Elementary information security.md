author: [[Richard Smith]]

One of the reading in [[5. CYM010 week 5]]

### 10.1 The network security problem
- "the" lol optimist
- Physical networks - [[LAN]] - are generally easier to secure. You can put the signal inside a cable and protect the cable with a building, security guards, all that good stuff
- on the other hand there's the risk that a single unguarded jack and, pop: someone else is on the network
#### 10.1.1 Basic network [[attack vector]] and defenses
- physical theft
- subversion: modification of a network to enable an attack. This will involve change to the physical or logical structure of the network, but does not alter the network traffic
- disclosure: an attacking computer captures copies of network data (rather than intercepting and blocking onwards transmission)
- forgery: constructing a fake message that looks real, or modifying a legitimate message, as part of an attack
- masquerade: tricking the network into sending messages that are apparently originated by someone else
- [[Denial of Service]]


### 12.3 Names on the [[Internet]]
IT'S DNS, MOTHERFUCKERS

Names in the DNS form a hierarchy, and different servers are assigned to different sections. These sections are called zones. A server assigned to a zone is considered the authority for answering questions about domain names in that zone.

#### DNS vulnerabilities
- cache poisoning
- DOS attack on major server
- DOS attack on shared resolver
Not mentioned:
- all of the fun things we find in the day job
### 12.4 [[Internet]] firewall
- a firewall reduces a network's [[attack surface]] by limiting the kind of network messages passing in or out
- your average home [[Wi-Fi]] box probably also has a fairly basic firewall, with a Default Allow policy for outbound traffic and a Default Deny policy for inbound traffic
#### 12.4.1
SKIPPED - NAT/DHCP stuff
#### 12.4.2 Filtering and connectivity
- [[packet filtering]]: the simplest kind of firewall
- inbound connections: what if we do actually want The Inernet People to communicate with us?
#### 12.4.3 Software-based [[firewall]]
- a [[firewall]] is generally today part of the standard operating system installed on a consumer device. The role of these software-based filtering approaches is basically the same as it is at the network level: that is, they control inbound connections and control access to the network by the applications on the user's device
## Chapter 13: Network encryption

## Chapter 14: [[Internet]] services and email

### 14.4 Enterprise [[firewall]]

#### 14.4.1 Controlling [[Internet]] traffic
- Gateways implement controls  in these four ways:
	- Host control: the sending or receiving host address
	- service control: the [[Transmission Control Protocol|TCP]] or UDP service as indicated by the port number
	- direction control: whether the session (connection?) was initiated inside the private network or from the [[Internet]]
	- content control: whether the data being transmitted violates specific restrictions (boooooo)
- these controls are applied across the protocol stack:
	- Link header/IP header -> host control
	- the service control looks at the TCP/UDP port number, which is part of the TCP/UDP header
	- direction control operates at the same level, examining the direction whence the traffic came
	- content control acts at the lowest level, examining the actual application data
#### 14.4.2 Traffic-filtering mechanisms
In order of increasing complexity:
1. [[packet filtering]]
2. [[session filtering]]
3. [[application filtering]]
#### 14.4.3 Implementing firewall rules
Generally, the fields on a firewall rule are:
1. Control number: number the rule so that it can be cross-referenced against a security policy
2. type of rule: generally either 'allow' or 'deny'
3. direction: 'in' or 'out', with the starting direction being the host device
4. transport protocol: 'TCP', 'UDP', 'All'
5. source socket: the host and service that produces the packet. Each field could be written as `value1-value2-value3` etc, or permit all possible values with the asterisk character `*`
	1. the host identifier might be IP address(es) or domain name(s)
	2. the service will be a port number or a protocol acronym
3. destination socket: the host and service intended to receive a packet defined by this rule. Again, has the same fields as source socket (above), with the same values
4. requirements: (ugh) the numbered requirements statements addressed by this rule
These rules essentially define exceptions to a Deny-by-Default approach

### 14.5 Enterprise point of presence
The point of presence (POP) is the point at which an enterprise connects to its internet service. There might be multiple points, or alternatively a single point through which all traffic flows. 

#### The demilitarized zone (DMZ)
Sigh
Will 2023 be the year that IT people stop thinking of themselves as soliders? Almost certainly fucking not.

A DMZ is a de-militarised area between two conflicting nations. It's used here to describe a segment of the [[LAN]] where [[Internet]]-visible servers live. These servers face higher threat than the servers on the internal LAN, and should be treated with appropriate caution.

#### Intrusion detection system (IDS)
These systems look for patterns in traffic, both inbound and outbound, that may indicate an attack or a compromise. It then reports these, most likely via a [[security information and event management|SIEM]]. These [[indicators of compromise]] can be rolled out like firewall rules to an intrusion prevention system. These systems are naturally vulnerable to false positives, where user behaviour is mistaken for an attack.

#### Intrusion prevention systems (IPS)
A slightly more advanced IDS,  an IPS identifies an intrusion and then automatically applies measures to contain it. For example, by blocking outbound traffic to the [[Command and Control]] centre for an attack.

#### Data loss prevention systems
You can also buy software that promises data loss prevention, usually by analysing traffic, but also sometimes through inventorying data assets

#### 14.5.1 POP topology
Some approaches:
1. Single firewall
2. Bastion host
3. three-legged firewall (sigh)
4. dual firewalls
Let's take them in turn

#### Single firewall
One firewall. One way in. One way out. Tight control, but it's going to be a gigantic pain in the ass to maintain.

#### Bastion host
A slightly older technique, whereby a strongly hardened host called a 'bastion' (sigh) provides Internet services. A separate firewall protects the internal enterprise network from internet based attacks. The bastion server has to be very carefully configured.

#### Three-legged firewall
The three-legged firewall uses a single device which provides three connections: to the ISP, to the internal enterprise network, and to a separate DMZ.
All inbound traffic is allowed to reach the DMZ hosts, but is blocked from making inbound connections to the internal network. Outbound connections can go to the the DMZ or out to the [[Internet]]. 
Because the firewall controls access between all three networks, it can also restrict administrative access to the DMZ. The firewall can restrict or block network management protocols (what?) from moving between the internet and the DMZ, and only exchange management protocols with the internal network.
However, given that much administration now happens over HTTP, HTTP traffic has to be allowed into the DMZ from the Internet

#### Dual firewalls
One firewall protects the entire enterprise, filtering traffic to the DMZ. The second firewall protects the internal network. It's very similar to the three-legged firewall approach above. However, it's more performant. Some people argue that the two firewalls should be of different brands, giving [[defense in depth]]. However, managing these in sync so that they don't clash is a real challenge.

#### 14.5.2 Attacking an enterprise site
##### Protocol attacks
- an attack might use IP spoofing to fool a firewall: that is, the source IP addresses appear to be internal to the network 
- the attacker streamed a long series of SYN and ACK packets at the victim's machine, trying to guess TCP sequence numbers. they were eventually successful
- in short, protocols can be attacked by making the protocol behave in unexpected ways
##### Tunneling
- if you're blocking/allowing based on a port/application, and not looking at the actual data, there's a danger tunneling is being used
- for example, if a firewall sees port 80 is in use and assumes "web", it may be wrong.  There's actually no restriction on applications using port 80
- worse still, if someone's using SSL, even the application data can't be viewed
##### National firewalls
- See [[China]]'s Golden Shield project
- An attempt by a nation-state to protect their citizens from the harms of the [[Internet]]
- users might get round this by SSL-ing to a proxy overseas...
- which the admins will try to block: technically by blocking connections to those IP addresses, and socially by throwing those people into re-education camps
#### 15.4.3 The challenge of real-time media
- providing audio and video simultaneously is very tricky
- it's not about perfect data transmission, but ensuring that the timings always work. That is, a couple of seconds of glitchy video/audio is better than audio and video not syncing, or pausing altogether
- we try not to use [[Transmission Control Protocol|TCP]] for this - instead, the [[IETF]] developed the Real-Time Protocol (RTP) to support these needs
- securing packets via this protocol is a moving target