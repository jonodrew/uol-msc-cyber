---
alias@: [IRT]
---
>[!quote] a capability set up for the purpose of assisting in responding to computer security-related [[incident|incidents]]
>
>\- [[NIST SP 800-61]], Appendix C

>[!quote] \[a computer security incident response team] consists of the people who handle the response to an incident. It may include internal and external teams, and may differ based on the nature of the incident
>
>\- [[National Cyber Security Centre|NCSC]]

These are very broad descriptions. Let us compare to [[Computer Emergency Response Team]] and [[Security Operations Center]]. A CERT is a very particular form of response. CERTs tend to focus on improving incident response more generally, for example across an industry or country. SOCs are not usually tasked with response.

An IRT is therefore a specific team within an organisation. It is sensitive to the local context, the industry's threat environment, and the organisation's [[risk appetite]].

[[ISO 27035-2]] provides guidance on how IRTs can be set up and integrated.

- single type: A 1:1 IRT <-> organisation mapping
- hierarchical type: an organisation has multiple IRTs, generally overseen by a coordinating IRT. These IRTs have different focuses
- remote type: an IRT that's outsourced and remote from the organisation, that's still able to monitor for threats and events via the [[Internet]]
>[!question] What should a small/medium sized enterprise consider before outsourcing their IRT to a third party external contractor?
>
>They should consider:
>- what risk they still carry, and what new risks are introduced. Recent stories about [Capita leaving open buckets on the Internet](https://www.theregister.com/2023/05/17/another_security_calamity_for_capita/) emphasise the importance of conducting thorough research on partners in this space. Additionally, the intrusion onto their network by a third party opens a significant risk 
>- what coverage they'll get for their money - is it 24/365 or more 9-5?
>- what actually happens during an incident?

Taylor et al in [[Information security management principles#Chapter 3: Information security framework#Security incident management|Information security management principles]] point out that members of an IRT should be competent enough to make good decisions, and endowed with enough authority to implement them immediately. They also note that the IRT should have a good understanding of their local legal requirements for reporting, and how to capture information that meets the standard required for that legal process.