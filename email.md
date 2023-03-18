The basic concept of an email address is `username@domain`

As long as the domain is registered in the [[DNS]], we can send email to users on that domain. The domain record should be of type `MX` - see [[DNS#Resource records]]

## Routing
1. An email is composed in a mail user agent (MUA). This might be a native application like Thunderbird, or via a web interface, like ProtonMail. The user only needs to define the following fields: `to, cc, bcc, subject, body`
2. The MUA hands the message to the mail transport/transfer agent (MTA). A relay may follow, with the message being passed from MTA to MTA. 
3. Finally, it ends up at the mail delivery agent (MDA), which hosts mailboxes for users.
4. Finally, the recipient's MUA retrieves the mail from the MDA and displays it to the user

[[Simple Mail Transfer Protocol|SMTP]] is used to wrap messages and communicate from MUA to MTA, and from MTA to MTA. However, this is not the same as from the MDA to the MUA at the recipient end - this is done with something like [[Post Office Protocol|POP3]] or [[Internet Message Access Protocol|IMAP]].

## Security
- there are no security measures built into the email infrastructure 😳
- yaaaaay
- what [[security behaviour]] would we expect to see in email?
	- [[confidentiality]], both of the message content and the message header
	- [[data integrity]], or maybe even [[data origin authentication]]
	- reliability/[[availability]]
	- the ability to reject unwanted messages - spam, malicious, etc