Computer viruses are generally classified according to their target. Thus:

## File infectors
These come in direct and memory-resident flavours. 
### direct

^0b03db

These immediately infect files, actively searching for them. They come with three approaches:
- overwrite: when the virus simply overwrites the code in the host file. This might be through brute-force overwriting (which may stop the host software working properly), pre-pending, a-pending, or internal cavity infection
	- internal cavity infection is fascinating, because it takes advantage of empty space within the existing software. So: how do you end up with empty space in software?
- companion: where the virus renames itself with a suffix that puts it higher in the execution order than the host file. Thus if `hello` is executed, the virus is run before the host file. The virus will also pass control back to the original host file once its finished executing
- parasitic: where the virus 'attaches itself' (how?) to the host file, either at the end or at the beginning
### memory-resident
These use the same approaches as [[#^0b03db|direct]] above. Rather than immediate infection, they remain in memory using the 'Terminate but stay resident' (TSR) system call in DOS.

They might also loiter, in [[Windows]] systems, in the registry - where they insert keys to ensure they're revived every time the system boots

Alternatively, the startup folder is a fun place - because everything in there is run once the user logs in. This is where the "Iloveyou" [[worm]] situated itself.

Scheduled tasks are a useful way for [[malware]] to, well, schedule tasks. This can aid in avoiding detection if the tasks are scheduled when nobody is likely to be looking at the machine

Finally, malware can masquerade as a service. 

## Boot-sector viruses
This is a nasty little thing that infects the boot sector - the part that runs even before the [[operating system]] starts up. There are some figures here for master boot record size (512 bytes) that might need checking
## Multipartite viruses
They can do both: [[#Boot-sector viruses]] and [[#File infectors]]