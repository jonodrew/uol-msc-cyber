---
author: "[[Carmela Troncoso]]"
---

This is part of the #CyBOK 
## Introduction
- #privacy is a human right!
- privacy can (should!) be considered as a security question, with a view to the [[attacker|attackers]] that might be interested. This is the "adversarial model"
- privacy is necessary, even as it protects illicit activities
- references "contextual integrity" from [[Privacy as context integrity]]
## 1 Privacy as [[confidentiality]]
- includes both data being communicated and metadata (data about the data)
### 1.1 Data confidentiality
#### 1.1.1 [[cryptography]]-based access control
##### data in transit
- protection of data in transit is known as [[end-to-end encryption]]
- argues that this often includes [[data integrity]] and user [[authentication]]
- can use [[Diffie-Hellman]] to ensure [[forward secrecy]]
- a special case of [[end-to-end encryption|E2EE]] is what's known as [[Off-the-Record]] messaging
- The [[signal messaging protocol]] implements something very close to [[Off-the-Record]], and more details are in [[A formal security analysis of the signal messaging protocol]]
##### data during processing
- how do we protect data when someone else has to process it, and we consider that person [[attacker|adversarial]]?
- two examples are given:
	- if you access a record on a patent database, it gives the owner of that database information about a business you may be thinking of starting
	- accessing a particular entry in a messaging directory reveals relationships between users
- apparently these problems can be mitigated by [[Private Information Retrieval]], more of which in the [[Cryptography Knowledge Area]], which allows a database to be queried without revealing which record is being accessed
- a similar use-case exists in online shopping, where a server returns information to a user depending on inputs. Shopping patterns may leak information about users, and in such cases [[Oblivious Transfer]] can be used (again, referring back to [[Cryptography Knowledge Area]])
- these are very specific approaches to these problems. The general solution would be [[homomorphic encryption]]
- We also consider collaborative computation, where everyone involved in the communication collaborate
- such applications might include computations with entities one considers an [[attacker|adversary]], and so how do you conduct this effectively?
	- [[Multi-Party Computation]] (see Lewis' MSc thesis about dead-drops)
	- you might also use [[Private Set Intersections]]
##### verification of encrypted data
- how do you verify data that you can't see?
- enter: [[zero-knowledge proof]]
- these are well suited to verifying inputs to a privacy preserving protocol are as they should be
- there is also a question of 'private [[authentication]]': is it possible to authenticate to a service without providing an identity? One approach is [[Attribute-Based Credentials]]
- what if you want to spend money privately? [[blockchain]]-based currencies, like [[Zerocash]], offer privacy-preserving technology in the use of [[ZK-SNARK]] systems
#### 1.1.2 [[obfuscation]]-based inference control
##### [[anonymisation]]
- removing identifying information from data points to make them unlinkable

## 2 Privacy as control

## 3 Privacy as transparency

## 4 Privacy technologies and democratic values
### 4.1 Privacy technologies as support for democratic political systems
- Technology that increases democracy is generally good
- Technology that uses outsourced elements, such as cloud, can't be trusted
- therefore we must ensure that the systems preserve privacy

#### [[eVoting]]

#### [[anonymous petition]]

### 4.2 Censorship resistance and freedom of speech
We can understand censorship as an attempt to impose a specific distribution of content across a system. 

>[!note] there are other ways to understand censorship, and we should recognise the cultural dimensions the author is bringing into this. Here's an example of a counter-cultural argument: https://weirdpeople.fas.harvard.edu/qa-weird

#### Data publishing censorship resistance
- you could publish copies of documents on servers in different jurisdictions, so that they can't all be 'got' at the same time
- if you encrypt the files, then the state can't see inside them and try to selectively disallow distribution
- anonymous [[authentication]], or no authentication at all, means that the server can't be compelled to give up user identities
- this approach later inspired [[Freenet]] and, in a way, [[Tangler]]
#### Data access censorship resistance
- users have to be able to conceal that they're accessing that material
- this might be through mimicking: requests to a service can be modelled to look like a different service, for example a Skype call. However, this may not stand up to the scrutiny of an [[attacker]] actively probing the service
- alternatively through tunnelling: you pass data through a widely-used service, so that blocking that communication becomes more expensive for the censor
- finally you might hide communication/material inside videos or images - a kind of [[steganography]]
- alternatively you might look at hiding the destination of the request. [[Tor]] does this by relaying traffic through intermediate nodes whose [[IP address]] is not public. However, they appear normal. Service providers do this through the use of pluggable transports
- alternatively, have the option of 'decoy routing'. The request is initially routed to a benign destination. However, the request includes a secret signal that is interpreted by a  censor-antagonistic, cooperating [[router]]