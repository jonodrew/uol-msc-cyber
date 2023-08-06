This week we look at the hacking lifecycle, hacking techniques and common tools used by different types of hackers. This is followed by how important digital forensics is in gathering evidence and the need to follow the four principles of digital evidence covered by the ACPO Good Practice Guide for Digital Evidence.

### Learning Objectives

---

- Summarise the four principles of digital evidence as outline by ACPO
- Explain the main techniques used by hackers to attack system
- Explain the importance of digital evidence in investigations and how to gather it
- Outline the hacker attack cycle and demonstrate how stages of the lifecycle link to hacking tools

## Reading
- [[Cybercrimes - Critical issues in a global context]], pp. 53-58

## Lesson 1: Hacking is illegal
- hacking is the act of trying to gain access to a computer system that you do not own
- it is 100%, no messing around, no funny business, illegal
- right?
- right.
- like even if you try and fail, you're still doing the thing, and you may still be prosecuted
- [[penetration testing]] is the legal, consensual hacking.
	- Risk Aware Consensual Hacking, kids
- the lecturer absolutely bodying the skiddie community here
- hacking is, however, very fun
	- this makes convincing teenagers not to do it very tricky
- hacking tools are illegal
- pen-testing tools are not
![[Pasted image 20230801182203.png]]
- to cover one's tracks, one might use:
	- a [[virtual private network|VPN]]
	- the [[Tor]] browser
	- a virtual machine
	- operating systems such as [[Kali Linux]]
- Google is your friend for [[open-source intelligence|OSINT]]
	- there are a number of advanced operators
- Google Hacking Database --> Google Dorks
- *many IP cameras are free to access*
- Censys.io and zoomeye.com are handy tools in this space
- additionally, [[Shodan]] is a perennial fave for identifying open ports
## Lesson 2: hacking!
- hacking cycle
	- more possible now that bikes are electronic
- Phase one: reconnaissance
	- social media
	- remote access
	- [[open-source intelligence|OSINT]]
- Phase two: scanning
	- ping or Nmap to identify potential open ports
	- Nessus for vulnerability identification
	- Network mapping
- Phase three: ingress
- Phase four: maintain access and move laterally (living off the land)
- Hack the Box and Over the Wire are fun for practising hacking
	- NOT NOW, JONATHAN
- Software has bugs
![[shocker-shocked.gif]]
- Finding and selling exploits is not illegal, but using them is
- "Blackhole exploit pack" is the market leader in exploit services
	- there's a phrase I never expected to write
## Lesson 3: Digital forensics
- Digital evidence is fragile, and should be recorded as soon as possible
- [[Locard's Exchange Principle]]
- [[ACPO Good Practice Guide for Digital Evidence]]
- [[The Case of the Stolen Exams]]

## Lesson 4: Mobile forensics
- [[Encro chat]]
- [[Regulation of Investigatory Powers Act 2000]]