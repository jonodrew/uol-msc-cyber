- we define 'essentially' as $\epsilon$ 
- a small $\epsilon$ means #privacy is more preserved, but responses to queries are less accurate
- [[differential privacy]] is not an algorithm but a definition, and may describe many algorithms
- 'anonymisation' is an incomplete answer to the problem of data privacy - paper gives example of 'anonymised' Netflix dataset which, when cross-referenced with IMDb reviews, revealed the individuals. These are called linkage attacks
	- holy _shit_
- re-identification is a harm in and of itself, but in addition there are harms that may come as a consequence of being able to tie specific data back to an individual
- paper also notes *differencing attacks*. Consider that a person of interest, Ms B, is known to be in a specific database. We can take a broad query: "How many individuals in this database hold a high clearance?", and a specific query "How many people, not named 'Ms B', hold a high clearance?". And now we know if Ms B holds a high clearance
	- we could also just checked her LinkedIn, probably 🙄
- auditing queries is not much use either: if the auditor allows the first query in the above, then to refuse the second query "because it gives away information" *itself gives away information*
	- what a mindfuck
- summary statistics are...apparently also hackable
## Chapter 2: Basic terms
- we trust the curator, who might in other places be called the [[data controller]]. However, we might decide to trust the curator by removing them and turning them into a protocol.
	- cf [[Multi-Party Computation]]
- there is a non-interactive, or offline, model of privacy whereby the curator produces a sanitised, synthetic database or even just a collection of summary statistics. The original dataset is deleted. The curator is made redundant
	- in this job market? Brutal
- in an interactive, or online, model, analysts can query the data iteratively and adaptively
- a privacy mechanism is a function $F$ whose arguments are a database $D$, a universe (??) of data types $\chi$, random bits, and some optional queries
- these approaches result in less accurate responses
## Chapter 13: reflections
