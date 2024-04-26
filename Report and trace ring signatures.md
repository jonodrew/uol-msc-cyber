- builds on [[Traceback for end-to-end encrypted messaging]]
- group signatures and ring signatures provide [[anonymity]] within a set of users
- group managers issue keys, and are therefore able to break anonymity
- by contrast ring signatures are non-hierarchical. users select a ring of users within which they are anonymous; however, a designated 'tracer' role can identify signers
## implementation
### goals
- a tracer must only be able to revoke anonymity if a report has been made