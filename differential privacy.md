>[!quote] The goal of this technique is to address the limitations of data anonymisation techniques for publishing such as [[anonymisation#^0d4347|k-anonymity]]
>\- [[Privacy and online rights knowledge area]], p.13

>[!quote] the goal of a privacy-preserving statistical database is to enable the user to learn properties of the population as a whole while protecting the privacy of the individual contributors
>\- Dwork *et al.*, 2006

>[!quote] 'Differential privacy' describes a promise, made by a data holder, or curator, to a data subject: 'You will not be affected, adversely or otherwise, by allowing your data to be used in any study or analysis, no matter what other studies, data sets, or information sources, are available'
>
>\- Dwork and Roth, 2014

>[!quote] the guarantee of a differentially private algorithm is that its behaviour hardly changes when a single individual joins or leaves the dataset
>
>\- Harvard University Privacy Tools Project, 2024

## Technical definition
- Differential privacy should provide privacy by process
- here's an example from social sciences:
	- if you're asking participants about an embarrassing or illegal behaviour, have them:
		- flip a coin, and answer truthfully if it's heads
		- else, flip a second coin, and always respond 'yes' if it's heads of 'no' if it's tails
	- thus, an individual has plausible deniability of any outcome. But how do we do anything useful with this?
	- Let $S$ be the property "is a smoker", and $R$ the population of respondents
	- Suppose we end up with a dataset whereby 75% of participants say they have the property $S$. What's the real fraction, $s$? $$\begin{aligned} 
\frac{1}{4} \cdot (1-s) + \frac{3s}{4} &\Rightarrow \frac{1-s}{4} + \frac{3s}{4} \\ &\Rightarrow \frac{1+2s}{4} \\ &\Rightarrow \frac{1}{4} + \frac{s}{2} \\ 
\end{aligned}$$
	- that's a little  spicy, so let's take a closer look. The likelihood of a 'Yes' answer is 1/4 regardless; therefore, the expected number of 'Yes' answers is $\frac{1}{4}$ times the number of participants who do *not* have the property $S$ plus $\frac{3}{4}$ of those who *do* have the property $S$.
	- That is, of the people who claimed not be a smoker, we can confidently say that 1 in 4 were saying that because the coin told them to say it.
	- Likewise, of those who said they *were* smokers, 1 in 4 were actually smooth-lunged liars: but 3 in 4 really are hacking their lungs up every morning
	- we can then apply this formula equal to the supposed probability of $s$, ie $P(S) = \frac{1}{4} + \frac{s}{2}$ and then rearrange to get $P(s)$.
	- In our case: $0.75 = \frac{1}{4} + \frac{s}{2}$ , which rearranges to $1.5 = \frac{1}{2} + s$, and thus $s = 1.5 - 0.5 = 1.0$ or, to put it another way, every respondent answered 'yes'

