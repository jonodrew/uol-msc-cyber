## reading
- [[CYM090 - syllabus.pdf]]
- [[What is data privacy?]]
- [[Privacy and online rights knowledge area]]
## 1.1 Introduction to #privacy as a concept
### interview with [[Maryam Mehrnezhad]]
- works on emerging technologies, eg [[IoT]]

## 1.2 Why is privacy important?
- socio-legal definitions:
	- drawing first from UN Universal Declaration of Human Rights, Art.12
		- "No one shall be subjected to arbitrary interference with his privacy, family, home or correspondence, nor to attacks upon his honour and reputation. Everyone has the right to the protection of the law against such interference or attacks."
	- Warren and Brandeis (1985) define privacy as 'The right to be let alone'
	- Rouvroy and Poullet (2009) define it as 'The right to informational self-determination'
		- notice how these are getting more complex
- these definitions lack context, and don't help us as system designers to build privacy into everything we do
- enter the #CyBOK 
## 1.3 [[confidentiality]]
- 🚨 Dictionary definition alert 🚨
- it's about keeping information secret
### Scenario 1: trusted recipient, untrusted [[network]]
- we use [[end-to-end encryption|E2EE]]
- messages should also have [[integrity]]
- and we should have [[entity authentication]] as well to ensure we're actually talking to the people we think we are
### Scenario 2: untrusted recipient, untrusted network
- if we don't trust the recipient, we might want to use [[obfuscation]]

