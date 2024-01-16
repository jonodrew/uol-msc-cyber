Computer viruses are generally classified according to their target. Thus:

## File infectors
These come in direct and memory-resident flavours. 
### direct

^0b03db

These immediately infect files, actively searching for them. They come with three approaches:
- overwrite: when the virus simply overwrites the code in the host file
- companion: where the virus renames itself with a suffix that puts it higher in the execution order than the host file. Thus if `hello` is executed, the virus is run before the host file. The virus will also pass control back to the original host file once its finished executing
- parasitic: where the virus 'attaches itself' (how?) to the host file, either at the end or at the beginning
### memory-resident
These use the same approaches as [[#^0b03db|direct]] above. Rather than immediate infection, they remain in memory using the 'Terminate but stay resident' (TSR) system call in DOS.
## Boot-sector viruses
This is a nasty little thing that infects the boot sector - the part that runs even before the [[operating system]] starts up. There are some figures here for master boot record size (512 bytes) that might need checking
## Multipartite viruses
They can do both: [[#Boot-sector viruses]] and [[#File infectors]]