## reading
- [[Fundamentals of Fully Homomorphic Encryption - A Survey]]
## 5.1 Introduction to #privacy  technologies - [[fully homomorphic encryption|FHE]]
- valuable in contexts where we don't trust the [[data processor]]

## 5.2 What is [[fully homomorphic encryption]]?

## 5.3 [[fully homomorphic encryption|FHE]] schemes
- [[Ilaria Chilotti]]
- noise-based schemes are 'levelled', because they generate noise with every operation. Before long the noise is so great that the result can't be decrypted
- Gentry 2009 found a solution to this problem, called 'bootstrapping'

## 5.4 Applications of [[fully homomorphic encryption|FHE]]
- [[Microsoft]] Edge uses [[fully homomorphic encryption|FHE]] to check if your password has been breached!
- is this a microservice I could build out for work?
- Should we consider FHE as a protocol, rather than a [[cryptosystem]]? Specifically, should we consider it a [[Multi-Party Computation]] #protocol?
- For this we need to bring in [[zero-knowledge proof|ZKP]]
