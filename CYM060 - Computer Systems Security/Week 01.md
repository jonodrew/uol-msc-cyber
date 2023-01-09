## Learning objectives
- summarise the role of security mechanisms for modern computer systems, including both hardware and software
- define key terms in Computer System Security
- start thinking critically about computer systems security

## Reading
- [[Computer security#Chapter 1: History of computer security]]
- [[Computer security#Chapter 3: Foundations of computer security]]

## Lesson 1: Introduction to computer system security
- this mfer's just got a robot to voiceover his lecture
	- is this some kind of performance piece?!
- Course book will be [[Computer security]]
- There will be labs to demonstrate security issues, but this is not a penetration testing course
- Now we touch on [[authentication]] - how your identity (in the context of the system) is verified
### Critical thinking exercise: [[data breach]]
**Purpose**: Gain experience in critical thinking in relation to security by investigating and reflecting on past data breaches.

**Task**: Come up with two examples of companies that have fallen victim to a data breach. You can do this by performing an online search for inspiration (in for example, online news or press) or use your personal knowledge and experience. Investigate your two data breach cases by doing the following:

-  Explain the reasons for their security failures.
-  Compare the two examples. Where are they similar and where do they differ?

 You can use the following questions to help your thinking process:

1. Were these human failures or were they machine failures?
2. What were the consequences (harms, penalties, public responses, effects on reputation, etc.) of these data breaches?
3. What lessons do you think the companies should learn as a result?

#### Case 1: [HMRC data breach, 2007](https://en.wikipedia.org/wiki/Loss_of_United_Kingdom_child_benefit_data_(2007))
The UK's tax authority, HMRC, lost two password-protected discs in the internal mail. The password protection was simply WinZip version 8, which anyone remotely qualified could crack in minutes.

Furthermore, the data was not sanitised before sharing: significant amounts of personal data, including bank details (!) were included in the data that was to be shared.

The security manual for handling data was not made available to the staff who were tasked with this work

The chairman of [[HMRC]] resigned, and an investigation was carried out into the incident

#### Case 2: [University of Essex data breach, 2022](https://www.bbc.co.uk/news/uk-england-essex-61312383)
A supplier to the university accidentally emailed a spreadsheet of personal data. 

However, the impact seems to have been entirely negligible.

## Lesson 2
### Critical thinking exercise: differences in definitions
**Purpose**: Gain an understanding of key terms and how they differ from each other. Knowing how to use these terms both accurately and precisely will help you for the rest of the course (if you are doing other modules), not just this module.

**Task**: In your study journal, write short answers to the following questions. If the differences between these terms are not immediately clear to you, search for the terms online or ask your peers in the forum in the next activity.  Aim to provide a detailed, consistent and clear description of the terms and their differences. Note that many resources exist online and – rather unfortunately – inconsistencies often appear, often from people not applying these terms critically. Be sure to not use cyclical definitions (e.g. ‘Computer security is security of computers’).

What are the differences between:

-   a threat and an attack?
	- a threat is theoretical. An attack...is not
-   a vulnerability and an exploit?
	- as above
-   computational trust and trusted computing?
	- a branch of computer science where we try to figure out how the computer can calculate an opinion on trust, versus users trusting computers. The fools. Never trust a computer
-   computer security and cyber security?
	- well computer security is real. There's no such thing as cyber
-   confidentiality and privacy?
	- the quality of nobody being able to read your messages, which is a subset of privacy: having spaces that are entirely your own and cannot be intruded upon
-   containers and sandboxes?
	- one is a way of packaging an application. The other is where you make sandcastles!
-   hacking and attack?
	- I plead the fifth
-   impact and harm?
	- Impact is a fairly cold calculation, while harm tends to be more holistic
-   logic bomb and phishing?
	- These two things aren't connected!?
-   phishing and spear phishing?
	- well, you do one with a spear
-   safety and security?
	- Ambulances and James Bond
-   security policies and security controls?
	- we write the one and we ignore the other
-   spyware and advanced persistent threat?
	- software you should worry about versus nation-state actors you can safely ignore
-   the trusted computing base and the operating system kernel?
-   a virus and a worm?
	- RNA/DNA
-   optional: challenge yourself to come up with three of your own related terms here.
    

**Outcome**: you should now have a significantly more nuanced understanding of key terms related to computer system security.