---
alias: [IDS]
---
An intrusion detection system is an automated system whose purpose is to identify unauthorised intrusion onto a network or host. They may use pattern recognition and traffic analysis to achieve this goal. 

## Vulnerability assessment
This examines the current security state of a network. It might look at open ports, what software is being run, which version (including patch number), network topology, etc. This naturally relies on good ideas of what 'vulnerable' means; [[Log4j]] and [[Solarwinds]] were evidence that having a inventory of software and their versions is a necessary tool.

## Misuse detection
Misuse detection looks for attack signatures. Attackers are lazy, and if a pattern works once, they figure it'll work again and more than likely try automating it. Capturing these signatures and comparing them to events observed on a network enable us to identify potential misuse and bad actors.

