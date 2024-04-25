Achieving full anonymisation is difficult. Data often includes patterns that allow for identification of a person, so we have to consider the uniqueness of a person's data. Removing the name from an address might not work if the address is 10 Downing Street, for example.

## _$k$_-[[anonymity]]

^0d4347

An approach that advocates combining [[obfuscation#^90f992|generalisation]] and [[obfuscation#^47d6dd|suppression]]. The aim here is to ensure that records are anonymous among at least _$k$_ other records. For example, 2-anonymity would mean that each record is indistinguishable from (according to a specific axis) at least one other.

However, there are critiques of this. _$k$_-anonymity along one axis doesn't really solve the problem: information still leaks along other axes, and generalising that data may render the whole dataset useless.

### _$l$_-diversity
This is an additional approach to _$k$_-anonymity (above), such that for each _$k$_ anonymous individuals, there are at least _$l$_ possible values for any sensitive attributes. This approach can also be broken, and some researchers further call for _$t$_-closeness, where the set of sensitive attributes is not only diverse but also follows the general distribution of those attributes in the general population.
