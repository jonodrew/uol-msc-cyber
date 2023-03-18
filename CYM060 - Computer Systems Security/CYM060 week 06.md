## Learning objectives
- ensure that the [[operating system|OS]] is running successfully after starting up the computer
- know when to look at hardware as a protection mechanism
- identify the main threats to boot security and possible mitigations

## Questions
1. Propose countermeasures for the following [[password]]-related security violations: 
	1. Offline dictionary attack: attacker obtains access to ID/password (hash) database; uses dictionary to find passwords. 
	2. Specific account attack: attacker submits password guesses on specific account. 
	3. Popular password attack: try popular password with many IDs. 
	4. Password guessing against single user: gain knowledge about user and use that to guess password. 
	5. Computer hijacking: attacker gains access to computer that user currently logged in to. 
	6. Exploiting user mistakes: users write down password, share with friends, tricked into revealing passwords, use pre-configured passwords. 
	7. Exploiting multiple password reuse: passwords reused across different systems/accounts, make easier for attacker to access resources once one password discovered. 
	8. Electronic monitoring: attacker intercepts passwords sent across network. 
2. Conduct a comparison between retina and iris scanning technologies – identify key similarities and differences.  
3. Read the following article:  

> Greene, T. ‘[Equifax breach proves bad employees are worse than good hackers](https://thenextweb.com/news/equifax-breach-proves-bad-employees-are-worse-than-good-hackers)’, _TNW_ (2017).

Do you agree with the title of the article? Would a proper access control mechanism have prevented or mitigated the breach in your opinion? 

4. The following three access control mechanisms were discussed in the course notes: 
	1. access control matrices 
	2. capabilities 
	3. access control lists. 

	For each access control mechanism, describe the complexity of: 
	-   determining authorised access during execution 
	-   adding accesses for a new principal 
	-   deleting all accesses for a particular principal 
	-   determining all principals which have access to a particular object 
	-   creating a new object to which all principals have access by default.   

1. What is the difference between paging and segmentation? Briefly indicate their respective advantages and disadvantages. 
2. Explain the difference between a virtual address and a physical address. Discuss the advantages of the use of virtual memory management.