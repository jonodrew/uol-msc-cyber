This week is concerned about the integration of different people and communities into security management. It looks at a range of components ranging from trust to security awareness training to demonstrate why the management of people is a core element to a successful information security management system. The week concludes by asking what people-centric security might enable for an organisation and how such a change of perspective can be beneficial to security management.

### Learning Objectives

---

- Develop an appreciation of the different types of people and how to manage competing interests in an [[information security management system|ISMS]]
- Identify and implement different controls for the management of people in organisations
- Evaluate the impact of integration of people-centric security into an ISMS

## reading
- [[Walking the line - The everyday security ties that bind]]
- [[Information security management principles#Chapter 5: Procedural and people control security controls]]
- [Cyber security: a practitioner's guide](https://www.vlebooks.com/vleweb/product/openreader?id=WORLDWIDE&accId=9116556&isbn=9781780175973)
- [[Trust - an element of information security]]

## Lesson 1: why focus on people?
>[!question] Choose one [[control]] you have studied in the past three weeks and describe how people are important \[within it]
>
>There are only 8 controls in the [[ISO 27002#People|people family of security controls in ISO 27002]]. However, many controls that are not specifically about people involve people. As a very small example, consider controls around password complexity. The user should be able to remember the password and be able to differentiate it from other passwords they know. This is no small task!

>[!question] Identify five ways in which people's lived experience will differ, and what consequences that will have on security management
>
>1. Age: people from different generations fundamentally perceive risk and threat differently. For example, there is a generational difference in how much information people put online about themselves
> 2. Gender: Women are aware of the risks of loss of confidentiality more accutely than men. They are more often targeted for stalking and harassment, and consequently their understanding of risk is generally richer and more nuanced
> 3. Social class: controls that require a dedicated workspace may not be feasible for people in shared housing
> 4. Technical literacy: the variation in technical skills across the workforce should be considered when implementing controls
> 5. Disability status: certain controls, if poorly designed, assume people have the full use of (for example) both hands and excellent eyesight

We might additionally consider educational achievement, level of (local language), and work status

🚨 SECURITY IS A SOCIO-TECHNICAL SYSTEM 🚨

Introduction of the concept of [[positive security]]

>[!question] In what cases may two-factor authentication not be appropriate?
>
>In general, a second factor will introduce friction amongst people who can't access that second factor. For example, consider the case of benefits claimants in the UK. On the one hand, the organisation has a responsibility and a need to ensure that only the authorised recipient can access state funds. However, people who are seeking support from the State may not have access to a second factor, and would therefore be excluded from accessing these funds

>[!question] Do you think that the concepts of positive and negative security are more suited to different security controls?
>
>To restate the concepts, positive and negative security can be thought of as 'freedom to' and 'freedom from' respectively. That is, a username and password combination gives a user negative security: security from impersonation. However, it doesn't grant any positive security: it doesn't enable them to better reach their goals.
>
>A control such as an automated spam filter might be a positive security control: it accords users the freedom to do their work without distractions and potentially malicious emails flooding their inbox.

## Lesson 2: Managing people
>[!quote] Various different security controls produce different outcomes that may or may not be favourable to the organisation and people we are seeking to secure
- it is tempting to see 'staff' as a single, homeogenous group - that both have to be protected from outside threats, their own mistakes, and the ill intentions of the one or two malicious actors among them
	- we must avoid this temptation, as it's unhelpful in terms of good security outcomes
- A restatement of the need for [[ISO 27001#Leadership|leadership, as stated in 27001]]
- Documentation is at the core of security management, apparently
- To make the interface to security easier, we need:
	- buy in from the top
	- clear documentation
	- a deep understanding of how poeople communicate with the security team, and the experiences they bring (and the experience of interacting with the team)
	- a consideration of how different groups of people will be affected by security controls
	- a selective application of controls, assessed against how well they align with the organisation's broader aims and objectives
>[!question] What methods, other than documents, could you use to present acceptable use policies to staff?
>
>Acceptable use policies could be documented as a video, or as posters around the organisation (if the policy is simple enough). 

- training should address the why as well as the what and the how. Without the why, they almost certainly won't bother
	- cf. [[Drive]] and the need for people to understand what they're doing

>[!question] Do people management security controls simply pass on the responsibility to employees who do not understand information security?
>
>To a certain extent, yes. In an ideal world, these controls would empower our users to take responsibility. However, generally speaking, they do not. Security awareness training is seen as a necessary chore that can be slept through. Acceptable use policies are often never read - as a professional in this field, I can give countless examples of people asking why the firewall blocked access to a specific site, even when that site was specifically named in the acceptable use policy as a forbidden site. Thus it seems that the existing controls pass on responsibility, with no check on whether the person has the capability to be responsible.
>
>However, these controls are part of a suite of tools used to manage risk. Is risk truly mitigated if the training is ineffective? I would argue no, and that therefore much risk is retained. And under ISO 27001, risk is managed by the organisation. Therefore I find that there is a moral duty to improve staff understanding of information security, before giving them these responsibilities - but also a duty when creating our ISMS that the controls are as good as they can be. If you wouldn't use a [[Caesar cipher]] on your production database, why would you use the equivalent when training your people?

## Lesson 3: building trust
### Why is trust important?
- OED definition klaxon!
- trust is unquantifiable and also essential to effective management, both in terms of security and also in terms of *everything else*
- let us consider two definitions of trust: the social and the technical
	- social: the belief that something will happen in the same way it happened previously, based on one's own prior experience of the context of previous event
		- weird definition
	- I didn't notice a definition of technical trust
- ahah, [[zero-trust architecture]]!
- the thorny question of [[insider|insider threat]]
	- monitoring every employee's every action will ensure that no employee has the chance to become an insider
	- ...but also that there will be no employees
	- monitoring has its limits, too: consider the case of [[Edward Snowden]] and [[Chelsea Manning]]. These were both people under surveillance by their employers, and yet entirely capable of leaking classified information
		- is there an [[MSc project ideas|idea]] there?
	- 
