---
alias: [Data Encryption Standard]
---
DES uses the [[Feistel cipher]], with a minor change: for each round a subkey is used, rather than the whole key. The subkey is formed from the main key according to the key schedule.

## Specification
- 16 rounds, 
- 64-bit block size 
- 64-bit key, although it uses the first byte (8 bits) to do checks - so the effective key length is 56-bit
- The round function is a substitution, using rules based on tables known as [[S-boxes]]
- the specification should also include the key schedule, which identifis which bits of the key are used to form subkeys for any specific round
- any additional processing steps
Further details can be found online

## History
In 1973 the [[United States]] government, in the form of the National Burea of Standards (now [[NIST]]) published a call for proposals for a new [[encryption algorithm]]. There were no responses, no doubt because until that point [[cryptography]] was a secret thing, maintained almost solely by spooky people.
In 1974 they tried again, and well-known Nazi collaborators [[IBM]] offered an algorithm they'd been developing. The algorithm was published for comment in 1975, adopted as a federal standard in 1976, and published as DES for the first time in 1977. It was made mandatory for federal agency use in the same year, and was adopted into the banking standard with ANSI X3.92. From there, it spread to the rest of the international financial industry, and became the standard for [[encryption]] worldwide until the development of [[AES]].

DES was supposed to have a 15-year lifespan. However, the [[NSA]] withdrew its endorsement in 1988, only 11 years after it was originally published. In the same year, the NBS reaffirmed its use, perhaps because it was so embedded in the financial industry that to do otherwise would have caused chaos.

However, in 1998 [[NIST]] issued a call for a new [[encryption algorithm]], implicitly admitting that DES no longer offered sufficient protections.

### Critiques
#### Secret design criteria
The design criteria were never published, and this raised concerns about the _why_ of the algorithm's design. In actuality, almost the opposite seems to have happened: when [[differential cryptanalysis]] was discovered in the 1990s, it turned out that DES was already protected against such attacks. This raised an interesting question: was it by coincidence, or did the people at the [[NSA]] who'd helped design the system already know about this kind of attack...?

#### Small [[keyspace]]
An effective length of 56 bits for a key is not long enough, and this critique was offered even in 1975 when it was first published for comment. There were some rumours, even, that the [[NSA]] had encouraged the smaller key size to enable an effective [[backdoor]]. These rumours have never been substantiated, but conspiracy theories are fun and they've made Dan Brown a millionaire, so...

To get a sense of the size of the keyspace, let us apply the rubric of an [[attacker]] using a cloud service like AWS to spin up a million containers, with each one able to to test a million keys per second. That is, the total power they can bring to bear is $10^{12}$ keys per second. With a 56-bit key, the total [[keyspace]] is $26^{56}$, which is (very roughly) $7.2 \times 10^{16}$. Therefore an exhaustive keyspace search will take:
$${7.2 \times 10^{16} \over 10^{12}} = 7.2 \times 10^4 seconds$$
which is about 20 hours. When defending we assume they key will, on average, be found in the first half of the search, which means we assume it'll take this attacker about 10 hours to crack the key.