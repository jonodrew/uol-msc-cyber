A reference monitor is an abstract control concept. The [[security kernel]] is the implementation of that abstract idea, and the [[trusted computing base]] is the totality of the protection mechanisms within a compute system - including the security kernel.

## Requirements
- The reference validation mechanism must be tamper-resistant
- The refernece validation mechanism must always be invoked
- The reference validation mechanism must be small enough to be subject to analysis and tests to be sure that it is correct

## Where to place a reference monitor
Given that a reference monitor is an abstract concept, and not a specific thing, it can be placed just about anywhere. For example:
1. In hardware
2. In the [[security kernel]], which might be in the form of a [[hypervisor]]
3. In the [[operating system]] itself: [[access control]] is an example of a reference monitor
4. At the service layer - for example, [[roles-based access control|RBAC]] on something like a database
5. At the application layer, for example in the code itself
We should also consider where to place the reference monitor in relation to the program it should mediate access (to/from). For example, a reference monitor in the kernel protects the kernel from incorrect or inappropriate requests. 

Equally, we could place the RM in an interpreter, to moderate the running program's access to the outside world - as is done in the [[Java Virtual Machine]]. 

## Inspect or modify
Consider that there are a few ways in which a reference monitor can inspect or even modify a program.
1. An execution monitor only looks at the history of execution steps but does not try to predict the outcome of future steps
2. By contrast, a reference monitor could consider all future possible executions of the program when deciding whether to grant permission. The static type checker in the Java language family is an example of this
3. The reference monitor could rewrite the program (what??) to ensure that granting the access request would not lead to the violation of a security policy