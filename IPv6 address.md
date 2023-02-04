Version 6 of the [[Internet Protocol]] uses 16-byte (128-bit) addresses. 128 bits creates a space of $2^{128}$, a number not very much different to the number of molecules on the surface of the earth. It is a very large number. It will nonetheless probably not be very efficiently used.

They're written for humans as eight groups of four [[hexadecimal]] numbers, for example:

> 8000:0000:0000:0000:0123:4567:89AB:CDEF

Note above that there are three groups comprised solely of zeroes: these can be completely removed and replaced with a double colon, resulting in

> 8000::0123:4567:89AB:CDEF

Additionally, leading zeroes can be safely removed:

> 8000::123:4567:89AB:CDEF

Which makes the whole thing much easier to read

We can also express an [[IPv4 address]] wth this notation:

> ::192.168.1.0


