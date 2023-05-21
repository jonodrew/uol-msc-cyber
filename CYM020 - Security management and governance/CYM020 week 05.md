This week concerns how security management can be used to address and respond to security incidents through a range of techniques. This includes engaging with [[ISO 27035]] to develop a pragmatic response to risk management. This includes how to identify and prioritise incidents, their planning and preparation, responding to incidents as well as learning and assessing from (inevitable) incidents that organisations encounter.

### Learning Objectives

---

- Compare different incident response actions according to an organisation’s needs
- Assess how to report incidents and effective mechanisms for building resilience for an organisation
- Describe and identify what an incident is and how to prioritise them

## reading
- F-Secure, [Incident response: Cyber Security Crash Course](https://www.youtube.com/watch?v=eeQ2WpdvG0g "Cyber Security Crash Course")
- [[Information Security Management#Chapter 2: Information security departments and roles#section 5: cybersecurity incident incidents]]
- [[NIST SP 800-61]], Executive Summary and [[NIST SP 800-61#Chapter 2: Organizing a computer security incident response capability#Events and incidents|2.1]]
- [[ISO 27035-2|ISO/IEC 27035-2]], section 4 and Annex B

## Lesson 1: What is an [[incident]]?
- this area of cyber is not as exciting as you'd think
- it's much more about documentation, playbooks, practicing, and basically making the whole thing boring and predictable
- everyone is going to face security incidents
	- everyone!

>[!question] In one sentence, what is an information security [[incident]]?
>
>An event, or sequence of events, that could cause harm to an organisation

- 'could' is very important here, because it (correctly IMO) defines an 'near miss' as an incident itself. There is no such thing as a 'near miss' - there are only incidents, and their varying impacts
- couple of definitions here:
>[!quote] An information security incident is 'one of multiple related and identified information security events that can harm an organisation's assets or compromise its operations'
>
>\- [[ISO 27035-1]], Clause 3.4

>[!quote] ...a violation of imminent threat of violation of computer security policies, acceptable use polices, or standard security practices
>
>\- [[NIST SP 800-61]], Section 2.1

- we should collect events and try to identify patterns - this is where a [[security information and event management|SIEM]] tool comes in handy
- Case study time! A fictitious company called "Automotive Components Ltd"
	- Take a guess at what they make. Go on. Guess. Bet you can't.
- Is SME-sized, with 90 employees across manual and intellectual labour
	- remember kids, manual and intellectual labour is still Labour, and has more in common with each other than not!
- the entire IT department is two people, and of those only one (Kay) has responsiobility for information security management and governance
- We're going to step through [[ISO 27035]], and see how we can apply it to a smaller organisation
- Step 1: planning and preparation. If nothing else, an information security incident management policy must be produced. It must have buy-in and support from senior management. Updates should be regularly applied
	- I _really_ don't like this framing. The production of policy absent implementation and training doesn't help anyone - it's just words
- Tasks may need to be assigned out across the organisation
- Since Automotive Components Ltd has both information technology and operational technology in the factory, the [[attack surface]] is large and complex
>[!question] Should Kay be the only person responsible for a plan for incident management and response?
>
>lol no

- Kay does not have the finances to contract out the incident response team, nor does he have the people internally with the appropriate skills
	- Kay apparently uses he/him and they/them pronouns, which we love
- As a result, Kay has to rely on off the shelf consumer products
>[!question] What external assistance may KAy require if there were to be a ransomware incident at Automative Components Ltd? Remember that all servers are on-site
>
>Kay would need a [[Bitcoin]] vendor, because Kay is a bit stuck. At the very least, Kay will need to contract a supplier with expertise in digital forensics, who may be able to identify ff the [[attacker]] has used a previously broken ransomware tool. If so, they may still be able to recover the company's data. They'll also need to contact law inforcement, to report the crime; the [[Information Commissioner’s Office|ICO]], because if the criminal has enough access to encrypt the files they may well have also exfiltrated them; and they might also lean on the UK's [[National Cyber Security Centre|NCSC]] for support.

## Lesson 2: Incident preparation
>[!quote] The organisation shall plan and prepare for managing information security incidents by defining, etablishing, and communicating information security incident management processes, roles, and responsibilities
>
>\- [[ISO 27002|ISO/IEC 27002]], Clause 5.24

- prepare for failure!
- deep dive on [[ISO 27035-2]]
- the mention of principles and trust in 27035 has me returning to trust as the fundamental underpinning of these systems - because you've got to trust that your colleagues understand the intent and principles
	- zero-trust system here are where folks rules-lawyer the policy, vs understanding the 'spirit' of the rule
- the example reports in [[ISO 27035-2#Annex B: Example forms for information security events, incidents, and vulnerability reports]] look really, really useful!
>[!question] 'The standard processes of incident planning only work for large organisations with large IT security teams and budgets'. Discuss
>
>I would argue that, in fact, the standard processes of incident planning work better in small and medium sized enterprises. Much of the planning work (putting aside the response, for the moment) demands that the whole organisation understands: the purpose of the incident management policy; their actions under it; who is responsible. It also requires buy-in from management at every level - which, from experience, is easier when there's not very many levels!
>
>That is not to say that the process can be complex. Additionally, in a large organisation the supporting functions are likely to be more mature and therefore able to support. Without a clear steer from risk management on the [[risk appetite]] of the organisation, how can we outline the scope of the policy? There is also a risk, in an SME, that this policy is seen as obstructive and against the principles of the organisation. 

>[!quote] \[cyber resilience is] a measure of how readily a system can persist in a changing environment
>
>\- [[National Cyber Security Centre|NCSC]]

>[!question] Why has cyber resilience been promoted?
>
>'Resilience' as a concept is part of a wider shift across industries to examine and understand complex systems and behviours. We are starting to understand that the goal is not 'zero incidents' but low time-to-recover (TTR) and low impact
>
>These complex systems are an emergent property of systems that are more connected and less inside our control. Consequently, we can no longer build walls around 'our network', because it no longer exists
>
>There is also a growing understanding that, because of this complexity, the [[information security management system|ISMS]] will always fail in some way. This is because the ISMS works on a model of our system, and the model is always inaccurate.
>
>Finally: resilience allows us to adapt to changing environments, rather than getting stuck in one place

- if we don't test our plans, we are not resilient. We're just optimistic
- tests might be:
	- validating plans (how??)
	- training folks
	- testing processes and procedures
- approaches, in increasing order of realism:
	- discussion based exercises
	- [tabletop exercises](https://www.youtube.com/watch?v=CryNV8V-ZDU)
	- live exercises (chaos engineering!!)
- regularity of these approaches will be proportional to their realism, and therefore cost (though perhaps there's an argument for chaos engineering and making live exercises more common)
	- these exercises should be run when the environment changes
		- so all the time, then?

## Lesson 3: Incident response
- we're going to be looking at [[ISO 27035-3]]
>[!question] What three different potential sources of data may be used in information security incident management to build mechanisms to monitor security controls?
>
>- events, collected by a [[security information and event management|SIEM]] tool
>- reports from users
>- public, [[open-source intelligence|OSINT]] sources
>- information sharing partnerships, from [[Five Eyes]] all the way down to professional colleagues

- situational awareness is the first step
	- cf. [[OODA]]
- Our iterative process should be:
	- decide how much we trust the data
	- identify the requirements
	- choose sensors and types of data collection
	- proactively monitor these sensors
	- create procedures for the occasions when the data shows deviation from an acceptable baseline
	- develop systems to store and retrieve information

>[!question] A phishing email has been sent to Automotive Components Ltd! 
>
>- How might the SME use a combination of proactive and reactive measures to identify events?
>- what is the likely cause of an incident?
>  
>The likely cause of an incident will be a complex failure of a number of things, and if you say "ew users are the problem" I will hit you with a lettuce, so there.
>
>The likely cause of an incident will be, in no particular order:
>- the system not identifying phishing language in an email
>- someone senior in security purposefully phishing their colleagues, which in my opinion should be a fireable offence
>- [[DMARC]] not being correctly applied, allowing email that appears to be from the organisation's domain
>- [[DNS]] records not being correctly handled, allowing an [[attacker]] to take over one of your domains
>- the firewall not blocking a connection to a questionable domain
>- the authentication system not using a second factor
>- the finance team being too tight to pony up for hardware second factors

