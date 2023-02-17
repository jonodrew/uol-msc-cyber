I should write a blog post on this. It's got everything. [[digital signature]], [[asymmetric|asymmetric encryption]], [[data integrity]]...

Alright, let's go gang. How do we secure the [[DNS]]?

With [[digital signature]]! Specifically, we ask each name server to sign the response. How can we trust the signature? We can check the [[public-key certificate]], which should be signed by the next name server in the hierarchy. Yeap, it's more [[public key infrastructure|PKI]]. 

This approach adds a number of new [[DNS#Resource records|resource record]] types, including: 
- RRSIG, which contains the digital signature computed over a set of resource records. It may also contain a timestamp to limit the potential of [[replay attacks]]
- DNSKEY, which contains the [[public key]]
- DS, the Delegation Signer, whoch contains a cryptographic hash of the DNSKEY record
When DNSSEC is implemented, each answer to a DNS query contains an RRSIG in addition to the requested record type. 