Author: [[Dieter Gollman]]

## Chapter 1: History of computer security

### 1.1 The dawn of computer security
- more like the yawn of computer security, amiright
- Consider the evolution of computer security
	- 70s: mainframe (centralised)
	- 80s: personal computer (decentralised)
	- 90s: [[Internet]] (decentralised network)
	- 2000s: the web (??)
- I'd probably conclude these with 2010s: the cloud, and 2020: the internet of things
### 1.2 Mainframes
- multiple users meant researchers had to find ways to separate access rights and permissions, and store data securely in case folks went snooping
- introduction of [[cryptography]], specifically [[asymmetric|public-key encryption]] (which is strange to introduce here imo - it's mainframe disk encryption is more likely to be [[symmetric|symmetric encryption]], I would have thought)
### 1.3 Personal computers
- a personal computer means a single-user system, at which point we completely abandoned everything we'd learned about multi-level and multi-user security
	- surely that won't be needed again?
- the first [[worm]] was sighted
### 1.4 [[Internet]]
- The Internet was a mistake
- Connecting your personal, unprotected machine to a vast network of other machines?
	- foolishness
- The 90s saw the beginning and end of the crypto wars, where for a short time mathematical formulae became **squints** weapons subject to...export control?
	- wait, seriously?
### 1.5 The web
- that centralised web of servers, accessed via the browser/an app on your device
- now your device is tiny, and fits into your pocket!
- and any idiot can code an application accessible to the entire world
	- well, not the entire world. See [[China]]
- this has increased the number of vulnerable applications, and the ways in which the public's data can be stolen, by a factor of several million. Hooray!

## Chapter 3: Foundations of computer security
### 3.1 definitions
Nothing new here, so there are no notes

### 3.2 The fundamental dilemma of computer security
- Please don't be "usability or security"
- oh, it's not. It's:
>[!quote] Security-unaware users have speciﬁc security requirements but usually no security expertise.  
Gollmann, Dieter. _Computer Security_, Wiley Textbooks, 2011. _ProQuest Ebook Central_, http://ebookcentral.proquest.com/lib/londonww/detail.action?docID=819182.  
Created from londonww on 2023-01-09 11:13:39.

(I am not entirely sure that's actually a di-lemma. What's the lemma? Where's the di?)

### 3.3 Data vs information
- data is a metric about the world
	- remember that our metrics may be incorrect
- information is an interpretation of that metric
	- data: increased heartrate
	- information: patient may be stressed, in love, scared, have high blood pressure
### 3.4 principles of computer security
- bake it in at the beginning
- it's not that hard
- seriously
- please
- the book proposes a two-dimensional approach to desigining security. The first axis is user-resource, and the second is software-hardware
- let us consider that [[integrity]] could also be phrased as "compliance with a set of rules"
- this immediately open up the question of "what rules", and "who/what is subject to these rules?"
	- which users are allowed to read/write a specific data item
	- what operations may be performed on a data item
	- what format or content a data item may have
- (you can see how this flows quite easily into [[object oriented programming]])
- then we move on to the question of where the control should be placed and applied:
	- application?
	- services?
	- OS?
	- OS kernel?
	- hardware?
- each level will require a different kind of engineering, and must interact nicely with the levels below and above
	- below hardware is physics, and it's super important you play nicely with physics
	- above application is the user, and you really really have to play nicely with them
- boo for over-use of "man" to mean "person". 
	- minus ten points from Dieter
- there is a trade-off to be made in terms of complexity versus assurance. That is, assuring a complex system is almost impossible
	- cf. [[Cynefin]] and how complex systems react to being probed
- we can say that, broadly speaking, "feature-rich security systems and high assurance do not match easily"
- we might also want to ask whether we should centralise or decentralise our controls
	- This is a fascinating question and is significantly broader than computer security. We might also apply it to onboarding checks, employee vetting, recruitment, software standards...
	- there's a [[Wardley map]] here for sure
	- centralisation makes enforcement easier in theory, but in practice results in either a bottleneck or a massive and expensive single entity. Conversely, distribution is efficient but also requires constant alignment, which anyone who works in a distributed setting can tell you is a total fucking nightmare
### 3.5 THE LAYER BELOW
- sounds ominous lads
- it's not. The question is, how do we prevent an [[attacker]] from getting access to a layer below the protection mechanism
- because once that happens, it's game over: your application level protections are worth nothing if an attacker has [[pwned]] your operating system
- here are some fun examples of how an attacker might access low-level parts of a computer system
	- recovery tools: they're used as part of recovery to examine the physical structure of data on a disk when the logical representation is destroyed. However, this is also an excellent way to get to files when the OS is rudely telling you you're not allowed to access them
	- object reuse: if the previous process left some data in the memory allocated to the new process, then the new process might read something it's not supposed to. This breaks logical separation
	- buffer overflow (the book calls it overrun, because...why). A value is assigned to a variable whose memory buffer is too small to contain it. Consequently the data overflows the buffer into ajoining cells. This is...bad, and again breaks logical separation
	- backups: a great way to get hold of data that you know the organisation cares about!
	- core dump: programmers want to be helpful and so when a computer crashes it vomits out its internals to help with debugging. Unfortunately, some mischevious person might try to intentionally crash a system, so that they can look through the internals. Naughty!
### 3.6 THE LAYER ABOVE
- Seriously loving the ominous titles here lads
- A really...interesting point here. Gonna quote it for later
>[!quote] it is neither necessary nor sufﬁcient to have a secure infrastructure, be it an operating system or a communications network, to secure an application.  
Gollmann, Dieter. _Computer Security_, Wiley Textbooks, 2011. _ProQuest Ebook Central_, http://ebookcentral.proquest.com/lib/londonww/detail.action?docID=819182.  
Created from londonww on 2023-01-09 12:33:00.

Erm. Really?

## Chapter 14: [[cryptography]]