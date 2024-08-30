>[!quote] Security experts frequently refer to people as "the weakest link in the chain" of system security. \[...] However, more enlightened researchers have pointed out that current security tools are simply too complex for many users.
>
>\- Angela "Sass is my middle, _and_ my last name" Sasse
- introduces the word 'panorama' to stand in for the real-world context
- thus there are three nicely alliterative elements: product, process, panorama
- product:
	- what do current security mechanisms and policies require from different stakeholders?
	- is that work an acceptable load, from a mental and physical perspective?
	- what does it cost the organisation, both in terms of pound-amounts but also staff-hours?
- process:
	- security being considered a 'non-functional requirement' is an anti-pattern, because it assumes that users don't interact with security
	- far better to design security the way we design everything else. 
	- For example, security might suggest encrypting a giant database full of personal data. That's a good security approach, unless analysts need constant access to it. If it takes five minutes to decrypt every time an operation is run, sooner or later they'll just download a copy of the data so that they can do their work more effectively - but it sure as hell won't be _secure_
- panorama
	- context is key
	- context includes the culture of the place where the work is happening
	- a positive security culture makes the extra work of security more understandable, and therefore users are less likely to work around these controls
	- it also includes monitoring and feedback for those users who aren't complying - feedback either to the design team, if there are thematic issues, or feedback to the user's line manager if they are just non-compliant
		- design that is bad for minorities is easy to confuse with non-compliance, so do the user research first!
	- education is also vital, with a view to giving users a personal understanding and stake in securing their work
	- political, ethical, legal, economic constraints around the system will impact both the design and the way the system is used
- Users fail to behave the way we expect because:
	- they can't
	- they don't want to
- Brostoff and Sasse found that if you allow ten strikes, successful logins increase to 93%
>[!quote] Security experts are often inclined to reject proposals for improving usability (such as the ones listed earlier) because the help given to users might help an attacker.
- the goal of security is to build systems that are actually secure! Not theoretically secure!
- badly designed security is just expensive!
- paper distinguishes between 'production tasks', which move the user towards a goal, and 'supporting tasks', which are not essential to achieving the goal
	- snuck in there is a really interesting taxonomical distinction
	- if we change peoples' minds to see that security is a production task, they'll be more likely to do them