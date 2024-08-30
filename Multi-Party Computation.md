---
aliases:
  - MPC
---
## Introduction
In [[cryptography]] we talk a lot about Alice (honest), Bob (honest), and Eve (wicked).

Multi-party computation raises an interesting question: what if you can't trust ~any~ some of them?

See https://www.zama.ai/post/fhe-as-a-puzzle-piece%20 for an interesting read there

## Techniques
### Shamir Secret Sharing
- why does all this stuff sound like wizard nonsense
- a generalised secret sharing scheme solves the problem of a 'dealer' who wants to share a secret, $s$, amongst $n$ parties such that some subset $t + 1$ can reconstruct the secret together, but a subset of size $\leq t$ can learn nothing about it
- for this particular scheme, we use the fact that for any $t+1$ points on a two dimensional plane $(x_1, y_1),...,(x_{t+1}, y_{t+1})$ with unique values of $x$, there exists a unique polynomial function, $q(x)$, whose degree is at most $t$, and has output $q(x_i) = y_i$ for every $i$
- in addition, it should be possible to efficiently reconstruct the polynomial$q(x)$, or any specific point on it
- apparently there's a set of polynomials called Lagrange basis polynomials that are good for this, because reconstruction can be carried out by calculating $q(x) = \sum_{i=1}^{t+1}l_i(x) \cdot y_i$, remembering that $t+1$ is the smallest subset of people allowed to reconstruct the secret 
- we assume that all computations are in the finite field $\mathbb{Z}_p$ for a prime $p > n$ (remember $n$ is the number of people with whom you want to share the secret) 
- my understanding of this is: imagine a curve on a two-dimensional plane. It can be described with a polynomial formula. If you only have one, two, or anything up to $t$ points you can't figure out what the curve should look like. With $t+1$, you should be able to perfectly reconstruct that curve, and therefore its equation
- the secret is defined as $q(0)$