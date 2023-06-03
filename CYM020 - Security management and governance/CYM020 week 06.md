This week concerns how to maintain business continuity at times of disruption and how it is essential to maintain and build continuous resilience as part of security management. To do so, the week will explore how to plan for business continuity by engaging with [[ISO 27031]] , disaster recovery processes, as well as testing and organising different external and internalctors. The week concludes by an explicit attention to developing cyber resilience and continuous improvement as part of business continuity.

### Learning Objectives

---

- Summarise the role of disaster recovery planning and processes for business continuity
- Recognise the importance of cyber resilience and continuous improvement for continuity and disaster recovery in an [[information security management system|ISMS]]
- Create a business continuity plan and select appropriate controls and methods for their implementation

## Readings
- [[The tensions of cyber-resilience - from sensemaking to practice]]
- [[Information security management principles#Chapter 8: Disaster recovery and business continuity management]] pp.177-88
- all of [[ISO 27031|ISO/IEC 27031]]

## Lesson 1: What is [[resilience]]?

### Is incident management not cyber resilience?
- QTWTAIN
- As of 2023, the [[EU]] is developing a cyber resilience act, with a view to improving its resilience to supply chain shocks
- given cyber resilience relies on resilient supply chains, being resilient requires everyone to become better
	- does this map to the internals of an organistion, and a broader positive security culture?
- cyber resilience cannot be built alone!
- redundancy is useful in resilience, because it offers the chance to failover without impacting a service
	- however, redundancy - both of people and resources - is expensive
- there is no one meaning to 'cyber resilience', but we agree that it's not the same as security
	- _awesome_
- cyber resilience is a poly (many) semic (meaning) word: nobody can agree and everyone reckons they know
	- acceptance of unknowable (black swan) events
	- robustness in the face of adversary
	- it could be expanded to a broader sense that includes the people and socio-technical systems
- lecturer suggests that resilience differs from security in that security offers 'concrete processes, [[control|controls]], and procedures to address [[vulnerability|vulnerabilities]]', while resilience is for when threats can come from unexpected places
	- hm
- cyber resilience means stepping outside of the traditional bounds of the IT team into the running of the wider organisation, which isn't always appreciated
- cyber resilience: not about enumerating every risk, but being prepared to deal with most threats

>[!note] ION Group
>
>- ION was impacted by the [[ransomware]] [[attacker|threat actor]] [[LockBit]]
>- they provide essential computing systems to automate derivative trading, which is like gambling
>- the impact of this [[attack]] was that market regulators, and others, were unable to produce weekly trading reports
>- thus, in a networked world, resilience is essential for the wider sector
>- vaccinations aren't just for you

>[!question] Is cyber resilience just a new ‘fad’ (or interest) or will it define security management and governance in the next 10 years?
>
>Cyber resilience is a novel idea, though perhaps not as novel as it appears at first glance. Throughout human history, social groups have realised that the resilience of their group is reliant on the actions of everyone in that group, and further, everyone in that group acting (in some capacity) to support the others. Recent experience of a global pandemic gives us some parallels to draw on, and a worrying conclusion
>
>The actions of individuals during the pandemic were not solely for themselves. Instead, people acted in ways that improved the resilience of the wider society, even though it required some sacrifice on their part. It is clear that, through a combination of positive messaging and legal pressure, groups of people can be induced to form a more resilient society. 
>
>Cooperation in the face of a deadly virus, however, isnt' necesarily analogous to an industry - particularly an industry where there is competition. If the bottom line is profit, what does it benefit an organisation to share threat intelligence with its competitors? Of course, as security professionals, and with the experience of the ION group, [[Solarwinds]], and [[Log4j]] we know the answer: because we're all using the same software, and we're all just as vulnerable as each other.
>
>And what of redundancy? We know it's the key to resilience, as it offers a way to 'fail-safe' - a digital crumple zone, if you like. If regulatory bodies can influence industries to invest money into redundancy (without creating a monopoly that would be a juicy target), then we'll all be better off - but that money represents shareholder dividends and higher pay. 
>
>There may be something in this new (old) idea. Cooperation over combat in the competitive arena may be an approach that folks can support. However, given the cost associated with becoming a resilient organisation, I do not believe this idea will be anything more than a fringe hope.

## Lesson 2: what is [[business continuity]]?

- without cyber security, there is no cyber resilience
- business continuity managment aims to ensure that there is a minimal service that can continue to be operated
- [[ISO 27031|ISO/IEC 27031]] is introduced!
	- IRBC is focussed on availability
	- but remember that business continuity is unique to a business!
- Plan -> Do -> Check -> Act
- BCM is an absolutely massive task, and involves actually considering what your core offering is and what's required to be able to provide it
- [[ICT readiness for business continuity]] and a new acronym
- the aim is to reduce the gap between the ICT capability and the wider [[business continuity]] plan
- lean supply chains reduce storage costs, but are brittle
>[!question] What might we do in an [[ICT readiness for business continuity|IRBC]] plan to assess what is critical?
>
> - Examine the [[business impact assessement|BIA]] and look at the dependencies on ICT systems
> - Take part in or lead [[business continuity]] and [[disaster recovery]] exercises
> - speak to users and get a sense of what systems they use, and their importance

- what is the '[[Minimum Business Continuity Objective]]'?
- what is the '[[Recovery Point Objective]]'?
- What is the '[[Recovery Time Objective]]'?
>[!question] Consider the following statement about business continuity management that was partially referenced in the first lecture of this lesson:
>
>>[!quote] Business continuity management (BCM) should prioritise availability over confidentiality and integrity.
>
>Reflect on different organisations and prioritisations and explain why there may be differences, if you think there are. Record your reflection in your study journal.
>
>For most organisation, availability is prioritised over condifidentiality or integrity when considering business continuity. Generally speaking, busines continuity requires that staff are able to access the information and systems that make up the business offering. Confidentiality and integrity of data have no value if the data is maintained if the information is inaccessible, but the business suffers at a time when it cannot afford to. However, even as these parts of the [[CIA triad]] are deprioritised, local regulations must still be followed. Additionally, organisations like government departments, as well as parts of an organisation whose remit is solely either confidential data or data whose integrity can never be questioned, will make a cost-benfit analysis and decide that customer pain is preferable to risking the confidentiality or integrity of the information under their care.
>

## Lesson 3: enabling recovery
- [[business continuity]] is about dealing with the 'known'
>[!question] What constitutes a disaster?
>
>Oh darling, those shoes? *Disaster*
>A disaster is an event that crosses multiple oeprational domains, reducing capacity to near-zero. It throws the operational domain into [[Cynefin#chaos|chaos]]
>
- What is a disaster? Context specific, but we can consider the case of [[Mærsk]], which was hit by [[NotPetya]] in 2017: a [[wiper]] masquerading as [[ransomware]]. There was little network segregation and consequently the attack was across the network within 7 minutes (!)
- the only office not impacted was Ghana which, by a stroke of luck, had suffered a power cut and was offline
- the business took a further nine days to restore systems
>[!question] Identify three critical business processes that Green Accountancy Services (a case study) need to protect
>
>### Context
>Green Accountancy Services:
>- provide accountancy services to 100s of organisations
>- they produce reports for local tax authorities
>- has five offices, which share a network and storage. Both are run from the head office
>	- is the head office one of the five?
>- some of these locations are prone to natural disasters, including earthquakes and flooding
>- Head office is in a large urban area that suffers from significant heatwaves
>- there is little network segregation
>- a team of 4 people manages IT security for this fictional firm
>  
>### Answer
>In order of criticality:
>- the confidential client information that it holds. Therefore, they will be looking at their storage mechanisms. Given that their office is in a location prone to earthquakes one hopes they have off-site backups
>- communication services, including email, to ensure the work can continue being done
>- possibly a failover postal address, as much tax and accountancy work still happens by physical mail

### Activity:
>[!note]
>In this investigative activity, you will produce an abstracted business continuity plan with a business impact analysis using the fictitious case of Green Accountancy Services that we explored in the previous lecture.
>Your investigative task will consist of three steps that should be recorded in your study journal:
>1. You will develop a brief business [[business impact assessement]] (BIA) by creating **your own scenario of an adverse event** (of at least 100 words) and identifying at least two critical ICT functions that may be at risk for [[Green Accountancy Services]] in this case.
>2. Using the business impact analysis, you will **choose three information security controls from [[ISO 27002|ISO/IEC 27002]]:2022** that will be impacted by your chosen scenario (with no more than one from each of the main categories of control: organisational, people, physical and technical).
>3. Using the three identified controls, **develop a business continuity plan for your three selected information security controls** (with at least one point on each security control following Plan-Do-Check-Act in [[ISO 27031|ISO/IEC 27031]]) using your BIA.




