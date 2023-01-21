## Learning objectives
- Explain the challenges of network security
- Define key terms of computer networks
- Describe the different network layers

## Reading:
- [[Computer networks]] chapter 1 - 1.2
- [[Computer networks]] chapter 1.3-1.5
- [The command line for beginners](https://ubuntu.com/tutorials/command-line-for-beginners#1-overview)
## Lesson 1.0
- read the [[CYM050-Networks-and-Infrastructure-Security-syllabus.pdf|syllabus]]
## Lesson 1.1
- this is interesting. Guido proposes a different lens on [[attacker|threat actor]] and introduces [[threat model]].
- he points out that depending on the thread model we're considering, 'attacker' and 'defender' may be the same entity. For example: social media networks that invade our privacy (attacker), and social media networks securing the messages we send to our lovers on the platform (defender).
- consider a network that is controlled by an [[attacker|adversary]]. We can maintain [[integrity]] and [[confidentiality]] through [[cryptography]],  but can we achieve the final leg of the [[CIA triad]] and retain [[availability]]? No, of course not: the adversary will be more than capable of blocking every message. This model is therefore not completely useful, because in reality the only advice we can give is "try not to be in such a network"
	- (and if you are, never never _never_ never never link your true identity with your network identity)
- Therefore let us weaken this theoretical attacker to one that collects and stores every message, but does not actively seek to disrupt all communications. However, it may still target some communications. How can we maintain availability, given that requirement?
### Adversaries in a network
A #criticalThinking exercise

**Purpose:** Reflect on the attacker’s perspective.

**Task:** Think of a particular company’s computer network. Assume that you are an adversary. Find one or two good scenarios (from literature or your imagination) for attacks considering the following points:

- What are the possible targets for an adversary in this network? 
- What kind of adversary could try to attack these targets? 
- How does the type of adversary influence its chances of success?

**Answer**
Case one: ransomware operator

The targets for this adversary will be any machine that stores data that the company needs access to. This will include proxies, such as credentials to gain access to backups. The kind of adversary we're looking at is a ransomware operator - a criminal organisation with a fairly restricted set of skills. The chances of success are high in the case of unpatched devices, and very low in the context of an organisation with a decent level of cyber-hygiene.

Case two: espionage with a view to blackmail

In this case, an attacker would squat on the network and try to read decrypted messages. The targets are therefore likely to be email servers or end-user devices, where messages are decrypted at rest. The kind of adversary attempting this is likely to be at the more advanced end of the spectrum, as this will be a custom job, involving scoping the network, planning ingress and exfiltration, and masking their presence. To that end, they may well be successful - however, it is also highly unlikely that any of us will experience such an adversary in our day-to-day lives.

### The 'tin can' telephone network
This is a #thoughtExperiment
A tin can telephone is a point-to-point communications service. Let us first consider the operators in the network. How do they know when the communication is over and it's their turn to speak? They could use in-band or out-of-band signals. Out-of-band signals might be a small flag that one operator waves when they've finished speaking. In-band signals might be a word with specific significance. For [[NATO]], the word is "OVER". There are several other keywords, or [procedure words](https://en.wikipedia.org/wiki/Procedure_word), to indicate different signals. We might also want to include the sender and the receiver - again, note NATO's procedure words.
Suppose, however, that we want to connect two tin-can telephones. Or more! But now we run into a new problem. Remember that the tin-can telephone is point-to-point. So how do we communicate with someone who is not in our immediate network? Putting an address on our message will help. Being friends with all the operators in the neighbourhood will also be important, as we'll need to be able to trust them. In fact, even if we trust them, maybe we should encrypt the message - just in case. However, we'll need to leave the address unencrypted - so there's a risk that someone will know I'm communicating with someone else, even if they don't know the contents of the message.
In this way, if an operator receives a message that's not for someone in their network, they can forward it onwards. Before long we will need to address how we organise permission to speak across this vast network of simultaneously communicating nodes.

### Higher network layers
In order to connect networks together, we need a way to route packets through them. This is done through the [[Internet Protocol]] protocol. However, [[Internet Protocol]] only works across devices. What if we need to connect to a specific application running on a device, or even a specific part of an application? This is where the [[Transport Layer]] comes in. There are two key protocols used in the transport layer@ the [[Transmission Control Protocol]] and the [[User Datagram Protocol]], UDP. Both introduce the idea of ports, which address sockets, which are the interfaces to applications running on devices.