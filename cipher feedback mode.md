---
aliases:
  - CFB mode
---
A [[mode of operation]] similar to [[output feedback mode|OFB mode]]. It converts a [[block cipher]] into a self-synchronising [[stream cipher]]. It does this by encrypting (again?) the previous [[ciphertext]] block and then [[exclusive or|XOR]]-ing it with the next [[plaintext]] block, which produces the next [[ciphertext]] block