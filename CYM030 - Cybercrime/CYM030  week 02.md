## Learning Objectives

- Describe how deception and social engineering manifest and how they can be defended against
- Differentiate between the various actors involved in cybercrime and their associated perspectives
- Evaluate the underlying psychological principles which make social engineering the most successful attack vector in cybercrime
- Explain the key role of human aspects in cybercrime

## Reading
- [[Cybercrime and you - how criminals attack and the human factors that they seek to exploit]]
- [[The online disinhibition effect]]
- [[Adversarial behaviours knowledge area]]
- Hadnagy, C. and P. Wilson _[[Social engineering - The art of human hacking]]._ (Hoboken: John Wiley & Sons Incorporated). [Chapter 8: Case Studies: Dissecting the social engineer](https://go.oreilly.com/university-of-london-worldwide/https://learning.oreilly.com/library/view/social-engineering-the/9780470639535/9780470639535_case_studies_colon_dissecting_the_social.html).


## Lesson 1: The importance of human aspects in [[cyber crime|cybercrime]]
- every actor in our system is human, for better and for worse
- their rationality is bounded
- personality too has a bearing
	- remember [[OCEAN]]
	- oh lord, 'the dark triad': narcissism, psychopathy, and Machiavellianism
		- in criminals, you'll often see extroversion and neuroticism also represented
- as does the cultural dimension
	- six are proposed: power distance; uncertanity avoidance; individualism/collectivism; masculinity/feminity; long-term/short-term; indulgence/restraint
	- another model has eight and could be more suited to organisations:
		- communication: high-low
		- critique: direct-indirect
		- leadership: egalitarian-hierarchical
		- decision-making: top-down - consensus-driven
		- trust: task-based - relationship-based
		- tolerance for disagreement: high-low
		- scheduling: linear-flexible (??)
		- mean of persuasion: inductive (context-specific) - deductive (from principles)
- security culture as a human angle: how do the following impact and interact with security culture, which is an emergent property of the system of people in it?
	- attitudes
	- behaviours
	- cognition
	- communication
	- compliance
	- norms/values
-  prospect theory: people are risk-averse to gains unless the gains are significant, but risk-seeking when it comes to _avoiding_ losses
- so phishing emails suggesting people will lose access/money/livelihood etc are more effective, and equivalent effect for gain means the phisher needs to make outlandish claims of the prize on offer
- optimism bias: we generally think things will turn out okay
- affect heuristic: if you're feeling good, your perception of risk is lower - but equally if you're feeling bad, everything seems out to get you
- availability heuristic: what you remember is given more weight than data
	- even an imagined outcome is considered more likely than one that has not been imagined
- people will remember vivid stories than pallid ones, and therefore (see above) will be more persuaded after the fact
- representative heuristic: people give more weight to more detailed scenarios, even though they are by definition less likely (feminist bank tellers are less frequent than bank tellers)
- base rate fallacy: if a thing is very unlikely, even a good test for it will be wrong more often than it is not

## Lesson 2: Entities involved with [[cyber crime|cybercrime]]: [[attacker|attackers]], victims, and law enforcement
- Why do people commit crimes?
	- monetary gains
	- intellectual achievement
	- peer recognition, self-esteem
	- with regards to nation-state threats: ideology and duty

## Lesson 3: [[social engineering]]
- [[Kevin Mitnick]]'s cycle:
	- Research, for example by [[open-source intelligence|OSINT]]
	- Develop a rapport and trust - this can be over a longer period
	- Exploring information - gently teasing out topics of interest in a way that does not arouse suspicion
	- Utilising information
- Using logos, pathos, and ethos to form convincing arguments
	- it should be noted that this is simply a good introduction into persuading people *generally*, and that there is nothing nefarious about it
- However, the addition of deception makes things more nefarious
	- nefariouser and nefariouser
	- Mirroring of verbal and non-verbal signals can aid in deception and rapport building
- Note that we tend to mentally operate 'moat' thinking - that is we trust the context, rather than verifying each individual. This is the sort of thing that results in:
	- 'pillow talk' - intimacy in one sphere does not mean intimacy in all spheres
	- loose lips sinking ships - informal work chat in public spaces can be overheard by non-friendlies
	- lack of challenge - just because someone gained access to the building, doesn't mean they're allowed to be here
- deception can increase cognitive load, because it's stressful - but [not all stress is deception based](https://www.youtube.com/watch?v=ZSC4tV3a1z8)
- Ah, we're doing Milgram
- Two-thirds of drivers in the US (citation?) think they are better than average
	- hang on a second
	- I mean these numbers work, as long as you're using a median and there's a couple of really terrible drivers
	- like, driver Georg, who crashed three times on the way to the survey, is an outlier and shouldn't have been counted
- if you get people do something for free, even if it's meaningless *and they know it's meaningless*, they'll assign greater meaning to it than if they got paid
	- what the fuck
	- is this the basis for the charity sector?
	- I don't agree with the assessment - "Admitting a lack of meaning in the task would imply that they wasted their time without getting paid". 
	- Instead, maybe it's closer to [this study that found that people were more comfortable being late for pickup if there was a monetary amount assigned](https://www.parenta.com/2014/07/23/study-into-imposing-late-fines-on-parents-yields-surprising-results/)
	- that is - the moment we put a monetary value on something and it stops being an exchange of favours, or an interpersonal relation, our relationship to the task changes
	- **[Marx intensifies](https://en.wikipedia.org/wiki/Marx%27s_theory_of_alienation)**
- With that being said, there is a valid interpretation of the above that leans on a human tendency to be more confident in a decision *having made that decision*
	- for example, we are more confident that our horse will win the race after we have placed the bet, even though no condition has changed
- in uncertain situations, many people will look for context, and may be willing to accept it from people they wouldn't normally look to.
- they may also be more susceptible to being deceived, because of stress and the lowering of inhibitions that causes
- reciprocation can often be greater than the first gift; that is, if you can engineer a situation where you offer a low-value gift *and* the only thing the receiver can gift back is high value, they are likely to do that
- be very, very cautious about universal non-verbal signals
- that image \[at 9.12] is a poor copy of fig. 23, p.70, *What Every Body is Saying*, auth. Joe Navarro
- the next figure also
- Okay so this whole section is just a re-presentation of the book, huh
	- even the phrase *gravity-defying behaviours* is from the book
	- and *turtle effects*
	- and pacifiers
- Are we good at detecting lies?
	- no
- Lying is hard, though it can be learned
- It's not lying if you believe in it hard enough, which is why one ought never trust actors
	- remember! All actors are threat actors