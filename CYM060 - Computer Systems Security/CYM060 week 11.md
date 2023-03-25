## Mock exam

### Question 1
(a) The Von Neumann architecture introduced flexibility in programming, by enabling users to store programs as data, rather than as part of the machine itself. This in turn means you can write programs that alter data and, since programs _are_ data, you could write a program that writes or alters another program.

This immediately opens the door to malicious programs. To alter the programming of Colossus or ENIAC, for example, you would need physical access to the machine, an awful lot of time, and probably a spanner. To alter the programming of a computer with a Von Neumann architecture, you only need to alter some data, or find some way of making the computer run a program to make that alteration itself. Such alterations might damage the program itself, the operating system, or even the memory of the machine. This attack could be conducted by an attacker, but it might also be a result of a bug introduced by the software engineer who did not anticipate the program being used in a particular way.

Despite these new risks, computing continued down this path and built in mitigations against such attacks, such as memory protections and access controls.

(b) The only truly secure system is not necessarily one that is unusable. It is difficult to imagine the damage one could do with a calculator, for example. However, beyond such trivial examples of fixed-program systems, security starts to come at a cost to usability. This is because, as stated above, most modern computing uses (or at least has evolved from) the Von Neumann architecture.

As noted above in 1.a, programs that can modify other programs, as well as stored data, present a significant risk - both from malicious outsiders writing programs designed to do such things, and benign programs acting in unexpected ways. Nonetheless, users must be able to modify data, because that is the purpose of a modern computer system - to store user data and to allow the user to modify it.

Indeed, modern systems are so complex that calculating every possible interaction of all of the software that might interact is almost completely impossible. There are two broad approaches to assuring a system's security: 