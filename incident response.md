There are generally three phases to incident response: containment, eradication, and recovery

## Containment
>[!quote] \[containment] provides a reasonable security solution until such time that sufficient information has been collected to address the [[vulnerability|vulnerabilities]] and the damage
>
>\- [[ISO 27035-3|ISO/IEC 27035-3]], Clause 11.2.1

Containment is not a long-term solution, but it will at least contain the threat. It is also likely to have significant impacts on the rest of the organisation. Removing a resource's access to the [[Internet]] will prevent command and control from an [[attacker]], but will also prevent legitimate users from accessing that resource.

## Eradication
The total remove of the problem. Malware is entirely removed from devices and systems, via a total wipe or the judicious application of a shredder. Compromised tokens are rotated, and any assets that might have been compromised with those tokens are examined and contained or eradicated. Again, this may cause problems with the wider organisation. For example, if the [[remote authentication dial-in user service|RADIUS]] server needs to be wiped and new certificates generated, the entire organisation may be temporarily unable to operate

## Recovery
Recovery will be phased, and remediation will depend on the priority of different systems 

