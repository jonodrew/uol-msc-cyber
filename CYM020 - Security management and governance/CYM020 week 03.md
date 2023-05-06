This week is concerned with the management of cyber security risks. Risk management forms the foundation for both the [[ISO 27001|ISO/IEC 27001]] and [[NIST]] security frameworks. The [[ISO 31000|ISO/IEC ISO 31000]]  model for risk management is introduced, and the key steps are discussed. The key steps or  risk assessment and risk treatment are then examined in greater detail. The week concludes with a review of a simple worked example of the risk assessment and treatment processes.

### Learning Objectives

---

- Select, implement and coordinate security controls chosen in accordance with an established risk-based methodology
- Distinguish between approaches to risk treatment
- Help generate a comprehensive risk assessment for an organisation, as a key component of the [[information security management system|ISMS]]

## reading
- [[Information security management principles#Chapter 2: Information risk]]
- Clauses A.2.1-A.2.5 of Annex A of [[ISO 27005]].
- [_Standard deviations: a risk practitioner's guide to ISO 31000_](https://www.theirm.org/news/standard-deviations-a-risk-practitioner-guide-to-iso-31000/ "Standard deviations")
- clauses 5, 6, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2 of [[ISO 27005|ISO/IEC 27005]]

## Lesson 1: What is [[risk management]]?
- before you can manage a risk, padawan, you must understand what a [[risk]] is
- Before you can understand a risk, you must comprehend...a [[threat]]!
- definitions are valuable, because they delineate responsibilities and ensure we have nice clear silos
- Risks must be associated with an information asset. For example: having a weak password is not a risk. It might be a [[vulnerability]], and the vulnerability could be exploited to damage an [[asset]] - and herein lies the risk.
- consider also the difference between hostile acts and acts of nature. Can you consider climate change a threat?
- Are we now ready to manage risk?
- No! First we must consider the nature of the assets that are at risk
- 🚨 there is no clear boundary between the inside and outside of an organisation any more! 🚨
- risk management is a superset of cybersecurity management, which is a superset of cybersecurity
- there is a standard for risk management 😭 [[ISO 31000|ISO/IEC ISO 31000]], and a further standard that builds on it ([[ISO 27005|ISO/IEC 27005]])
- they're going to be the focus of the next lesson
- Let's talk about [[risk assessment]]
- [[ISO 27001|ISO/IEC 27001]] requires that organisations have a security [[risk assessment]] process that:
	- defines security risk criteria, including both risk acceptance criteria and criteria for performing risk assessments
	- ensures that risk assessments produce consistent, valid, and comparable results
	- [[risk identification|identifies information security risks]]
	- analuses the information security risks, including assessing the consequences, assessing the likelihood, and determining the overall level
	- evaluates the information security risks, including prioritising the analysed risks for [[risk treatment]]

>[!question] ISO/IEC 27001 requires risk assessment to be carried out periodically, according to a predefined schedule, and also when **significant changes** are proposed or occur. What sorts of events might be defined as significant changes in this context?
>
>Significant changes are those that require a review of risks. Although this sounds circular, it's impossible to detail what 'significant' means absent the context of an organisation. However, given the cost and intensity of people-time required, we can rule out minor changes in staffing. A migration from local servers to cloud; a change of office location; or the takeover of another company would always be considered 'significant' changes.

- we go in deptth on [[ISO 31000]]
- and then on to [[ISO 27005|ISO/IEC 27005]]

## Lesson 3: [[risk assessment]]
1. [[risk identification]]
2. [[risk management#Risk analysis]]
3. [[risk treatment]]
4. Risk evaluation
>[!question] When might it be appropriate to treat a risk which is assessed as being within the risk appetite of an organisation?
>
>It might be appropriate to treat a risk, even if it is within tolerance, when that risk is relatively unknown or if there is an element of uncertainty about the threats. For example, if the threat is unknown or poorly understood - suppose an insider whose capabilities could vary quite significantly . Alternatively, it might be the case that the context of the vulnerability is not well understood - for example, if there is a poor understanding of the extent to which a software library is incorporated across the business.

## Lesson 4: [[risk treatment]]
