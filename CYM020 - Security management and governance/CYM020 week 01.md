This preliminary week introduces key concepts that are developed further in the remainder of the module, including an understanding of what an [[information security management system]] is and the role it plays in Cyber Security Management (CSM) within an organisation. The key standards-setting bodies are introduced, as are key notions such as security threat, security risk and security control. Finally, the role of people in ensuring cyber security is highlighted.

### Learning Objectives

---

-   Define the role of an [[information security management system]] within an organisation
-   Explain the key role played by people in Cyber Security Management
-   Identify security [[threat|threats]] and [[risk|risks]]
-   Describe the role of #standard within Cyber Security Management

## Readings
Books for this course are:
- [[Information security management principles]]
- [[Cyber Security (A Practitioner's Guide)]]
- [[Information Security Management]]

## Lesson 1: What is cyber security management?
- oh hey, it's [[Chris Mitchell]]
- it's about reducing the [[impact]] of [[attack|attacks]]
- Cyber security management is about managing the [[security controls]] that should protect against attacks. There are:
	- technical
	- procedural (security policies, vetting, logging, auditing)
- 'people are the foundation on which cyber security is built' 
- for our purposes, cyber security means maintaining the [[confidentiality]], [[integrity]], and [[availability]] of information (the so-called [[CIA triad]])
- we don't do this for fun, but for the sake of the organisation (which means taking a risk/reward based approach to security!)
- just because everyone knows the basics, doesn't mean we can wave away the need for proper, systematic management

>[!question] What's the first thing to consider when developing a systematic approach to cybersecurity?
>You must understand:
>- the [[risk]] to the organisation
>- the kind of [[threat]]
>- the [[risk appetite]] of the organisation

- Before we can assess risk to assets, we need to understand what the [[asset|assets]] actually are. Chris argues that all assets should have an asset owner. This is a good thing to aim for, but 'asset' is a very fuzzy term and consequently finding an owner for each broadly defined thing is difficult.
- Your [[information security management system|ISMS]] should be a dynamic, 'living' document that's updated when the threat landscape changes.
>[!question] To what extent do you agree or disagree with the following statement?
>
>To ensure the CIA of information assets it is typically necessary to implement a wide range of security controls. Selection, implementation and ongoing configuration and management of these controls typically requires detailed technical knowledge. As a result, and bearing in mind that many threats arise from issues relating to software, it is essential that **all** members of staff with responsibility for cyber security have a detailed understanding of information technology and security, including extensive programming experience.

This statement is provocative. First, let's consider who has responsibility for 'cyber security'. The answer might well be everyone. Even the least-technical member of staff is responsible for reporting [[phishing attacks]] and _not_ plugging random USB devices into their machines. Alternatively, the only person really responsible for cyber-security is the CEO or equivalent - and they probably don't have a technical background. The Board will probably agree that it's not necessary?

So what's the answer? Simple. Cyber-security is everyone's responsibility, and for a select group of people it's their full-time job. That job is advancing, improving, and shifting security so that's it becomes a utility.

### reading
- [[Information security management principles#Chapter one: Information security principles]] 

## Lesson 2: #standard and cyber security
- In [[International Standards Organisation|ISO]] standards:
	- 'shall' means "required for compliance with the standard"
	- "should" means "recommended but not required for compliance with the standard"

### reading
- [[Information security management principles#Chapter 3]]

### *de facto* and *de jure* standards
>[!fail] If you're wondering, indiscriminate use of Latin is a sure sign of an insecure industry that needs to prove how clever it is

*de facto* standards are standards that are bottom-up; that is, they are used because they are useful, or because the biggest player in the market uses them and everyone follows suit. *de jure* standards, by contrast, come from 'official' (for some value of official) bodies. *de facto* standards can become *de jure* if someone official decides to give the standard an 'official' mark of approval

>[!question] Should standards be public and freely available?
>Yes!
>
>Unfortunately, because [[International Standards Organisation|ISO]] makes most of its money from selling access to the standards, this is unlikely to happen any time soon

A quick segue into [[RFC]], which is a process for making bottom-up, *de facto* standards. These standards dictate how large parts of the [[Internet]] are run.

>[!question] Compliance with a security framework standard like ISO/IEC 27001 undoubtedly involves the generation of a lot of documentation. Some people regard this as a waste of time, and argue that the time spent on documenting procedures, risk assessments, etc., would be better spent on actually doing things. Please take a few minutes to think about this and write down your response.
>
>The question proposes a false binary, as both are unhelpful. An organisation that spends all of its time generating documentation, conducting risk assessements, etc, is not more secure than one that has not. Indeed, it may be less secure: people have a tendency to view the act of writing something down as equivalent to enacting it. 
>
>However, an organisation that charges around, securing things but never documenting what it's done or why is equally probably less secure than it was. If colleagues don't understand the reasoning, or can't find it in an emergency, they will not understand what actions to take. 
>
>In short, documentation should be proportionate to action, and actions should be documented.

## Lesson 3: Security [[threat|threats]], [[risk|risks]], and [[control|controls]]
#### 3.1: [[threat]] and [[risk]]
A threat stands in opposition to our attempts to maintain the [[CIA triad]]. That is, a threat might:
- read without [[authorisation]], threatening [[confidentiality]]
- write without [[authorisation]], threating [[integrity]]
- reduce [[availability]] of data. They might do this through deleting the data, encrypting the data (cf. [[ransomware]]), or by overwhelming a system (cf. [[Denial of Service|DoS]] )

>[!question] Is there anything missing here?
>
>Some might argue that [[accountability]] is not included in this definition

However, [[Chris Mitchell]] argues (and I agree) that accountability is a system function and not a security function. As security professionals, we are concerned with ensuring that function is available and its integrity is not compromised - but it's not our concern who did what.

On the other hand, a security function that doesn't care about [[accountability]] or [[non-repudiation]] is going to struggle to be useful. These functions are only valuable if we don't maintain [[CIA triad|CIA]] - but by contrast, one of the necessary elements of building [[resilience]] in a system is accepting that we'll never maintain a perfect CIA. So maybe we should be accepting that cybersecurity has a wider scope than just CIA.

### [[control|security control]]


#### reading
- [[Information security management principles#Chapter 2]] pp19-38
- [[Information security management principles#Chapter 5]] pp. 102-117

## Lesson 4: Isn't it all about people?
- We talk about [[authentication]] and [[authorisation]] mechanisms
	- with authorisation we segue into multifactor authentication and [[biometrics]]
- then technological controls like 'groups' - cf. [[roles-based access control]] and [[access control]] 
- then access points, and the relative merits of hardlines, wireless network within the [[network]] perimiter, and remote access (likely via a [[virtual private network|VPN]])
- then data protection, noting the procedural control of 'classification'
	- Oooh, this is my chance to show you [Jon Snow taking us through the new levels of security classification](https://www.youtube.com/watch?v=gHGP4ikjIp8)
	- We also note that the US includes confidential, restricred, protected, and unclassified
	- commercial organisations may use terms like public, internal, confidential, and highly confidential
- We touch on need-to-know, but this time there's nuance in acknowledging that sometimes you don't know ahead of time who needs to know
	- it all comes back to [[risk appetite]]!
- 