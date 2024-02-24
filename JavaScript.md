---
aliases:
  - js
  - .js
  - javascript
---
## Declaration
I accept that I hate JavaScript. Please take that under advisement.

## introduction
[[HyperText Markup Language|HTML]] is a way to describe images and text. And then one day we thought, hey. Why don't we let users execute totally arbitrary scripts that they've downloaded from the [[Internet]]? What's the worst that could happen?


## The worst that could happen
_this_

A language that is, depending on your preference, event-driven, [[object oriented programming|object-oriented]], functional, or imperative. It is a complex and beautiful programming language, and that is great.

Its addition to [[World Wide Web|the Web]] has been a calamity for security because executing arbitrary scripts on a user's computer is literally the thing we spend all damn day trying to stop happening. 

Thankfully, browsers sandbox JavaScript. The API exposed to the script are limited, but still powerful. 

These scripts have access to the totality of the [[Document Object Model|DOM]], and can use that access to rewrite the content of the page dynamically, including adding new elements! Hurrah! They can also make their own requests to external servers (how Google Analytics works, but also a fantastic way to exfiltrate data). The script can also access elements of the browser, which enables it to alert users with pop-ups, among other things.

## Single-origin Policy
The browser also restricts certain actions. One restriction is the same-origin policy, or SOP. This policy states that a script running in a window can access the content of another window if, and only if, both windows share the same origin. 'origin' here means the protocol, hostname, and port must be the same.

>[!example]
>http://example.org/a/b has the same origin as http://example.org/c/d
>
>However, https://example.org and https://www.example.org do not - because www... is actually a subdomain





