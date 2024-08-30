This week is concerned with standards for approaches to, and techniques used in, cyber security management. The key standards-making bodies are introduced, as are the most significant cyber security management standards. The use and contents of two particularly important cyber security management frameworks are explored, namely [[ISO 27001|ISO/IEC 27001]] and the [[NIST]] Security Framework. In the last part of this week, the compliance and certification process for ISO/IEC 27001 is introduced.

### Learning Objectives

---

-   Evaluate the appropriateness of security management frameworks for an organisation
-   Create security policies underlying an ISMS
-   Contribute to the development of an Information Security Management System (ISMS), in line with the requirements of ISO/IEC 27001, and evaluate its suitability

## reading
- [[Information security management principles#Chapter 3]]
- Clause 5 of the [[ISO 27000]]
- chapter 2 of [[NIST Special Publication 800-53|NIST SP 800-53]]: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf
- What is ISO 27001? https://advisera.com/27001academy/what-is-iso-27001/
- cyber essentials requirements: https://www.ncsc.gov.uk/files/Cyber-Essentials-Requirements-for-Infrastructure-v3-1-January-2023.pdf
- guide to secure payments: https://www.pcisecuritystandards.org/wp-content/uploads/2022/05/Small_Merchant_Guide_to_Safe_Payments.pdf


## Lesson 1: an overview of security management #standard 
- we quickly review the [[NIST Cyber Security Framework]] and [[NIST Special Publication 800-53]]
- we also touch on [[Cyber Essentials]]
- also note [[ISO 27701]], which is a #standard that explains how to apply [[ISO 27001]] to protect privacy
- How would you choose between NIST and 27001?
	- Depends whether you need certification, but also how mature the security function is within the organisation
- Then we get into [[Cyber Essentials]]

## Lesson 2: Deep dive on the [[ISO|ISO]] frameworks
- [[ISO 27001|ISO/IEC 27001]]
- [[ISO 27002|ISO/IEC 27002]]
- A reminder that security policies should be in line with the organisation's wider objectives:
	- "We will enforce need to know" is at odds with "We will let teams experiment with data to find new solutions", unless you redefine "need to know" as "everyone needs to know" - in which case what's the point of the policy?
- [[Statement of Applicability]]

## Lesson 3: [[NIST]] security framework
- [[NIST Cyber Security Framework]]
- and then [[NIST Special Publication 800-53|NIST SP 800-53]]
- note that 27002 used to categorise [[control|security controls]] in the same way that SP 800-53 does - according to purpose, as opposed to mechanism. ISO argue that the change was made because the new taxonomy is simpler, and there is no overlap between groups.
- There's a brief summary of the set of controls in the 'Awareness and Training' family of [[NIST Special Publication 800-53|NIST SP 800-53]].
- The fifteenth class of controls in 800-53 is entitled '[[personally identifiable information]] processing and transparency', and regards privacy rather than (strictly) security
- worth noting that NIST documents are loosely coupled, and seem more 'agile' or at least iterative. ISO documents are more targeted towards compliance and certification

## Lesson 4: Certification
- the compliance process for [[ISO 27001|ISO/IEC 27001]] is theoretically simple
- compliance must be audited by an independent third party. This third party will comply with more requirements, which are listed in a different standard: [[ISO 17021-1]]
	- it's standards all the way down!
- There's also (!!) another standard, [[ISO 27006]], which describes additional requirements on organisations verifying compliance with 27001.
- [[UKAS]] is the UK-based organisation that audits organisations that want to offer 27001 compliance. That is, the answer to the question "Who audits the auditors" is, in this case, UKAS
- The [[British Standards Institution]] offers certification/audit services, and provides us an opprtunity to check out the process
### The certification process
First, there is a gap analysis. The existing [[information security management system|ISMS]] is examined and compared with the requirements in 27001. If there are gaps between the two, these can be flagged and remediated before the 'formal' assessment.

Then comes the formal assessment in two stages. First, a check to see whether all specified procedures/approaches in 27001 have been implemented, and asking the client to rectify any omissions.

Once this has been done, the auditor should examine the full set of procedures and and controls to ensure they're working effectively.

The third and final phase is to issue the certificate of compliance, which is generally valid for three years. However, it's worth noting that there are still follow up checks during that period to ensure that the ISMS remains compliant

### Other certifications
- [[Cyber Essentials]]!
- [[PCI DSS]]!
