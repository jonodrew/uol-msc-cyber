A means of structuring memory. Memory is divided into pages of equal size, and addresses comprise {page number}{offset}. 

The standard size makes memory management efficient - but makes protecting them more difficult, because a page may contain objects with different security requirements.

Worse still, even if the objects all have the same security requirements, we can use them as a covert channel for uncovering data: when the [[operating system]] runs out of page, a `PageFault` exception will be raised. This tells an [[attacker]] that the data is divided across two pages, and that they are consuming it in a way that is acceptable to the system.