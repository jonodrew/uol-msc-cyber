## notes
>[!quote] security and user-friendliness are not mutually exclusive quality features of a system

- ref [[Users are not the enemy]], [[User-centred security]] and [[Why Johnny Can't Encrypt]]
- ahah, a fairly liberal reading of [[Kerckhoffs' six principles#Easy to use]]
	- He was talking specifically about [[cryptosystem]]s, but the authors have fudged it a bit to talk about security systems more widely. I like it
- [[Saltzer and Schroeder]] get a shout as well, for their [[Computer Security principles and practice#^7a4905|psychological acceptability]] principle. Specifically, that the user's mental model should match up to the mechanism
	- which is made significantly harder by stuff like [[asymmetric|asymmetric encryption]] which fundamentally nobody has a good mental model for
- Transparency is important, but can also be overwhelming. For example: if your software just tells people "That's a bad password", that's not transparent and it's bad. Adding context, such as "How about these three words", or "consider adding numbers/letters/symbols", or "that's the same password you used last time, which means it'll be easier for an attacker to guess" helps the user understand what they need to do next
- However, too much detail overloads the user, so there's a balance to be struck
- could personalisation be useful in terms of changing behaviours? If so, what are the divisions?
- ah, a reminder that places like LinkedIn encourage you to breach the privacy of others for the platform itself
	- work for free for your corporate, robotic overlord!