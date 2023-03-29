```mermaid
sequenceDiagram

Attacker/Fake Site ->> Victim: Your files have been lost. Please login using this link (https://fake-app/login) and re-upload your files
Victim ->> Attacker/Fake Site: Valid credentials (may be harvested for later)
Attacker/Fake Site ->> Real Site: Attacker credentials
Real Site ->> Attacker/Fake Site: Redirect to Attacker dashboard
Attacker/Fake Site ->> Victim: Pass through redirect
Victim ->> Real Site: Upload files
```
