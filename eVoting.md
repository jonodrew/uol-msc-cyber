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
- a third alternative uses [[homomorphic encryption]], but I honestly can't follow this one. It might become clearer in the future
- 