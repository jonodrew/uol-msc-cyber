Set text for [[5. CYM010 week 5]]
And [[CYM070 week 1]]
## Chapter 1
Learning objectives
1. Describe the key security requirements of [[confidentiality]], [[integrity]], and [[availability]]
2. Discuss the types of threats and attacks that come out way, and discover examples of them and their application to different categories of [[asset]].
3. Summarise the [[functional requirements]] (oh-no.jpg) for computer security
4. Explain the fundamental security design principles
5. Discuss the use of [[attack surface]] and [[attack trees]] (ooh! they're a bit like [[cyber kill chain]], except not trademarked and wanky!)
6. Understand the principle aspects ofa  comprehensive security strategy
### 1.1 Computer security concepts
We cover the same boring things from [[NIST]] that we did last week, and the week before that. Then we tack on two new ideas: [[authenticity]] and [[accountability]]
### 1.2 
Nothing interesting here, skipping
### 1.3 Security [[functional requirements]]
Security is hard, not because technology is hard - it is - but because people are a bloody nightmare
### 1.4 Fundamental security design principles
Alrighty. Here's a list from a US government body:
1. Economy of mechanism: don't make it any more complicated than it has to be (recognising that sometimes it has to be complicated)
2. fail-safe defaults: the default position should always be to prevent or disallow access.
	1. This is a little contraversial, and I think should be flexed according to business need
3. complete mediation: every action should be checked against the access control mechanism
	1. In its most extreme form, this means every autosave requires checking if the user still has the same permissions they had 30 seconds ago. This is probably why its not implemented.
4. open design: [[make things open, it makes things better]]
5. separation of privilege: pull apart the privileges an action requires and ensure that only actors with all of them can conduct an activity. That is: 'superadmin' is, generally speaking, a Bad Thing. See also AWS Lambda, where each Lambda has its own specific role and set of permissions within that role 
6. least privilege: only ever use the lowest level of permissions you need. Production access is not a thing that people should need at all.
7. least common mechanism: not sure I get this one. The book says "minimise the functions shared by different users, providing mutual security"??
8. psychological acceptability: I love this one, on the other hand. Security should be transparent to the user, and should reflect their mental model of protection. Otherwise they'll turn it off: users need to be able to do their jobs, want to be able to do their jobs, and will get round anything we put in place to effect that.
9. isolation: Don't put things together unless you have to. That may mean physical network separation or even an [[air-gapped]] system in extreme cases. It also means separating user profiles, their software, their data, and so on. This is particularly pertinent, and interesting, with the growth of [[public cloud]]. Finally, isolate backups and [[key]] material from the systems where they're used.
10. encapsulation: we love [[object oriented programming]], and the theoretical benefits from encapsulation - because they mean that callers of the software can only access the interface of the software, and not its internal data structure.
11. modularity: build once. Use everywhere.
12. layering: [[Swiss Cheese model]], but also [[defense in depth]] 
13. least astonishment: don't surprise people, basically. Things should act, and fail, as users broadly expect
## 1.5 [[attack surface]] and [[attack trees]]
## 1.6 Computer security strategy
