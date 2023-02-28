The Open Web Application Security Project (OWASP) [publishes a top ten list of vulnerabilities](https://owasp.org/Top10/). It doesn't change much year to year, and in 2021 it comprised:

1. [[injection]]. An attacker’s hostile data can trick an interpreter into executing unintended commands or accessing data without proper authorisation.  
2. [[broken authentication]]. Application functions related to authentication and session management are often implemented incorrectly.  
3. Sensitive data exposure. Sensitive data may be compromised without extra protection, such as encryption at rest or in transit and requires special precautions when exchanged with the browser.  
4. [[XML external entities]] (XXE). Many older or poorly configured XML processors evaluate external entity references within XML documents.  
5. Broken [[access control]]. Restrictions on what authenticated users are allowed to do are often not properly enforced.  
6. Security misconfiguration. This is commonly a result of insecure default configurations, incomplete or ad hoc configurations, open cloud storage, misconfigured HTTP headers and verbose error messages containing sensitive information.  
7. [[cross-site scripting]], or XSS. XSS allows attackers to execute scripts in the victim’s browser which can hijack user sessions, deface web sites, or redirect the user to malicious sites.  
8. Insecure deserialisation. Insecure deserialisation often leads to remote code execution.  
9. Using components with known vulnerabilities. If a vulnerable component is exploited, such an attack can facilitate serious data loss or server takeover.
10. Insufficient logging and monitoring. Insufficient logging and monitoring, coupled with missing or ineffective integration with incident response, allows attackers to further attack systems, maintain persistence, pivot to more systems and tamper, extract or destroy data.