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
- clauses 5, 6, 7.1, 7.2, 7.3, 7.4, 8.1, 8.2, 8.3, Annex A.1 of [[ISO 27005|ISO/IEC 27005]]

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
>[!question] Consider the case where a risk has been shared via an insurance policy. What can the organisation do if the insurance company ceases operation?
>
>This would require a reassessment of the risk. With the insurance company bankrupt and therefore unable to offer compensation if the risk is realised, the risk is essentially untreated. New treatments may need to be applied. 
>
>Additionally, for me this raises the following question: who owns the risk of the risk-sharer going bankrupt, and what treatment can be applied to this *other* than acceptance? Can it be mitigated through re-insurance?

## Lesson 5: A simple scenario
- [[Chris Mitchell]] takes us through a simple example of [[risk assessment]]
- for a qualitative assessment that's given a numerical score, what's the impact of a function that sums the scores versus a function that calculates the product? 
	- There's no difference in the matrix that's output, so I suppose it comes down to whether you think a risk of 25/25 is going to impress folks more than 8/8
	- However, if your risks are qualitative, your qualities will appear larger. For example: if you have a risk that is a 2/2, and you reduce the likelihood to 1, the sum function tells you that you've reduced the risk by 25% (4 --> 3), while the product function tells you that you've reduced the risk by 50% (4 --> 2). Which is a more accurate representation of the world?
	- Equally, if the likelihood of an impact-2 risk increases from 1 to 2, has the risk overall become 33% greater (3 --> 4) or 100% greater (2 --> 4)?
	- For me, this is the clearest problem with representing qualitative assessments numerically. Numbers are not neutral, and understanding their relationships, and the relationships created by functions, is non-trivial.
- "Assigning values to risk probability and risk impact is a difficult and complex task" says Chris, king of understatement