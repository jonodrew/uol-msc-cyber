## Learning objectives
- reason about what makes software secure
- identify why security is challenging to benchmark, and make use of different strategies
- make use of resilience to enhance protection of systems

## Reading
- [[Computer security#Chapter 13: Security evaluation]]

## Lesson 1: [[secure design]]

## Lesson 2: [[engineering frameworks]]

### Critical thinking exercise – Secure design

#### Purpose:
Learn how to identify secure design applied in real-world systems today.

#### Task
Select a real-world software or operating system you would like to examine in detail (note: you are supposed to spend three hours on this task, this is much longer than usual). Now pretend you are the designers that were responsible for architecting this system. Retroactively break down the key components that make up the system, propose a threat model and how each sub-component of the system is connected with the others (note: it will be faster to do this task for a piece of software than for an OS, but attempt an OS if you feel brave enough). Identify which of the Saltzer and Schroder principles (see [[secure design]]) have likely been adopted, how the software/OS abides by [[STRIDE]] and what it would have done if it had followed the [[engineering frameworks#Microsoft security development lifecycle|SDL]] framework. This is a creative critical thinking exercise – you can make use of UML diagrams to break down the system. The way you break down/describe the system does not need to be perfect, but you should make use of diagrams and best-guesses to outline how the system may have been built and identify any (likely) security flaws (based on existing documentation online or reasonable assumptions). Would you have done anything differently to make it more secure?

#### Optional
Share your findings on the discussion forum and read others’ examples.

#### Response
As a refresher, here are the principles:
- Economy of mechanism: Keep the design as simple and small as possible.
- Fail-safe defaults: Base access decisions on permission rather than exclusion.
- Complete mediation: Every access to every object must be checked for authority.
- Open design: The design should not be secret.
- Separation of privilege: Where feasible, a protection mechanism that requires two keys to unlock it is more robust and flexible than one that allows access to the presenter of only a single key.
- Least privilege: Every program and every user of the system should operate using the least set of privileges necessary to complete the job.
- Least common mechanism: Minimize the amount of mechanism common to more than one user and depended on by all users.
- Psychological acceptability: It is essential that the human interface be designed for ease of use, so that users routinely and automatically apply the protection mechanisms correctly.
- Work factor: Compare the cost of circumventing the mechanism with the resources of a potential attacker.
- Compromise recording: It is sometimes suggested that mechanisms that reliably record that a compromise of information has occurred can be used in place of more elaborate mechanisms that completely prevent loss.

I will be considering the UK government's flagship notifications service, gov.uk/notify. Immediately we can see that the fourth principle, open design, is met: [all of the code is open-sourced](https://github.com/search?q=topic%3Agovuk-notify+org%3Aalphagov&type=Repositories). Then we ask: is this well-architected? What is the threat model?

There is a clear economy of mechanism in this software. The design is broken down over multiple applications which communicate via a web-based API, ensuring that access to each sensitive object is checked for authority.

Users of the system are required to use a second factor when they access the system through the web interface, but the web API only requires a single factor

## Lesson 3: [[Resilience]]