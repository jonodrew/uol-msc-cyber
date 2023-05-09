## Authors
[[Andy Taylor]], [[David Alexander]], [[Amanda Finch]], [[David Sutton]]

## Chapter 1: [[Information security]] principles
### Concepts and definitions
The definitions below are drawn from [[ISO 27000]]
This adds a new definition of [[confidentiality]], which I've added to that page and inserted below:
![[confidentiality#^a1e10b]]
Stresses the importance of [[need to know]]. 

>[!question]
>How do we balance [[need to know]] with [[Open Government]] and sharing things publicly? 

Then we have the definition of [[integrity]]: ![[integrity#^ab35e7]]
Finally, the last leg of the [[CIA triad]]: [[availability]]. Defined as ![[availability#^529e00]]
>[!INFO]
>There is an endless, pointless, and fundamentally uninteresting debate over the difference between "data" and "information". I've not yet found a single article or book that agrees, internally or externally, with what they mean. In my opinion, this is because they're both: my raw materials are your finished product, and we're both right. 

We also cover [[asset|assets]], [[threat|threats]], [[vulnerability|vulnerabilities]], [[risk|risks]], and [[impact]]. See the linked pages for definitions. We then move on to [[control]]. In the [[information assurance]] context, these are the activities that are taken to manage [[risk|risks]]. See [[control]] for further detail.

Then we look at [[identity]], [[authentication]], and [[authorisation]]

### The [[information security management system]] concepts
If people are going to use the ISMS, they need to be able to understand it - read it, and understand it.

### The need for, and benefits of, [[Information security]]
Securing information:
- is expensive
- makes working with the information more difficult
So why should we bother?

#### As part of a business model
Digital and technology means we can now approve multi-million pound spends with an email. Information assurance gives us the tools to prove that the email is from a legitimate source! In addition, it gives us the tools to protect data - whether it's sensitive customer data, which might have a regulatory cost attached if we lose it, or sensitive internal data, like our commercial plans, which would damage our bottom line if they were leaked.

Remember that some information assets are inside your employees' heads. Consider how best to manage that.

>[!warning] Remember that unlicensed surgery is illegal in most jurisdictions



## Chapter 2: Information [[risk]]
Let's start with a bit more detail on [[threat]], [[vulnerability]], and [[asset]]. Then let's talk about [[impact]].

>[!question]
>Based on what you have learned so far and using the education SME (college) scenario example from our previous reading, consider what we could do as an organisation to minimise our information assets and thus reduce our cyber exposure.

### Model answer
Minimise the data we keep, protect that data, ensure [[confidentiality]] (encrypt data at rest and data in motion), ensure [[integrity]] (data is not altered) and ensure [[availability]] is for authorised individuals and data is destroyed as specified.  Undertake Privacy Impact Assessments (PIA) or Data protection Impact Assessments (DPIA) activities etc. including considerations with respect to cloud computing (if appropriate). 

Maintain good relationship with the [[Information Commissioner’s Office|ICO]] and ensure our data protection officers are trained and processes are robust. 

Ensure good control of access to data and do the best to detect unauthorised access to minimise data exfiltration and response. 

Consider if some data can be securely archived (air-gap) so an online [[attack]] accesses the minimum information. (Note insider threat considerations and also whether you actually need to keep the data or it needs to be securely destroyed.)

Later in the degree course, there is another module on privacy which will provide more depth. There are some key requirements and guidance for the UK from the Information Commissioners Office ([[Information Commissioner’s Office|ICO]]) which provides a depth of information.

- [ICO advice](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/security/)
- [ICO data protection by design](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/accountability-and-governance/data-protection-by-design-and-default/) (note security by design and privacy by design are key considerations)
- [ICO security outcomes](https://ico.org.uk/for-organisations/security-outcomes/)
- [ICO accountability and governance](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/accountability-and-governance/)
- [ICO small business security practical guide](https://ico.org.uk/media/for-organisations/documents/1575/it_security_practical_guide.pdf)
- [ICO accountability framework](https://ico.org.uk/for-organisations/accountability-framework/)
- [ICO use of encryption](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/encryption/)
- [ICO guide to cloud computing](https://ico.org.uk/media/for-organisations/documents/1540/cloud_computing_guidance_for_organisations.pdf)
- [ICO guide for online services](https://ico.org.uk/media/for-organisations/documents/1042221/protecting-personal-data-in-online-services-learning-from-the-mistakes-of-others.pdf)

The next section is [[risk management]], which has its own page.

In terms of threat – is there much we can do to make us less of a target? We can [reduce exposure as identified by NCSC](https://www.ncsc.gov.uk/information/reducing-your-exposure-to-cyber-attack)  where we are effectively investing in our protect, detect and response capabilities.   

Our IT/security team, our employees and students need awareness, training, and overall we need additional security resourcing (staff, equipment and services) and of course better management and governance. Recall from Taylor et al., Chapter 2, that we could make use of cyber insurance as a mechanism to share risk. 

How much will it cost to make our organisation 'significantly above average' in terms of cyber protect, detect and respond/recover?  (And how can we measure this?) In scenario 14, we have identified average threat and information assets, but selected our protect, detect, respond/recover capabilities as significantly above average. That could potentially save circa £400,000 per annum based on one successful cyber-attack according to the HISCOX cyber exposure calculator. 

Note it is a model based on previous data for similar businesses, we might be unlucky and the attackers could have more successful attacks and we have significantly higher losses. We might not save £400,000 per annum, so we are speculating here on what might be.

## Chapter 3: Information security framework
### The information security manager
- A role that's responsible for [[information assurance]]. They are responsible for:
	- co-ordinating IA activities across the enterprise, including those outside the IA function
	- co-ordinating the creation of security policy
	- communicating security information to other employees and users
		- 


### Security standards and procedures
The key standards in the area of information security are in the [[International Standards Organisation|ISO]] 27xxx series. Specifically, there is [[ISO 27001]] and [[ISO 27002]].

There are also standards for securing information technology systems. In the EU, the standard is [[Information Technology Security Evaluation Criteria]]. This scheme has itself been standardised with Canada's [[Canadian Trusted Computer Product Evaluation Criteria]] and the US' [[Trusted Computer System Evaluation Criteria]], producing the [[Common Criteria for Information Technology Security Evaluation Criteria]]


## Chapter 5: Procedural and people [[control|security controls]]
>[!quote] \[...\] the subject of controls is an almost bottomless pit
>
>\- Taylor et al.

### People security
>[!quote] the most sophisticated information assurance system on the planet is worthless if the people, whose data it is designed to protect, are not security conscious

The text refers to a "positive security culture", which I think should be read as "a security culture that is positive", and not as "a culture of [[positive security]]"

### training and awareness
- try not be sidetracked by what seems cool at the moment. Instead, focus on your actual [[attack surface]]
- run your internal culture change campaign the same way professionals run behaviour change campaigns
- make sure senior people are seen to care about this stuff
- Different formats of information will work differently, and variety is important and helpful
- Please don't use [[phishing attacks]] against your own staff (personal, very strongly held opinion)
- [Here's an interesting article a classmate shared](https://www.philvenables.com/post/people-and-security-incentives)
- 
