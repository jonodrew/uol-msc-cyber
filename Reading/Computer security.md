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

## Chapter 2: Managing security
- Security is hard
- people are important
### 2.2: Measuring security
- We can establish a "security measurement", which is either quantitative or qualitative.
	- Quantitative measures might be things like "number of ports open" or "is the machine patched to the most recent version?"
	- Qualitative measures are fuzzier and might include ideas like "company reputation" or "employee opinion of the security team"
- we can then try to compare these measures with the values we recorded the previous time, and see if we've "improved"
	- "improved" is sort of a tricky thing again - if the business has grown and we're employing more developers, who are generating more bugs, are we less secure? Or more secure because we have better financials?
- Some branches of some industries have banded together and come up with standards, such as the [[PCI DSS]]. There are also standards like [[ISO 27001]]. 
### 2.3: [[risk]] and [[threat analysis]]
- "hazard risks" are damaging events, while "opportunity risks" are events that may be positive
- there's a disaster of a diagram here that identifies a product lifecycle as "design --> implement --> operate" which I thought we did away with in like...1991
- it is important to know what [[asset|assets]] you are defending before you try defending them
>[!quote] Identification of assets should be a relatively straightforward systematic exercise
	- gods bless academics
- we now turn to [[threat|threats]]
- then to [[vulnerability|vulnerabilities]]
- and then to [[attack|attacks]]

#### Measuring risk
Now that we've accurately measured our assets, threats, and vulnerabilities all we need to do is multiply them together (with likelihood) to get our risk. 

Hah, nope. All of our inputs are garbage. And as they say: GIGO.

We can try applying quantitative risk, using probability theory or even [fuzzy theory](https://en.wikipedia.org/wiki/Fuzzy_logic). However, because we lack precision in our inputs, the answers may be off. Way off.

There is a qualitiative approach too, where we rate things on a ten/five/three/seven/whatever point scale, and then map those across to numbers. [[Common Vulnerability Scoring System|CVSS]] and [[DREAD]] both use this approach.

Once we've measured risk, in theory we should have a prioritised list of things to manage. Conducting a full risk analysis seems like a great idea, but must be done quickly: the world, and the system, will keep changing. Even the analysis itself is subject to change, particularly if human beings are doing the analysis. Criteria start to drift, and people leave midway through.

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
	- [[buffer overflow]] (the book calls it overrun, because...why). A value is assigned to a variable whose memory buffer is too small to contain it. Consequently the data overflows the buffer into ajoining cells. This is...bad, and again breaks logical separation
	- backups: a great way to get hold of data that you know the organisation cares about!
	- core dump: programmers want to be helpful and so when a computer crashes it vomits out its internals to help with debugging. Unfortunately, some mischevious person might try to intentionally crash a system, so that they can look through the internals. Naughty!
### 3.6 THE LAYER ABOVE
- Seriously loving the ominous titles here lads
- A really...interesting point here. Gonna quote it for later
>[!quote] it is neither necessary nor sufﬁcient to have a secure infrastructure, be it an operating system or a communications network, to secure an application.  
Gollmann, Dieter. _Computer Security_, Wiley Textbooks, 2011. _ProQuest Ebook Central_, http://ebookcentral.proquest.com/lib/londonww/detail.action?docID=819182.  
Created from londonww on 2023-01-09 12:33:00.

Erm. Really?

## Chapter 4: [[identification]] and [[authentication]]
### 4.1: username and password
- Identification is here described as the action the user takes: the identify themselves as Alice
- authentication here is explicitly described as the same thing as [[entity authentication]]
- so let's start with the basics: a thing the user knows. A [[password]]

## Chapter 5: [[access control]]
- once again we go over the flow of access control:
	- a subject attempts to operate on an object. This attempt is moderated through a [[reference monitor]] of some sort.
	- a subject acts on behalf of a principal, which should represent a human user
- in the [[Bell-LaPadula model]] there are four access rights: read, write, execute, and append. 'append' is the right to write (ugh) to the end of a file without reading what's previously been written, while a regular 'write' is the right to write wherever the subject wants (which requires the ability to read)
- SO MUCH UNNECESSARY MATH
 ![[Pasted image 20230221192920.png]]
- I really hope this doesn't come up in the exam. What a strange way to express human-computer interactions

## Chapter 6: [[reference monitor]]
### 6.1: Introduction
- a review of the [[reference monitor]]
### 6.2: [[operating system]] [[integrity]]
The Platonic ideal has been achieved and the operating system can enforce all [[access control]] policies. Well done. What next?

The next step for an [[attacker]] is going to be to target the operating system itself. The [[threat model]] assumes an attacker who has access to the command line but not the underlying physical hardware.

So now we have a new requirement: the user must not be able to modify the operating system, even as they are able to _use_ the operating system. We achieve these aims through modes of operations and controlled invocation

#### Modes of operation
The operating system must distinguish between actions on behalf of the operating system itself, and operations on behalf of a user. A system may work in dual-mode operation, where the dual modes are a "user mode", where instructions that are non-critical security instructions are performed, and "supervisor/root/kernel/monitor/system mode", where privileged instructions are carried out.

The processor's [[control register]] has a hardware-level status flag that distinguishes in which mode the system is currently operating. Generally this only requires one bit, as there are usually only two modes. Is this the best model? Probably not, especially when we've previously wanged on about [[protection rings]].

#### Controlled invocation
However, simply flicking that bit whenever the user wanted to do something ~~dangerous~~ would just let them do dangerous things. Instead, we hand control over to a function that does one thing (the dangerous thing) and then hands the result and control back to the calling function. c.f writing Roles for AWS Lambda.

### 6.3 Hardware security features
- the deeper you push the security controls, the simpler they can be
- the simpler they are, the easier they are to test and assure
- the simpler they are, the greater the reduction in performance overheads
- the decisions a reference monitor has to make are arcane and far removed from the needs of the user, so it's best to abstract them away and never let the user worry about them

#### Processes and threads
A process is a program in execution, and so comprises executable code, data, and the execution context. Contrast this with threads, which are strands of execution within a process, sharing the same process address. 
#### Interrupts/exceptions/traps
Any error in a program, whether it's a user request, a hardware failure, or a developer mistake, is handled by an exception. This is a special input to the [[CPU]] which includes an address, called an interrupt vector, which is stored in an interrupt vector table. The interrupt vector table gives the location of the program which deals with the condition specified in the exception. The program that handles the exception is called the interrupt (exception) handler, because naming things is hard.

When an exception is raised, the system saves the current state on the stack and then executes the handler, which takes control away from the user-initiated process. The handler ensures that the system is reset to a known safe state before returning control to the user process.

This raises an interesting vector for an [[attack]]: if you can change an entry in the interrupt table so that it points to attack code, you just have to force that exception to be raised

As a side note, when we think about processes asking other processes to do things, we have to consider [[the confused deputy problem]]

### 6.4 [[memory protection]]
#### [[memory protection#Secure addressing]]

## Chapter 7: [[Unix]] security

## Chapter 8: [[Windows]] security

## Chapter 11: [[Bell-LaPadula model]]

## Chapter 12: Security models
- aie we're still banging on about latices and set theory

## Chapter 13: Security evaluation
This chapter is very dull. If it comes up in the exam, duck

- we follow the terminology of the [[Trusted Computer System Evaluation Criteria]], apparently
- we distinguish between evaluation, accreditation, and certification:
	- evaluation: assess whether a product has the security properties it claims it has
	- certification: assessing whether a product is suitable for a given application. This naturally relies on an evaluation having been done
	- accreditation: an executive decision to use a product in a given application. The product will necessarily have been certified before such a decision can be made
- this chapter focuses on evaluation
- We should pay attention to the target of the evaluation, and the thin line between systems and products
- products are things we buy off the shelf, as-is (see [[Wardley map]]), while systems are custom-built
- products are theoretically easier to evaluate, but may not meet requirements
- systems built to specific requirements are more expensive to evaluate but are probably more likely to meet the requirements
### The method of evaluation
Whatever method is used, it should have two qualities:
- repeatability: conducting the test at a different time with the same product should yield the same answer, and
- reproducability: a different team conducting the same test on the same product should find the same result

Evaluation can be process- or product-oriented:
	- product-oriented: examine and test the product itself. Different evaluations may give different results, however, as different testing teams may pick up or miss different things
	- process-oriented: examine the process by which the product is made, but ignore the product itself. This is on the basis that if the process of making the product follows best practice, the outcome should also align to best practice. There is an open question as to how true this is.

### Legal/organisation framework
Additionally we also consider the organisational and legal framework of the evaluation process. For example, there might be a government agency or an accredited private enterprise empowered to conduct evaluations.

A government body may or may not charge for evaluations. As long as the evaluation is carried out in-house, there are fewer organisational overheads. However, with the public sector come limited funds, and a danger of long backlogs

Private evaluations are an answer to this problem, but bring their own issues: commercial pressures can lead to corners being cut.

## Chapter 14: [[cryptography]]

## Chapter 17

### 17.3: [[firewall|Firewalls]]

### 17.4: [[intrusion detection system|Instrusion detection]]