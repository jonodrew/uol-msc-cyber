Written by [[Keith Martin]]

## Chapter one
Securing things might mean:
- ensuring we can trust the contents of a message, [[integrity]]
- ensuring the message can be received, [[availability]]
- ensuring the message can't be read in transit: [[confidentiality]]
- this is the [[CIA triad]]
- paradox of crypto: allows people to transact secretly. Good if you're sending account details, for example, but bad if you're sending [[CSA]] 
- when Keith talks about [[security service]], he doesn't mean Box or VX. He defines it as 
>a specific security goal that we may wish to achieve.

- he lists some of them:
	- [[confidentiality]], or secrecy: that the data cannot be viewed by an unauthorised user (what does _authorised_ mean, then? has the key == "authorised"?)
	- [[data integrity]]: that is hasn't been changed
	- [[data origin authentication]]: the assurance that a given entity was the original (!) source of received data. Therefore, even if the data has been forwarded many times, there is still a means of proving that the message originally came from [[Alice]]
	- [[non-repudiation]]
	- [[entity authentication]]: assurance that a given entity is involved and currently active. Currently active requires a "freshness" check, like a short-lived token
### relationships between security services
 - [[data origin authentication]] is a stronger notion than [[data integrity]]. If you can be certain that the message came from the originator, but not what the message was, there is no value.
 - [[non-repudiation]] is stronger still than [[data origin authentication]]. If we need to be able to prove to a third party that data came from [[Alice]] and that it really says she is giving us her house, then we naturally need to prove also the integrity of the data and the origin
 - however, [[data origin authentication]] is not the same as [[entity authentication]]. For example: we should be able to prove that your grandmother's will was written by her and that the data in it has not been changed (even though it's changed hands multiple times). However, that's not the same as checking that your grandmother is there. Frankly, you need a medium at that point, and not a lawyer. Different kind of parasite.
 - with that being said, you could use [[data origin authentication]] plus a freshness check to provide [[entity authentication]]. After all, if we can prove that's Nana's signature, and she can tell us what's in it, then we can be pretty confident she's really Nana, and not a demon wearing her skin.
 - finally, [[confidentiality]] does not imply [[data origin authentication]]. Just because nobody else can read the message, doesn't mean it came from the person you thought it came from.
### concepts
- [[cryptographic primitive]]
- [[cryptographic algorithm]]
- [[cryptographic protocol]]
- [[cryptosystem]]

### primitives and what they can offer

#### on their own
- [[encryption]] can only provide [[confidentiality]]
- a [[hash function]] can sometimes provide [[data integrity]]
- a [[MAC|message authentication code]] can provide both [[data integrity]], [[data origin authentication]], and sometimes [[non-repudiation]]
- a [[digital signature]] can provide [[data integrity]], [[data origin authentication]], and [[non-repudiation]]

### Basic model of a [[cryptosystem]]
Suppose [[Alice]] wants to send something to [[Bob]]. She cannot be sure that the channel she's using won't be intercepted, and she wants the message to retain [[confidentiality]]. 

![[fig. 1.2.png]]

the following terms will be useful:
- [[plaintext]]
- [[ciphertext]]
- [[encryption algorithm]]
- [[decryption algorithm]]
- [[encryption key]]
- [[decryption key]]
- [[attacker|interceptor]]

To encrypt the [[plaintext]], the sender needs access to the [[encryption key]] and [[encryption algorithm]]. If the [[plaintext]] is not encrypted in a secure environment, there's no guarantee as to its [[confidentiality]]. The receiver needs access to the [[decryption key]] and the [[decryption algorithm]], and again should only decrypt the data in a secure environment.
It is worth noting that [[encryption]] cannot prevent interception, but it can render interception less valuable as an attacking technique, because the data will be unintelligible (there are caveats - see also [[Enigma]]). [[encryption]] also doesn't guarantee end-to-end confidentiality, because there is no way to guarantee the security at both ends.

### A brief word about [[codes]]
First rule of crypto club is that you don't talk about codes, because nobody knows what that means. Generally, the term code is used for any scheme where data is replaced with other data before being communicated. This is the process of encoding and decoding, and is generally not for [[cryptography|cryptographic]] purposes. Some examples are [[Morse Code]] and [[ASCII]]. Now, if a codebook is kept secret, then this might be some kind of [[cryptosystem]]. Not necessarily a good one - a "code" like Morse is vulnerable to [[frequency analysis]], [[index of coincidence]], and [[Kasiski examination]]. 

[[Morse Code]] is similar to the encryption approach we study here only in that it uses [[binary]] - dots or dashes. However, when we examine the way computer systems encrypt data, they don't bother ever storing data as human-readable language. Instead, they start with binary.

### [[steganography]], my favourite dinosaur
Steganography is the study of information hiding. That is, the aim is to transfer a plaintext from a sender to a receiver in such a way that only the receiver can retrieve the plaintext, because only the receiver knows the plaintext exists in the first place. For example, [Herodotus' tale of a message being tattooed on a slave's scalp](https://en.wikipedia.org/wiki/Histiaeus#Ionian_revolt_(499-494_BC). This differs from [[cryptography]], where the encrypted data can be shown to an interceptor. When using steganography, an interceptor should be unaware that any message is being passed at all.

### [[access control]]
This is a major topic in its own right, and likely one that we'll return to in other parts of this course. For now, it's enough to say that access control is another mechanism, usually applied at the [[Application Layer|application layer]]. It should be used alongside [[encryption]] - the so-called [[Swiss Cheese model]] model of security - to protect data.

### Two types of [[cryptosystem]]
There are two kinds of [[cryptosystem]]: [[symmetric]] and [[asymmetric]]

## Section 1.5: [[cryptosystem]] security assumptions

### 1.5.1 Standard assumptions
We have to make certain assumptions when building a cryptosystem. They are:
- that the attacker can access all [[ciphertext]] sent by the system
- that the attacker can guess some [[plaintext]]-[[ciphertext]] pairs
- that the attacker has access to the full detail of the [[encryption algorithm]] (see [[Everyday Cryptography#^9e46e5|1.5.3]] below)
### 1.5.2 Theoretical attack models
Broadly there are four theoretical #attackModel: [[ciphertext-only]], [[known-plaintext]], [[chosen-plaintext]], and [[chosen-ciphertext]]. 

### 1.5.3 Knowledge of the [[encryption algorithm]]
The way the book uses the word proprietary is not the way the word is generally used. This is, in my opinion, deeply stupid, and so for the purposes of these notes "proprietary" means "private" or "secret". This is to be compared with publicly known algorithms, which are very sensibly named.
The second of [[Kerckhoffs' six principles]] states that
>[The [[encryption algorithm]]] must be able to fall into the hands of the enemy without inconvenience

This is not the same as saying that the algorithm must be public; only that if it were, it would not hamper its operation.
With that being said, publicly known algorithm do have some advantages. It opens up the algorithm to scrutiny by experts, who may be able to identify flaws. It enables interoperability, which in turn increases uptake and decreases costs. Finally, it enables transparency: an algorithm I can read and understand is more trustworthy than a black box that you swear is definitely 100% secure.
Still, we should recognise that there aren't that many experts. Making an algorithm public means it can be scrutinised, but not necessarily that it will be. This is similar to the problems in [[open source code]]. 

^9e46e5
## 1.6 Breaking [[cryptosystem|cryptosystems]]
Hacker voice: I'm in
Note that in this section we're only going to deal with breaking the system's [[cryptographic primitive]]s, not the wider system. So no [[rubber hose cryptanalysis]] just yet. Here we're going to be dealing with [[binary number]], [[exclusive or]], [[exponentiation]], and [[concatenation]]. You already know what they are, but if you don't, take a look at their pages. That was 1.6.1, so let's jump straight to
### 1.6.2: [[Key lengths and keyspaces]]
[[Key lengths and keyspaces]] is a very important thing to know about, so go read that.
### 1.6.3 Breaking an [[encryption algorithm]]
Even though we said we were going to stick with the algorithmic stuff, [[Keith Martin]] points out again that the most likely point of failure of a cryptosystem is the [[key management system]]. However, speaking purely technically, there are two kinds of break:
1. There is found a method for determining the [[decryption key]] directly. This is Game Over for users, because the decryption key can be applied retroactively to all communications
2. There is some weakness in the [[encryption algorithm]] that allows analysts to deduce a [[plaintext]] from a [[ciphertext]], without first deducing the [[decryption key]]. This is the way [[Enigma]] was broken.
There is discussion about the value of (2), because deducing a single plaintext from a ciphertext probably doesn't mean the entire algorithm is broken. With that in mind, let's look at the one surefire way to break almost every [[cryptosystem]]:
### 1.6.4 [[exhaustive key search]]
This attack is so important that it's the benchmark against which all other attacks are measured, and is effective against all-but-one [[encryption algorithm]] (more on which in [[#3.1.3]]) Further detail in the linked page on how they're done, but right now we're interested in protecting against them. Given that an [[exhaustive key search]] is, well, exhaustive - one way to protect against the approach is to make the [[keyspace]] so bloody enormous that it's not worth the effort. How big does that mean?
There are about 30 million seconds in a year, which we can express as $3 \times 10^7$ or $2^{25}$, depending on how we feel a the time. Assuming we only want our messages to be secure for a year, what size of keyspace do we need?

Keys per second|Key length required
---------------------|--------
1|26 bits
$10^6$|46 bits
$10^6 \times 10^3 = 10^9$ |56 bits
$10^6 \times 10^6 = 10^{12}$|66 bits

The threat of the exhaustive key search is an argument in favour of making a [[decryption algorithm]] slower. However, most designers try to make their [[cryptosystem]] as seamless and rapid as possible - so practically speaking, it's huge [[keyspace]] or bust. Check out [BlueKrypt](https://www.coursera.org/learn/uol-cym040-applied-cryptography/supplement/nbQHs/key-lengths#:~:text=Visit-,BlueKrypt,-.%20This%20is%20a) for more info on keyspaces.

### 3.1.3

## Chapter four: [[symmetric|symmetric encryption]]

### 4.1
In general, a [[symmetric encryption algorithm]] is either a [[stream cipher]] or a [[block cipher]]. This division is slightly false, because:
- a stream cipher could be considered a block cipher with a block size of one
- a stream cipher that operates on bytes could be considered a block cipher with a block size of 8
- block ciphers are often used in a [[mode of operation]] that turns them into stream ciphers. The block cipher is used to generate a [[keystream]], which is then used by the stream cipher to encrypt the data.
We tend not to use these categories when describing an [[asymmetric encryption algorithm]], because they work in a slightly different way.

^716736

### 4.2 - [[stream cipher]]
The author argues that a modern [[stream cipher]] simulates a [[Vernam cipher]] by using short [[key|keys]] to generate longer one-time keys. This gives us the best of both worlds.

#### 4.2.1 Model of a [[stream cipher]]
As noted above, we don't use a [[key]] as long as the [[plaintext]]. Instead, the key is used as the seed for the [[keystream generator]]

^8d27eb

#### 4.2.2 [[key management system]] for [[stream cipher]]
This is generally a solved problem, and the same issues and solutions exist as exist for securing the [[key]] of a [[symmetric|symmetric cryptosystem]]. However, we must additionally be cautious not to use the same portion of the [[keystream]] for encrypting two different [[plaintext]]s, because the difference (\![[exclusive or|XOR]]) between the two [[ciphertext]] messages will reveal the difference in their respective plaintexts. So we might add additional complexity to the key before inputting it into the [[keystream generator]]. We might use time variant data (see section [[#4.6]]), either as part of the key or as part of the generator itself.

#### 4.2.3 - the impact of errors
Within a communication system, there will always be [[transmission errors]], [[transmission losses]], and [[computational errors]]. In noisy or unreliable environments, the first two can be almost guaranteed. These errors are all problematic, because [[off-by-one-errors]] are horrible. However, there's something interesting here about [[error propagation]] - if we want it, and if it's better that it happens. For example: if a single figure silently changed from a point (.) to a comma (,) it could be disastrous and hard to spot. If the entire number was also changed into its inverse, then users might be more likely to notice the error.

#### 4.2.4 properties of a [[stream cipher]]
- no [[error propagation]]: a one-bit error in the [[plaintext]] will only ever result in a one-bit error in the [[ciphertext]]
- speed: because the [[encryption algorithm]] is just [[exclusive or|XOR]], stream ciphers are dead quick
- on-the-fly encryption: stream ciphers are great for encrypting a stream of data, like keystrokes into a secure terminal
- efficiency: at a hardware level, this algorithm can be implemented with a very low gate count
However!
- synchronisation must be perfect, as if the sender and receiver's [[keystream]] fall out of sync the receiver will be completely unable to decrypt the message
	- some implementations use a fresh key every _n_ seconds
	- others make the keystream dependent not just on the key but also on several of the most recent bits of the ciphertext. Thus if connection is lost and re-established, the [[keystream]] will re-sync
- Stream ciphers tend to be properietary, in contrast to [[block cipher]], which are more well-known and tend towards openness. 
- they also have slightly lower versatility. While a [[block cipher]] can be used for [[hash function]] and [[MAC]] design, stream ciphers can really only do [[encryption]]. And even then, it's trivial to adjust a [[block cipher]] to function as a stream cipher.

#### 4.2.5 examples of a [[stream cipher]]
With all that in mind, are there any stream ciphers actually in use? Yes. The three best-known are [[RC4]], [[A5-slash-1|A5/1]] , and [[E0]]  

### 4.3 - [[block cipher]]

### 4.4 The [[DES|Data Encryption Standard]]
It's important to be familiar with her, even though she's not in use any more. Like Queen Elizabeth (either). But first, let's get Feistel

#### 4.4.1 [[Feistel cipher]]
The cipher on which [[DES]] is built

#### 4.4.2
![[DES#Specification]]

#### 4.4.3
![[DES#History]]
#### 4.4.4 [[Triple DES]]
This is very, very bloody tricky, so watch carefully.
### 4.5 [[AES]] #ToDo
Linked page covers development and design. The design is particularly tricky.
### 4.6 [[mode of operation]]
#### 4.6.1 [[ECB mode|Electronic Code Book mode]]
Having considered the many, many [failings of ECB mode]([[ECB mode#Problems]]) we turn to better alternatives
#### 4.6.2 [[Cipher Block Chaining mode]]
#### 4.6.3 [[Cipher Feedback mode]]
#### 4.6.4 [[Counter mode]]

### 5.4.3

^075586
## Chapter six: [[data integrity]]

### 6.1 Different levels of [[data integrity]]
Let's look at four attacks, in increasing order of severity.
1. Accidental errors. These are things like noise in a communications channel, and mechanisms offering protection against this level of attack include error-correcting codes like those in 1.4.4 and simple checksums like [[cyclic redundancy checks]]. These techniques compute a digest that is appended to the original data and which is computed with a simple mathematical formula. Since such a digest can be computed by anyone, they offer zero protection against an active attacker, because it becomes trivial to change both the message and its digest
2. Simple manipulations. In the case above, an attacker can predict what the new digest will be, and doesn't even need to calculate it. A [[hash function]] protects against this to a minor extent, because an attacker has to actually compute a new hash, but it's not exactly protection. It's the difference between leaving the door open, and closing it but not locking it.
3. Active attacks. In order to prevent an [[attacker]] creating a 'valid' digest, there has to be some secret as input. In turn, this normally additionally provides [[data origin authentication]], because the most natural way of preventing active attacks of this type is to tie together the source and the underlying data. The main mechanism for data integrity at this level is a [[MAC]].
4. Repudiation attacks. The [[attacker]] was inside the house the whole time! If someone signs something and then tries to wriggle out of it, how can we prove that they did in fact sign it? This will be covered by a later discussion of [[digital signature]].

### 6.2 [[hash function]]
An interesting, potato-based [[cryptographic primitive]]. The linked page covers 6.2.1 and 6.2.2
#### 6.2.3 How to attack a [[hash function]]
- a very small hash is a vulnerable hash. Consider a hash of length 2: the total number of possible values is only 4. That means there is a 1-in-4 chance that my super-strong password has the same hash as 'password1'. ❌
- a small hash is still vulnerable, though in a more interesting way. Consider a 10-bit hash. There are $2^{10}$, or about $10^3$, potential hashes. The likelihood of stumbling onto a match for my super-strong password is now only 0.1%. Success? Not quite. Because my system enforces certain rules for passwords, an [[attacker]] can generate a table of 1000 hashes corresponding to the rules for the password. Unfortunately, they've also bought the disk containing all of our hashed passwords...and now all they need to do is find a single overlap.

#### 10.2.1 Key lifetimes
A key should have a finite lifetime: a key that can be used forever represents an enormous risk. Finite lifetimes mitigate against:
- key compromise
- previously authorised users who've stolen the key
- future, as-yet-unknown attacks
Fixing the lifetime to a management cycle enforces key change/cycling, which is often valuable (but not always!)

#### 10.2.2 Key lengths
Longer is better, but also requires more computing power when encrypting. Because capabilities are always improving, it's worth looking at recent advice from the national technical authority (here: [[National Cyber Security Centre|NCSC]]) for how long a key length to pick.

### 10.3 Key generation
#### 10.3.1 Direct key generation
Keys can be directly generated with the help of a source of randomness. Different techniques exist for generating randomness.

#### 10.3.2 Key derivation
A means by which we can take a main key, generated in a strong and expensive way, and then derive other keys from it. For example, we could derive a signing key and an encryption key (because they shouldn't be the same) from the same base key, rather than having to generate two keys.
This then allows for longevity of the base key, and we can take advantage of this to insert it directly into hardware.

#### 10.3.3 Key generation from components
We may not want to trust one entity with key generation, in case they turn out to be evil. One mechanism is as follows: suppose we wish to generate a 128-bit key. Three people (Alice, Bob, and Charlie) securely generate 128 random bits. These three components are then [[exclusive or|XOR]]'d together, and that combination is the key. The combination is never replayed to the participants.

There are even clever-er approaches, such as the [[Shamir secret-sharing protocol]], that allows a key to be generated from any $k$ of $n$ components. 

### 10.4 Key establishment
This is the process of getting keys from the place where they're generated to the place where they'll be used. So, logically, the best key establishment practice is to generate them closest to where they'll be used. However, keeping a key close to the thing it secures is also considered very bad practice. The sum of these problems means key establishment is either hard or easy, but never in-between.

#### 10.4.1 Key hierarchies
Keys at a higher level can be used to encrypt keys at the level below. Naturally this is a recursive problem: how do we encrypt/secure the keys at the highest level? And how do we share them?
Everyone having a copy is a pretty bad idea, because then a single compromise/internal threat can pwn the whole network. Instead, we will likely fall back to a trusted authority of some form or another. The alternative is trying to establish data keys for all users - but with only 100 users, there's need to be 4950 data keys, one for each potential pair of users.

#### 10.4.3 Quantum key establishment
Sending a conventional key over a conventional channel risks interception. Quantum particles are changed by observation. Thus, if a key could be stored and transmitted as quantum particles, any interception would probably be noticed. The book goes into detail as to the protocol for quantum key establishment...but I'm not sure there's much value in recording it here, as the book then goes on to point out that it's not really that valuable for everyday applications.

### 10.5 Key storage
#### 10.5.1: Avoiding key storage
This is the best solution. Can't steal keys if they're not stored anywhere. This is just about manageable for local use, where a passphrase is used to generate an encryption key. If the passphrase is the same, and the key generator is deterministic, then we can confidently through away the key once it's used. However, this does rely on human users remembering secure passwords, which isn't always possible. However, if a key is needed for communications purposes, there's not really any way around the need to store the key somehow.

#### 10.5.2 Key storage in software
Software is inherently weaker than hardware - but it is easier. Security doesn't exist in a vacuum, and costs are a valid contrast with security.
>[!warning]
>### Storing keys in the clear: how to
>
>don't

So the key has to be encrypted before it's stored. But then we have the same problem again: where do we store _that_ key?

Alternatively we can generate it on the fly (see above in [[#10.5.1: Avoiding key storage]]), or we can store it in hardware. Or, finally, we can store it in component form ([[#10.3.3 Key generation from components]])

So it's better generally to store it in hardware

#### 10.5.3 Key storage in hardware
There are a multiplicty of fiendish ways Hardware Security Modules can be designed to be tamper-resistant. These are the pieces of hardware designed specifically to store cryptographic keys and to provide cryptographic operations. There is still the risk that these devices communicate through an API, and a malicious actor could use that API to get [[known-plaintext]] into ciphertext and thereby begin to divine the key. For this reason, clients that interact with the HSM should be well-designed and, in secure environments, build entirely-in house by trusted individuals.

#### 10.5.4 Key storage risk factors

![[Screenshot 2022-11-27 at 10.19.15.png]]
A nice diagram here detailing the riskiness of where the HSM/hardware is stored.

#### 10.5.5 Key backup, archival, recovery
Some organisations and legislations require the storage of keys, even after they've reached the end of their useful life. This is so that prior documents can be checked for authenticity. Key backup is tricky. We use safes and encrypted drives.

#### 10.6.1 Key separation
Keys should only be used for their intended purpose!

(But sometimes that's tricky/expensive, which is why we can fudge it a bit with key derivation)

[[Mobile phone security]] conforms strictly to the principle of key separation by defining a key derivation hierarchy that generates a range of keys for all the different purposes that are needed. Likewise, [[Transport Layer Security|TLS]] conforms rigorously, deriving separate keys for encryption and [[MAC]] computation (unless using authenticated encryption) and even defining entirely separate keys for each direction of the TLS communication.

#### 10.6.2 Key change
Sometimes key changes are planned, because we expected the key to come to the end of its lifecycle.  Sometimes, however, we fuck up and need to make an unplanned key change. ^1c1779

Key changes are really fucking difficult. At the highest level, we will need to re-encrypt all of the keys at the level below. If the change was unplanned because of key compromise, then it's possible there will need to be an incident response process to decide if all data encrypted by the key will need to be re-encrypted.

#### 10.6.3 Key activation

## Chapter 11:  [[public key]] management

### 11.1 Certification of [[public key]] 
- the main challenge for managing public keys is providing "assurance of purpose"
- the most popular mechanism for doing this is the [[public-key certificate]]
#### An example
Suppose I receive a digitally signed contract from my friend Alice. At least, I have a [[public key]] that supposedly belongs to Alice, and when I check the signature with it it returns a valid response. What might have gone wrong, for this to be inaccurate?
- the key may not really belong to Alice. I may have been tricked, and sent a key that actually belongs to Bob. Damn you, Bob.
- the key may belong to Alice, but Alice can deny that it's hers, and without some proof the signature may be cryptographically valid and legally useless
- the key may not be valid. It may have expired, and Alice has either purposefully or accidentally used it to create a signature that is not legally valid
- it may not be an appropriate key - for example, an organisation may have limits on how large a contract can be signed with a specific key
To provide assurance of purpose, we need to:
1. strongly associate the public key and the owner of the key, and
2. strongly associate the public key with other relevant data, including usage restrictions and expiry dates
This is made more difficult with public key encryption, because we put this stuff on the web, where it's harder to prove associations.

One crude approach is a trusted directory. However, 
- it would have to be trusted by all users of the public-key management system
- it would need to be available at all times
- it would need to be accurately maintained and protected from unauthorised modification
This is the basis (but not the whole) for a [[public-key certificate]]. You should go and read about that now
#### Registration of public keys
If either [[public-key certificate#Trusted third party generation|third party generation]] or [[public-key certificate#Combined generation|combined generation]] are used, the owner of the public-key pair must register with the [[certificate authority|CA]] before a certificate can be issued. That is, the [[certificate authority|CA]] must be confident in the identity of the requestor. Because this is a complex, almost certainly human-intensive process, it is common for this work to be conducted by a separate registration authority (RA), which itself may be distributed and feed into a single, centralised CA.
A [[certificate authority|CA]] may demand different levels of thoroughness in the registration process, and may offer different levels of certificates that correspond. They go from a very basic "does this person's email address work" all the way up to the kind of certificate used in national identity card schemes, which might use birth certificates, passports, etc

#### Proof of possession
If a [[certificate authority|CA]] runs [[public-key certificate#Combined generation|combined generation]], how can it be sure that the entity submitting the public key actually knows the corresponding private key? Simply, by encrypting a message with the public key, and asking the submitter to respond with the decrypted text. If they cannot, they do not own the private key.

### 11.2.3 key-pair change
#### Revocation of [[public-key certificate]]
Once a thing is published, it's impossible to un-publish it. So what can we do instead? We have to publish the fact that we have revoked it. Like a burn notice.

##### Certificate revocation list (CRL)
A database is maintained of all the serial numbers of all the certificates which have been revoked, called a certificate revocation list (CRL). A CRL needs to be carefully maintained, and is generally the responsibility of the CA that issued the original certificate.

##### Online Certificate Status Protocol (OCSP)
The opposite to the above: a database of valid certificates. This is standardised in RFC 2560.

##### Rapid expiration
If the certificate expires every five minutes, it would be real hard to use an invalid one. This is, however, very bloody expensive.


### 11.3 [[public key]] management models
#### 11.3.1 Choosing a CA
- in a closed environment, there's generally no choice. Central administrative functions within an organisation are generally well-suited to ensuring this
- in an open environment it's harder. There's commercial pressure to be excellent, obviously, but some argue that licensing is necessary
	- the industry argues that it's not and at time of writing in the UK they have successfully won that argument
#### 11.3.2 [[public-key certificate]] management models
The relationship between the owner of a public key, and the [[certificate authority|CA]], is either direct (in a closed environment) or a business relationship (in an open environment). However, what about the people who rely on the CA?

##### What if there were no CA at all?
The CA-free certification model is one where the owner uses the [[public-key certificate#Self-certification|self-certification]] approach. Relying parties access the certificate directly, and then make their own determination as to whether to trust it. This is linked to the idea of the [[web of trust]]

##### Reputation-based certification model
The reputation of the CA is the only thing the relying user can use to determine whether to trust the [[public-key certificate]]. However, this reputation can be developed by the CA over time

##### Closed certification model
When the relying party has a direct relationship with the [[certificate authority]], they can trust it firmly. For example, most departments will have a dedicated authority for issuing certificates.

##### Connected certification model
The 'friend of a friend' model. The relying party has a relationship with some trusted third party, which in turn has a relationship with the [[certificate authority|CA]]. This third party's role is to validate the data in the owner's [[public-key certificate]]. In this model, the relying party essentially delegates the task of validating a public-key certificate to another party - this 'validation authority'

#### 11.3.3: Joining [[certificate authority|CA]] domains
It's worth noting that this is a messy and quite complex process. Verifying a [[public-key certificate]] requires a user to:
1. Verify the signature on the public-key certificate
2. check all the fields in certificate
3. _and_ check whether the certificate has been revoked (although actually maybe do that first)

##### Cross-certification
The transitive property of trust means that (in theory) if Bob trusts his [[certificate authority|CA]], and his CA trusts Alice's CA, then Bob should be able to trust Alice's CA.

##### Certification hierarchy
If Bob trusts his CA, and his CA trusts the root CA (whoever that is), and the root CA has vouched for Alice's CA, then Bob should be able to trust Alice's CA.



## Chapter twelve
We secure the [[Internet]] with [[Transport Layer Security|TLS]]

Whomst the fuck is [[Diffie-Hellman]]?

### 12.6 [[cryptography]] for [[identity cards]]
Specifically, for the [[Belgian eID]] scheme