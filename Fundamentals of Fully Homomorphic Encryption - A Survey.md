That's [[fully homomorphic encryption]], lads.

## notes
- nggggh okay, let's do some maths
- in [[RSA]], the [[public key]] is the product of two primes $N = p \cdot q$  as well as some integer $e$
- the message space is the set of elements $\mathbb{Z}^*_N$
- encrypting a message $m$ to the public key means raising it to the power of $e$ and then taking the result modulo $N$, thus: $ciphertext = message^e \pmod N$
- it is not hard to see (listen, you _smug motherfucker_) that consequently the product of two ciphertexts, which one could express as:
$c_1 = {m_1}^e \pmod N$
$c_2 ={m_2}^e \pmod N$
and so $c_1 \cdot c_2$ evaluates to:
$${m_1}^e \pmod N \cdot {m_2}^e \pmod N
\\
\implies 
$$ which can be reduced to $({m_1} \cdot {m_2})^e \pmod N$, or to put it another way, the product of the two cleartext values.

However, it's rare that we simply need to multiply two 
