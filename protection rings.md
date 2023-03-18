A security feature in an [[operating system|OS]]. In theory, there are four rings:
0. Ring 0 is core to the [[operating system]]. It has the highest [[privilege]] and is necessory for [[memory protection]] and management.
1. This ring is for I/O, including OS components like hardware drivers
2. This ring is for high erlevel structures and services, like the [[network stack]] and [[filesystem]]
3. This is where user-level applications live. They get as little privilege as possible and are fundamentally untrusted

Unfortunately, most OS vendors do not use four rings. They use two. Processes are either ring 0 or ring 3.

This is obviously fine.

## principles
- each ring may access itself
- each ring may access all rings outside itself
- no ring may access a ring that is inside itself
By induction we can see that ring 0 can access everything.

## immediate exceptions to these principles
Outer rings can indeed access inner rings, but in extremely controlled ways. They do it by means of controlled invocations, which are also known sometimes as system calls.

## protection rings in hardware
Below the [[operating system]] (ring 0) exist a whole pile of other things. Researchers have taken to numbering them with negative numbers as follows:
- virtualisation/hypervisor layer: ring -1
- firmware layer: ring -2
- hardware/chipset: ring -3
As above, the lower we can compromise the system, the more control we have.