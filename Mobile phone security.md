GSM -> 3G -> LTE -> 4G

### What [[security service]] do we need here?
|service|detail|needed|
|-------|------|-------|
|[[confidentiality]]|should people be able to intercept phone calls? Definitely not. We should have confidentiality|Yes|
|[[data integrity]]|data in a phone call should be provably the same, so I'm going to say yes to this|Yes|
|[[data origin authentication]]|we should be confident that the data is really coming the the caller we think it is...so yes?|
|[[non-repudiation]]|we should be able to prove that the data came from a device, but we'd probably do that at the device level, rather than the connection.|No
|[[entity authentication]]|It's definitely important that we know who's accessing the network. However, this was not specified at the time of the development of [[GSM]], so it's not included there.|No


