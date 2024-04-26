## Abstract (abstracted)
- what if privacy, that could also be broken at any point?
- literally the first line is "Messaging systems are used to spread misinformation and other malicious content, often with dire consequence"
## Notes
### path traceback
- idea one is to share a [[symmetric]] key between the platform and the user, which will only be used to identify if the user has sent something that's been flagged as 'malicious'
- These they call 'tracing tags'
### tree traceback
- second idea is built on the first, and allows the platform to trace every single instance of a forwarded message
	- this could be used for cleaning up after a misinformation campaign
	- it could be used to trace people sending messages the platform, or an authority, doesn't like people sending
### implementation
- implementation relies on the platform not securing metadata
- platform has to store a trace tag for every single message on the platform
- can't get around the problem of copy-pasting content - if you receive a message, then copy-paste it into a new message, you'll be the source of a new chain
	- I think the authors assume this means you're malicious

>[!quote] The challenge of developing such policies and building moderator pipelines that can enact them will need future research; we focus on showing the cryptographic viability of performing secure tracing when it is appropriate.

_hmmm_

- the trace tags are formed into an encrypted linked list, which allows for traceability

#### goals
- Users should not learn anything about message paths beyond that which they already know (who forwarded to them; to whom they have forwarded it)
- the platform should not be able to trace the message unless it's reported
- if it is reported, the platform should only be able to trace the message, and not see the content of the message
- nobody should be able to forge a traceback, and thereby implicate an innocent user
- contrawise, no user should be able to author a message that can't be traced back to them (or the platform)