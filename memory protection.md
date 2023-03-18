Memory protection is a critical security feature in an [[operating system]]. 

An OS manages access to data and resources - both its own and the users on the system. Thus the operating system has two [[integrity|integrities]] to maintain: its own, and that of the users.

The integrity of the operating system is maintained through logical (as opposed to physical) separation. Separation can take place at two levels:
- file management, which deals with logical memory objects, and
- memory management, which deals with physical memory objects.

Why is this distinction important? Consider the risks in [[segmentation]] and [[paging]], which are the two main ways of structuring memory.

## Secure addressing
In order for the OS to maintain its own integrity and confine each process to a separate address space, then access to data objects in memory has to be controlled. A data object is nothing more than a collection of bits stored in memory locations - access to a logical object is ultimately translated into access operations at a machine-language level. At this level, there are three basic options to manage that access control:
1. modify the address received from the user process (address sandboxing)
2. construct the effective address from the relative addresses received from the user process (relative addressing)
3. check whether the address received is within given bounds, but otherwise do nothing else