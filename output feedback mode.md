---
aliases:
  - OFB mode
---
A [[mode of operation]] that converts a [[block cipher]] into a synchronous [[stream cipher]]. Unlike [[Counter mode]], we use a [[keystream generator]]. These blocks are then [[exclusive or|XOR]]'d with the [[plaintext]] blocks to generate the [[ciphertext]]