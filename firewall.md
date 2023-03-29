A block or filter on ingress and egress to a [[network]]. It should filter traffic, allowing only authorised traffic in either direction

The firewall itself should be hardened against attack, probably with a specifically-designed secure [[operating system]].

There are various approaches to filtering data, like [[application filtering]] and [[packet filtering]]. Other controls might be #behavioural like 'network activity'.

## Capabilities
It's worth noting that some of these capabilities are disputed. Notes are provided where this is the case.
1. [[Network Security Essentials]] claims that the firewall defines a single choke point. While it's true that this massively simplifies security management, it's also worth noting that this is a very old fashioned approach. Modern approaches, such as [[zero-trust architecture]], do not operate on this "inside good, outside bad" mode of security
2. A firewall is a useful place to put security monitoring, as it should be hardened against attack
3. It's also where one can generally find the [[network address translator]], and anything doing auditing
4. Finally, a firewall can be the platform for [[Internet Protocol Security|IPsec]]. 

## Threats/[[attack]]
- [[insider]] attacks
- attacks on the firewall software - remember to patch with frequency
- [[Internet Protocol|IP]] fragmentation attacks
	- put malicious code in packets that aren't the first - firewalls sometimes only examine the first packet
	- fragments that are impossible to reassemble - like the apocraphyl tale of releasing sheep marked 1, 2, 3, and 5 around the university

## Application level proxies
Positioned as a kind of [[reference monitor]] at [[application layer|layer 7]], the application level proxy acts as server and client. That is, the proxy acts as the server to the internal request, validating that it's acceptable according to the firewall rules. It then forwards that request on, if appropriate, acting as the client to the actual requested server. The same happens in reverse. Thus, like a reference monitor, it acts as a [[Computer security#Controlled invocation|controlled invocation]]. Naturally they are quite expensive, and so only tend to be run on [[system hardening|hardened systems]].