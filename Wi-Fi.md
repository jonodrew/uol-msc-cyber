## What [[security service]] do we need?
[[confidentiality]]: Used to be provided by wired connections. However, anyone with a scanner can access wireless data. So we need data to be confidential when it's in transit

[[data integrity]]: much harder to do with a wired connection. Again, we need to provide a means of doing this wirelessly

[[data origin authentication]]: it's pretty important that we can be sure that data is coming from the client or the router, rather than an impersonator

[[entity authentication]]: is it important we know who's accessing the network? Yes, definitely, because clients on the network have more privileges than those who don't. We also want to make sure we're talking to the right [[router]]

### Doesn't need:
- [[non-repudiation]]: it's unlikely you'll end up in a dispute about who sent what data where, so we probably don't need non-repudiation from our wi-fi service. If this was needed, it would probably be at the application level