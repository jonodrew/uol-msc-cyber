---
aliases:
  - Portable Document Format
---
## What's a PDF?
A PDF comprises three distinct ways of organising information:
1. A directed graph, where the nodes are objects and the edges are how the objects reference each other. This forms the document content
2. A header, trailer, and cross-reference table. These are used to help other programs read the PDF and form the file structure
3. The page content, which describes how graphics, text, etc should be organised on the page

### Document content
- there are a few distinct types for these objects
- boolean values `true` and `false`
- the null object (`null`)
- `Names` are their own type of object, and are identified by a preceding `/`. they are case sensitive and cannot contain whitespace or delimiters
- integers
- real numbers (not including exponentials)
- strings, which are represented in parentheses `(Hello world!)`
- References, which go `X 0 R` where `X` is the referenced object
- arrays, which do not need to be heterogenous and are introduced by brackets `[1, 2, /Bob]`
- dictionaries, which are signified by `<< >>` and which map `Name` objects to any other objects (ie, all dictionaries have the type `[Name, Any]`)
- You can also have a dictionary + some binary data, which are known as streams. Streams are used to store streams of graphics operators, images, fonts, things of this nature
### File structure
- the header is what marks the file as a PDF document
- the trailer has the byte offset of the cross-reference table and an end-of-file (EOF) marker
- the cross-reference table has the byte offset for each object in the document, which means you can jump to any object arbitrarily
### Page content
- a set of commands that describe what to do with objects
- for example:
```Postscript
BT (begin a block of text)

/F13 12 Tf (Choose Font F13 and set size to 12)

(ABC) Tj (Draw the String ABC)

ET (End the text block)
```
### Document structure
- We're not finished yet, though
- We also need:
	- a trailer dictionary, which will explain to the caller how to read the other objects
	- the document catalog, which is the root element in the graph (see [[#Document content]])
	- the page tree, which tells the caller how many pages are in the document
	- at least one page object, which itself must contain
		- resources, eg fonts
		- [[#Page content]]
## [[JavaScript]]
- you can put javascript in a PDF
- it's generally a sign that the PDF is malicious though, because the fact that it's possible does not mean that it's good
