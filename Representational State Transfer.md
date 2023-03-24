---
alias: [REST]
---
## Principles
- Separation of concerns, particularly between user interface and data
- Stateless interaction
- The cachability of responses (with an appropriate time to live)
- a layered architecture that allows for scaling
- annotation of resources
	- specifically, this means things like hypermedia: responses contain information that allows a user to go deeper or explore further
	- let's consider an example
```
GET /shelf ->
{
  books: [
    {
      "title": "The winter's tale",
      "loc": "shelf/book/1",
      "author": "William Shakespeare"
    }
  ]
}
```
In this example, the endpoint returns the 'author' key as a string, but doesn't indicate whether it's stored as a string or as an object in the database. This may prove to be a problem when I try to add a book to the shelf:
```
POST /shelf/book {"title": "Romeo and Juliet", "author": "William Shakespeare"}
```
Might return either:
```
{
  201 Created
}
```
indicating that the resource has successfully been added, or
```
{
  400 Bad request
}
```
indicating that we needed to have already added William Shakespeare as an 'author' resource.

## Security
Suppose we want to limit the users who can put books onto the shelf. This is where the `Authorisation Header` comes in. A username and password are concatenated with a colon (`username:password`) and then encoded in `base64`. Your reminder that encoding ≠ [[encryption]].

If a request is made with an invalid username, or an invalid password, or both, how should the server respond? Consider that a `401 Unauthorised` and a `403 Forbidden` response both leak information about the system. The best response from a security perspective is probably simply `404 Not found`, which only tells the [[attacker]] that these credentials do not grant access. However, it is a significantly less usable response. [[security vs usability]] strikes again.

Another great mechanism is [[OAuth 2.0]].