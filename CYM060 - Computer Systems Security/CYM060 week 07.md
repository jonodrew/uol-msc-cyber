## Learning objectives
- Propose countermeasures against common web attacks
- Identify and demonstrate common mistakes in web applications
- Determine problems of passing data across different contexts
- Define key concepts of the web infrastructure

This is my jam baby!

## Lesson 1: software threats
- [[OWASP Top Ten]] gets a mention

### Critical thinking exercise:

#### Purpose
Identify reasons why attacks happen and identify more general, non-technical approaches to combat them – despite vulnerabilities being present.

#### Task
Attacks happen when means, motives and opportunities meet for a malicious actor. Propose and justify what developers and vendors can do to means, motives and opportunities to reduce the likelihood of being attacked, despite vulnerabilities being present in their systems and software they have developed.

#### Answer
- To reduce the means, we can try our best to write secure software. Even if we can't guarantee its security, we can try to make it as good as possible. That means using automated testing suites, fuzzing, and human testers to try out different inputs.
- To reduce the motives, we should keep a low profile, and not say stupid things like "[our software is unhackable](https://www.investopedia.com/news/unhackable-crypto-wallet-was-hacked/)". We should also publicly state that we don't have insurance; that we don't pay ransoms; and that we don't store any useful data. 
	- We should also try our best to make sure those things are true.
- To reduce the opportunity, we should reduce our attack surface as much as we can. Specifically in the realm of software vulnerabilities, that means making sure our external APIs are clean and well-designed; that any external libraries we use are patched; and we should ensure our development team is well-paid, comfortable, taken care of, and encouraged to deliver software in a secure way.
	- full disclosure: I am a developer


## Lesson 2: common [[threat|threats]]

And immediately into the worst code I've ever seen
```C
bool checkPWStatus(void){
	char password[12];
	gets(password);
	return 0 == strcmp(password,"ishallpass");
}

int main(void){
	bool pwStatus;
	puts("Please Enter Password: ");
	pwStatus = checkPWStatus();
	if (pwStatus == false){
		puts("Access Denied");
		exit(-1);
	}
	else{
		puts("Access Granted");
		exit(0);
	}
}
```

Let's all promise to never write code like this please
## Lesson 3: mitigiation and system hardening