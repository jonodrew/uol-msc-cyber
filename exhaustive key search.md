This is it: the MacDaddy of breaking a [[cryptosystem]]. Effective against everything except a [[one-time pad]]. Let's see how we do it.
## Algorithm
1. Select a potential [[decryption key]] from the [[keyspace]].
2. Decrypt the [[ciphertext]] with the candidate key.
3. Check if the resulting [[plaintext]] makes sense
	1. If it does, mark this decryption key as a "candidate decryption key"
	2. If it doesn't, discard the key and return to (1)
## Identifying candidate
Attackers will use other information to support their key search. Multiple [[plaintext]]/[[ciphertext]] pairs will allow them to more quickly check their candidate keys. A good knowledge of the [[plaintext]] language also helps (one of the reasons that Japan's codes were more resistant during World War 2, and why the US army used [[Navajo code talker]]s). Finally, contextual information helps - for example, knowing that the plaintext will be a date, or one of a list of names.