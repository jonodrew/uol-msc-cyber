## Learning objectives
- Demonstrate in practice that networks are insecure by default
- Describe the concept of basic attacks like spoofing
- Explain how data packets are transferred and how receiver and sender can be identified
## Reading
- 4.3 to 4.3.2 in [[Computer networks]]
- Also 5.6 to 5.6.2, up to CIDR
- 5.6.3 up to 'Extension Headers'
- 5.6.4, ARP
## Lesson 1: the [[data link layer]]
- this layer takes care of transferring bits from one device to another. The actual physical mechanics of it are abstracted: it could just as easily be beads on an abacus as pulses of light in a fire-optic cable.
- Let's take as an example [[Ethernet]]
- This layer organises messages into segments called [[Ethernet#Frames|frames]]. It also addresses participants on the physical network, takes care of error correction, and is responsible for collision control and flow control to ensure reliable transmission
- Using Ethernet, a device broadcasts a frame to the network. All devices receive it, but should only process it if their [[MAC address]] matches the one in the frame
- This naturally has...issues
- We don't love the fact that every participant can read every frame
- Ethernet as a protocol works perfectly in a totally closed system where everybody can be trusted
- Modern ethernet is significantly more point-to-point, connecting devices to a kind of device called a 'switch'. This switch serves as a distribution centre for frames, and allows us to connect multiple variants of [[Ethernet]] cables to it.
- This transforms the topology of the network from a bus to a 'star' design. The frames don't change, however. You still send frames with the same format, and you monitor the wire for messages addressed to your MAC address. However, participants are now connected either to one other participant or a switch. So when a switch receives a frame, what does it do with it?
- One approach is flooding: every message is sent on to every participant. Given that some participants are also switches, before long the entire network has been reached. However, this is a very, very inefficient way of routing frames
- Instead, when a switch receives a frame, it stores the sender MAC address for a short time. If it then receives a frame destined for that MAC address, it can forward the frame directly on to that link.
- However, a switch is not a very sophisticated device. An attacker on the network can spoof a known MAC address and in doing so get "copied in" to every frame sent to the intended recipient.
- It should be noted that Ethernet does not guarantee (by itself) [[confidentiality]] or [[integrity]] of data. Nor indeed does it guarantee [[availability]]. An attacker has several options if they wish to deny access to a resource on the network.
	- the [[attacker]] might send frames with a MAC address that doesn't actually exist on the network. This will result in the entire network being flooded. If they keep doing this, the entire network will become congested
	- alternatively, the attacker could conduct a [[Denial of Service|DOS]] attack by sending overwhelming numbers of frames to one specific link
	- finally, there is a risk that two switch ports are connected to each other. This will create a feedback loop where the switch sends frames to itself endlessly
## Lesson 2: the [[Internet Protocol]]
