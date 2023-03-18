Web developers love a container, because it contains none of the mucky [[operating system]] questions. It turns out they're important. Who know.

## intro
Containerisation allows a single OS to keep its applications and their dependencies isolated. This enhances process isolation (one aim of a perfect container-driven architecture is one container, one process) and makes software more modular (though infinitely more complicated, cf [[Kubernetes]])

## concerns
Container escaping has become a popular hobby of [[attacker|attackers]] in recent years, and they do seem alarmingly easy to pop. Nonetheless, because of their ease-of-use, expect them to continue to feature heavily in the security landscape