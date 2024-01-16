## Reading
- [[Internet Crime Report 2022]]
- [[Thinking Security (Stopping Next Year's Hackers)]] chapter 2
- [[Computer Security principles and practice#1.1 Computer security concepts]]
- [[Computer Security principles and practice#1.2]] to [[Computer Security principles and practice#1.5 attack surface and attack trees]]
- [[Security in computing#1.1]]

## 1.1 Why [[software]] security?
- we're going to review [[security service|security services]]!
### types of [[attack]]
- [[malware]]
- [[DDoS]]
- [[insider|insider threat]]
### case studies
- [[Solarwinds]] again!
- [[Colonial Pipeline]]
- [[University Hospital Dusseldorf]]

## 1.2 Security concepts
- we're doing [[CIA triad]] again
- [[Alice]] and [[Bob]]!!
- [[confidentiality]]:
	- things that are private stay private, even if they're intercepted
- [[data integrity]]:
	- consistency is key
- [[authentication]]
- [[non-repudiation]]
- [[malware]]
- [[vulnerability]]
- [[exploit]]
- [[attack vector]]
- [[security patch]]
- [[encryption]]/decryption
- [[threat]] -> [[attack]]
- [[phishing attacks]]
- [[sql injection]]
- [[cross-site scripting]]
- [[principle of least privilege]]
- [[Secure by Design]]
- [[defense in depth]]
- [[fail-safe default]]
- [[economy of mechanism]]
- [[complete mediation]]
- [[Kerckhoffs' six principles#Open Design]]
- [[Secure Software Development Lifecycle]]
## 1.3 Vulnerabilities/threats/exploitation

## 1.4 Come up to the lab...
- Do not run malware on your own machine
	- This was said with the weariness of a man who's found that it doesn't matter how many times he says it, he's going to get an email saying "I busted my host because I ran malware"
- If you're running malware in a virtual machine on a host you own, the VM network interface should be host-only
	- Not NAT
	- Not bridged
	- HOST ONLY
- Have you checked that it's host only?
- bootstrap script called 'Flare VM' that gets a windows machine set up as an analysis tool
- [[REMnux]] is an analysis flavour of linux. Might even be an [[Ubuntu]] fork
	- hey it has [[CyberChef]]!
- 