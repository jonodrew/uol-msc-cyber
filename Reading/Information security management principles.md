## Authors
[[Andy Taylor]], [[David Alexander]], [[Amanda Finch]], [[David Sutton]]

## Chapter one: [[Information security]] principles
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

### The need for, and benefits of, [[Information security]]

## Chapter 2

>[!question]
>Based on what you have learned so far and using the education SME (college) scenario example from our previous reading, consider what we could do as an organisation to minimise our information assets and thus reduce our cyber exposure.

### Model answer
Minimise the data we keep, protect that data, ensure confidentiality (encrypt data at rest and data in motion), ensure integrity (data is not altered) and ensure availability is for authorised individuals and data is destroyed as specified.  Undertake Privacy Impact Assessments (PIA) or Data protection Impact Assessments (DPIA) activities etc. including considerations with respect to cloud computing (if appropriate). 

Maintain good relationship with the ICO and ensure our data protection officers are trained and processes are robust. 

Ensure good control of access to data and do the best to detect unauthorised access to minimise data exfiltration and response. 

Consider if some data can be securely archived (air-gap) so an online attack accesses the minimum information. (Note insider threat considerations and also whether you actually need to keep the data or it needs to be securely destroyed.)

Later in the degree course, there is another module on privacy which will provide more depth. There are some key requirements and guidance for the UK from the Information Commissioners Office (ICO) which provides a depth of information.

-   [ICO advice](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/security/)
    
-   [ICO data protection by design](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/accountability-and-governance/data-protection-by-design-and-default/) (note security by design and privacy by design are key considerations)
    
-   [ICO security outcomes](https://ico.org.uk/for-organisations/security-outcomes/)
    
-   [ICO accountability and governance](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/accountability-and-governance/)
    
-   [ICO small business security practical guide](https://ico.org.uk/media/for-organisations/documents/1575/it_security_practical_guide.pdf)
    
-   [ICO accountability framework](https://ico.org.uk/for-organisations/accountability-framework/)
    
-   [ICO use of encryption](https://ico.org.uk/for-organisations/guide-to-data-protection/guide-to-the-general-data-protection-regulation-gdpr/encryption/)
    
-    [ICO guide to cloud computing](https://ico.org.uk/media/for-organisations/documents/1540/cloud_computing_guidance_for_organisations.pdf)
    
-   [ICO guide for online services](https://ico.org.uk/media/for-organisations/documents/1042221/protecting-personal-data-in-online-services-learning-from-the-mistakes-of-others.pdf)
    

In terms of threat – is there much we can do to make us less of a target? We can [reduce exposure as identified by NCSC](https://www.ncsc.gov.uk/information/reducing-your-exposure-to-cyber-attack)  where we are effectively investing in our protect, detect and response capabilities.   

Our IT/security team, our employees and students need awareness, training, and overall we need additional security resourcing (staff, equipment and services) and of course better management and governance. Recall from Taylor et al., Chapter 2, that we could make use of cyber insurance as a mechanism to share risk. 

How much will it cost to make our organisation 'significantly above average' in terms of cyber protect, detect and respond/recover?  (And how can we measure this?) In scenario 14, we have identified average threat and information assets, but selected our protect, detect, respond/recover capabilities as significantly above average. That could potentially save circa £400,000 per annum based on one successful cyber-attack according to the HISCOX cyber exposure calculator. 

Note it is a model based on previous data for similar businesses, we might be unlucky and the attackers could have more successful attacks and we have significantly higher losses. We might not save £400,000 per annum, so we are speculating here on what might be.