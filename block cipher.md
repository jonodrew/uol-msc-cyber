an [[encryption algorithm]] and a kind of [[cryptographic primitive]] 

Block ciphers require messages to be in a block of a specific length. [[DES]] required blocks of 64-bits, while the more modern [[AES]] requires blocks of 128-bits. The algorithm then outputs blocks of the same length.

A small block size is not preferred. Although it's faster to encrypt, it reduces the number of potential [[plaintext]] blocks that can ever be encrypted. If the block size is _m_, there is a maximum of $2^m$ blocks that can be encrypted. If an [[attacker]] is able to discover the plaintext blocks corresponding to some previously sent 

For smaller messages, the blocks are padded. Larger messages can be broken into chunks of _n_ bits. This is called the [[ECB mode]] [[mode of operation]], but it's not to be recommended. Instead, other approaches are used to ensure that no metadata is leaked from the communication (see other [[mode of operation|modes of operation]]).

A block cipher is a repetition of rounds. A round is an algorithm for [[encryption]] that may be weak on its own, but when iterated becomes more complex. Much like knotting a string - simple mechanisms that are repeated and repeated until the whole thing is a tangled mess.

Each round is parameterized with a round key, and each round key should be different (otherwise every round is the same, defeating the point). Keys are generated according to a [[key schedule]]





