Virtualisation is a mechanism that allows multiple [[operating system|OS]]s to run concurrently on the same hardware. This allows isolation of each OS from the other, resulting in each OS itself and others as logically separate. If one of these instances is compromised, it can be replaced. We can also take snapshots, allowing us to deploy known-clean instances of an OS

## unhosted/hosted virtualisation
It is possible to deply virtualisation directly into a hypervisor, or onto a host OS. The second type is slightly less efficient, because the host OS will consume some of the resources available on the hardware.

## Benefits
- Because they're built from the OS up, each virtual machine is isolated from the others. This limits contagion from malware
- virtual machines can be further configured to have limited access to the underlying hardware
- deployment is faster than traditional configuration of a physical server