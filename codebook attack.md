An attack on a [[block cipher]], where you generate every possible [[plaintext]] and consequently every possible [[ciphertext]]. With a cipher that uses $2^4$ (i.e 16)-[[bit]] blocks, there are $2^{16}$ ciphertexts for each block. That's only 65,536 - for which you'd need: $2^{16} \times 16 \equiv 2^{16} \times 2^4 = 2^{20}$ bits of memory, or a measly 128kB

Bumping it up to just 32-bit ($2^5$) blocks results in the following calculation: $2^{32} \times 2^5 = 2^{37}$, which is a more substantive 16GB

At 64 bits the memory you need to store the possible ciphertexts is $2^{70}$ bits, which is a fun new thing called a zetabyte, and at that point you'd give up 