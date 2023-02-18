## Learning objectives
- evaluate and discuss the foundations of [[authorisation]] and [[access control]]
- explain how access control is implemented in modern Linux operating systems
- critique information flow models

## Reading

## Lesson 1:

## Lesson 2: [[access control]]
### Access control list (ACL) vs access control matrix (ACM) vs capabilities

- ACM would mostly be empty cells, thus inefficient (to traverse and maintain). It would also be a single point of failure for access control (if the file gets corrupted, it’s pretty much over for the whole OS). By moving the access control to a per object basis, we limit the computation to a per object basis (i.e., ‘only check it when you need to check it’).
- Capabilities are better suited for queries related to per-person (principal) basis. This is better suited in, for example, database environments, in which the amount of data to query likely relate to an individual.

## Lesson 3: information flows
- The re-appearance of the dashed annoying 'high side' and 'low side'. 
- Let's also talk about [[Bell-LaPadula model]] and the [[Biba model]].
- And how impractical they are:
	- Static security levels. The models do not account for changes in security levels. This means that, in principle, a person can gain more or less access at some point and the model would not be able to accommodate for this change.
	- Not compatible with each other. BLP is a confidentiality model that is directly incompatible with the Biba model (they are inverts of each other).
	- It is difficult to enforce as it assumes honest and rational actors – e.g. wouldn’t deal with insider threat or collusion or accidents.