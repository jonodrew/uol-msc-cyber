Sources: [[Everyday Cryptography#11.1 Certification of public key]]

A public-key certificate binds a [[public key]] to data that relates to the assurance of purpose of the public key. A public-key certificate only serves to bind the data together. It cannot be used to encrypt or sign. It is also not a proof of identity! There are four essential pieces of information:
- Name of the owner: this should be unique within the context in which it is employed
- public-key value: the public key itself, usually with an identifier of the algorithm used to generate it/with which it should be used
- validity time period: the date and times between which the key is valid
- signature: the creator of the certificate signs the certificate, asserting that they believe that the data contained within is correct.
	- of course this raises the immediate question: who is the creator? Why do we trust them? Is it because of their certificate. Who is the creator of that? ...

## The Creators
A creator of a [[public-key certificate]] is called a [[certificate authority]]. They generally play three important roles:
1. Certificate creation (and issuance)
2. Certificate revocation
3. Certificate trust anchor: it is at the end of the chain of trust, and so needs to maintain its profile as above all suspicion

## Lifecycle
### Differences to key lifecycles
- Generation: just generating the asymmetric key pair is harder than symmetric. Now we have the added challenge of determining the validity of the associated information. 👎🏻
- establishment: potentially easier. The private key should never leave the creating organisation (or if it does, it should be securely transmitted). The public key is meant to be public, so it's a very easy operation
- storage/backup/archive: less sensitive when applied to [[public-key certificate]]
- usage: common formats, like X.509, specify fields for key usage
- change: let's talk about this later (?!)
- destruction: a less sensitive operation, and sometimes not even necessary

Generating a public-key pair and generating a public-key certificate are two separate processes. Some scenarios for these processes follow:

### Trusted third party generation
A trusted third party - potentially, but not necessarily, the CA - generates the key-pair. If they are not the CA, they'll need to contact the CA to arrange for a certificate to be created. Given the extra responsibilities that this third party would have, this is a scenario most often applied to closed ecosystems
#### Advantages
- Creating key-pairs properly is complex, and a third party may be better suited to carrying out this process
- Equally, it frees up resources for the owner
#### Disadvantages
- all of the usual disadvantages of outsourcing your key management to a third party

### Combined generation
The owner of the key-pair generates the key-pair themselves. They then submit the public key to the CA, who will generate the public-key certificate. This scenario is common in open environments, where the owners of the keys do not necessarily trust a third party to manage keys.
#### Advantages
- the owner is in full control of the process and the private key
#### Disadvantages
- the owner takes on all the risk and difficulty of generating and storing key-pairs
- the owner will need to demonstrate to the CA that they posess the private key relating to the public key they submit

### Self-certification
The owner of the key-pair generates the key-pair, and the certificate, and then signs it themselves. If they sign it with the private key that corresponds to the public key in the certificate it is known specifically as a self-signed certificate. CAs often self-certify their public-keys.
#### Advantages
- no need for an external authority
- everything can be done in house
- as long as users trust the issuer, this can work
#### Disadvantages
- this does not scale at all