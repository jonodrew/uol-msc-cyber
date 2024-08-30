Helios is an open-source [[eVoting]] scheme designed for low-[[coercion]] environments that uses [[homomorphic encryption]] and a kind of [[zero-knowledge proof]].

To vote, the user [[encryption|encrypts]] their choice and proves they did so correctly. The [[ciphertext]] and the proof together compose the ballot. The scheme administrator collects the ballots, discards incorrect ballots, combines them, decrypts the outcome and announces it.

The codebase has been open-sourced: https://github.com/benadida/helios-server but it needs some love. Could this be a [[MSc project ideas]]

Could this work with ranked voting?

## Detail
1. The administrator constructs a [[asymmetric|public-private key pair]] and publishes both the [[public key]] and the proof that they've constructed the keypair correctly.
2. Each voter encrypts their choice with the administrator's public key, prove they'd constructed the [[ciphertext]] correctly, and then cast these together as their ballot
3. The administrator collects the ballots, discards ballots whose proofs are incorrect and combines the ciphertexts in the remaining ballots. They derive the encrypted outcome, decrypt it, and publish the answer alongside proof of correct decryption.
As we can see, this approach is not resistant to [[coercion]]. It also assumes that the registration phase is trustworthy (a really challenging assumption). Additionally, the overhead for tallying increases quadratically with the number of votes; that is, the time required to do the tallying is $(tn)^4$, where $t$ is the time taken to tally a vote and $n$ is the number of votes