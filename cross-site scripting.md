---
alias: [XSS]
---
## Impact
- a script that runs on a user's computer can be incredibly powerful, if it can escape the [[browser]]
- even if it can't, it might still:
	- capture credit card information
	- capture passwords
	- hijack sessions
	- really do anything the user could do in the browser
- then there's the second order impacts - if you unknowingly host an XSS in your website, people will go off it
## Mitigation
- input validation
- output encoding - ensuring that scripts are treated as strings, rather than scripts
- [[content security policy]]
- secure frameworks and libraries (basically, most of the hard work has been done for you)
## Reflected
The malicious script is within the HTTP request. For example, an [[attacker]] might get you to click on a link that looks like this:

`http://example.com/search?query<script>alert('XSS')</script>`

If the server returns the query without sanitising it first, the script will run. This script just pops up a little alert box that says 'XSS', but you could do all sorts with it.
## Persistent
The script is stored on the server, and therefore presented as part of the usual [[HyperText Transfer Protocol|HTTP]] response. The [[attacker]] may have been able to get the script into the server through a message or comment form
## [[DOM]]-based
The script exists in the client side, rather than the server-side code