---
authors:
- M. Speciner
- R. Perlman
- C. Kaufman
---
## 15: [[public key infrastructure|PKI]]
This chapter recounts some of the models I've written about in [[public-key certificate]], but adds an interesting new idea: a bottom-up PKI model

### Bottom-up with name constraints
- Assume a hierarchical namespace in which each node is represented by a [[certificate authority|CA]]. Each parent verifies their child nodes with a [[digital signature]], but also each child verifies the parent node. Additionally, cross-links are allowed: a node can certify another node. Because it's hierarchical, it's not anarchic, but it does seem to combine the best of both the standard hierarchical CA model with the best of the [[PGP]] style, anarchic bi-directional verification.