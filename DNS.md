---
alias: [Domain Name System]
---
The so-called address book of the [[Internet]]. 

DNS is a means of translating human-readable URLs to computer-readable [[Internet Protocol]] addresses. 

DNS servers are distributed across the world. It is, bluntly, a genuinely distributed database. The database is divided into zones, which typically correspond to a single domain: for example, example.co.uk, and contains all of its subdomains - eg api.example.co.uk, www.example.co.uk, etc

A DNS response will contain one or more Resource Records (RR). These records can contain a huge amount of information and are therefore annotated with a type. [[IPv4 address]] records are A types, while [[IPv6 address]] records are AAAA or quad-A. Naturally, in order to use the DNS service the client must know the IP address of a DNS server. For home users, the ISP will supply the address, and the user will use the [[Dynamic Host Configuration Protocol|DHCP]] to set it. In enterprise settings, sysadmins will generally configure clients to use the organisation's own DNS server (why?)

The nodes that comprise the DNS are known as name servers. Each domain has at least one authoritative name server (but should have more! and it should be an odd number!), which publishes the information about the domain and the name servers of any domain subordinate to it.

The information about top level domains (TLDs) is provided by the root servers.

Both the DNS server and client use caching to improve the speed of DNS resolution. That means that each RR needs a TTL, to indicate how long the record is valid for.

## Format
Queries and replies have the same format: a header field, followed by four sections. The header comprises six values, each 16 bits (2 bytes) long. The first is Q-ID: the query ID, which allows a client to match the DNS replies to a query

## Resource records
Resource records are a 5-tuple containing the following fields:

>[!note] The Resource record 5-tuple: 
>(Name, Value, Type, Class, TTL)

The name and value are obviously the url and the value you're expecting. The type indicates how the value should be interpreted - for example, as noted above, `A` indicates an [[IPv4 address]] while `AAAA` indicates an [[IPv6 address]]. Other types include:
- `NS` - the Value is the domain name for a host that is running a name server that knows how to resolves names within the specified domain
- `CNAME` - the Value field gives the canonical (hence C-name) name for a particular host and is used to define aliases
- `MX` - the host is non-binary (no, not really - the Value field gfives the domain name for a host that is running a mail server that accepts messages for the specified domain)
We can generally ignore `Class`, and should look to `TTL` to make sure that the resource record is not kept for too long

## Attacks
Let's think like an [[attacker]].

### DNS cache poisoning
Bad data with a long TTL is send to a caching resolver by a fake, authoritative name server. The cache now holds false information and, worse still, if it's a DNS server itself it may also disseminate this false information. 

### Intercept and mislead
An attacker sniffs DNS packets, intercepts those intended for the target, and sends on bad information

### QID guessing
If an attacker can guess the Q-ID of a DNS query, it they can provide a false answer - assuming they know or can guess what the request is likely to be

### Privacy threats
There is no [[confidentiality]] protection for queries or responses. This can be mitigated by, for example, DNS over [[HTTPS]] or DNS over [[Transport Layer Security|TLS]]. 

### Typos
This isn't exactly a DNS problem - but attackers often squat on domains that are visually similar to official domains (rhul.ac.uk (`rhul`) vs rhuI.ac.uk (`rhuI`)). They might also squat on domains that might be common typos - `go.vuk` for example

## Securing the DNS
[[DNSSEC]] is one new technology to secure the Domain Name System

Another approach, specific to MX-type records, is the Sender Policy Framework or SPF. SPF is designed to detect forged sender addresses and emails. 