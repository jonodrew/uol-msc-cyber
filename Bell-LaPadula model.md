This model is specifically concerned with [[confidentiality]] and reads like it came out of the [[DOD]]. Ah wait, it did. It's written to ensure that access to controlled information is managed effectively. There are three security policies:
1. The Simple Security Policy: a subject at a specific clearance level may not read an object at a higher security level
2. The * (Star) Security Property states that a subject with a given security level may not write to any object at a lower security level.
3. The Discretionary Security Property uses an [access matrix](https://en.wikipedia.org/wiki/Access_Control_Matrix "Access Control Matrix") to specify the discretionary access control

This runs into problems immediately, because subjects with high clearances may often need to write to objects at a lower security level. The idea that people working at Top Secret *only* ever work at Top Secret is very stupid and immensely damaging.

Thus, the transfer of information from a high-sensitivity document to a lower-sensitivity document may happen in the Bell–LaPadula model via the concept of trusted subjects. Trusted Subjects are not restricted by the Star-property. Trusted Subjects must be shown to be trustworthy with regard to the security policy

Consequent to these rules, users are able to create and write at their level and upwards: that is, a researcher working on a document marked UK SECRET can write/append content to a document at UK TOP SECRET. Write is a tricky one here, because the Unix model implies that 'write' access includes 'read' access - but in actuality this model would not permit a researcher at UK SECRET to read a document at UK TOP SECRET.

Contrast with [[Biba model]], which only concerns itself with [[data integrity]]