## Abstract
Bitcoin is a purely online virtual currency, unbacked by either physical commodities or sovereign obligation; instead, it relies on a combination of cryptographic protection and a peer-to-peer protocol for witnessing settlements. Consequently, Bitcoin has the unintuitive property that while the ownership of money is implicitly anonymous, its flow is globally visible. In this paper we explore this unique characteristic further, using heuristic clustering to group Bitcoin wallets based on evidence of shared authority, and then using re-identification attacks (i.e., empirical purchasing of goods and services) to classify the operators of those clusters. From this analysis, we characterize longitudinal changes in the Bitcoin market, the stresses these changes are placing on the system, and the challenges for those seeking to use Bitcoin for criminal or fraudulent purposes at scale.

## Notes
- it's a paper about [[Bitcoin]]
- is there value in having money that you have to keep safe yourself?
- Yes, if your threat model includes your bank freezing your account
- there's a valid question about whether that should be _everyone's_ threat model
- this paper conducts a de-[[anonymisation]] attack to identify clusters of [[public key]]s, and hence specific 'spending authorities'
- authors argue that [[Bitcoin]] isn't actually as anonymous as people think it is