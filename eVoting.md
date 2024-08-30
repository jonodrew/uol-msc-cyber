---
aliases:
  - electronic voting
---
Electronic voting systems should enable fair elections, despite being run in adversarial conditions. They must have the following qualities:
- ballot secrecy
- universal verifiability: an external observer could verify that all the votes that were cast were also counted, and that the two amounts tally
	- some protocols provide a weaker property, which is 'individual verifiability': that an individual voter can verify that their vote has been correctly tallied. 
- eligibility verifiability: an external observer could verify that each vote was cast by a unique eligible voter
- some #protocol also aim to resist coercion, with the aim of making it impossible for an [[attacker]] to force a user to vote in a particular way
### ballot secrecy
- traditionally this is done by:
	- ballots having no identifying marks
	- ballots being mixed in a bucket or urn, such that the individual who put that ballot in can't be identified
- in electronic voting this can be done through the use of [[mix networks]]
- alternatively, one can use blind signatures: an entity authorised to verify eligibility (which is not the same as [[identity]]) signs a vote without seeing the content of the vote. To ensure they're signing a 'good' vote, the user provides a [[zero-knowledge proof]] that the vote has been correctly constructed. The user then submits the signed vote to the tally server via an anonymous channel. At no point can any entity tie a vote back to a user
	- bloody hell, that's clever
- a third alternative uses [[fully homomorphic encryption]], but I honestly can't follow this one. It might become clearer in the future
## Properties
### ballot secrecy
- a voter's vote remains secret, except when the result of the election reveals the vote, or when partial information about the vote can be deduced from the result (eg, the vote was unanimous)
### [[Receipt-freeness]] (RF)
- a voter cannot prove that they made a particular choice. This means that an attacker has no incentive to buy a vote, because there's no way of proving that the victim voted the way the attacker wanted
### coercion-resistance (CR)
- a voter can cast their vote as intended, even if they are under the control of an attacker for some time (but not the entire time) during the election
- this is the strongest threat model for a voting system
- it models an adversary whose goal is coercion to vote in favour of one outcome, or alternatively abstention from the process itself
### Coercion-evident (CE)
### Everlasting privacy (EP)