Fuzzing is an automated software testing technique, which works by trying to break the software with:
- random input
- too much input
- too little input
- etc
In short, it's a brute-force approach to testing, similar to that used in [[QA testing]]

Fuzzing can be [[black box]], [[white box]], and [[grey box]]. These are the same classifications as in [[CYM050 week 10#Lesson 1 penetration testing|pen testing]]

Remember that 'input' is a generic term for 'interface with the world'. So we might fuzz:
- an endpoint that accepts a file
- a command line tool that accepts user input
- a form
- a car
	- alright fine specifically the on-board computer of a car, or the [[Vehicular entry systems|blipper thing]]

>[!quote]Remember that people are vulnerable to fuzzing too: it's called a [Gish Gallop](https://en.wikipedia.org/wiki/Gish_gallop)
>
>\- Me, obviously

## suppliers
- American fuzzy lop (AFL)
- LibFuzzer
- Peach fuzzer
- BOOFUZZ ([[network control protocol]] fuzzing)


