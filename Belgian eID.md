## Background
ID cards have a weird history, and more so in the UK, where cultural attitudes are firmly against. However, the 1999 EU directive "European Directive on Electronic Signatures", which created a legal framework for electronic signatures to become legally binding, was the impetus for Belgium to begin work on establishing an electronic ID card.

## Purpose
The eID card has four core functions:

### Visual identification
The card continues to serve as a human-readable identity card, with visual data including a photograph, nationality, names, signature, etc

### Digital data presentation
These data can also be presentally electronically/digitally, to a verifying party

### [[entity authentication]]
The card holder can use the eID card to prove their identity in real time to a verifying party. 

### [[digital signature]] creation
The card, or rather its onboard private key, can be used to sign electronic contracts and social security declarations, and are considered legally binding

## Requirements
- [[data origin authentication]] of the card data: there must be assurance that the data has not been changed since the card was issues. This implies
- [[data origin authentication]] service: the card will need to provide this service, to support an [[entity authentication]] protocol between the user and a verifying service
- [[non-repudiation]]

## Application of [[cryptography]]
### [[asymmetric|public-key cryptography]]
Public key cryptography is necessary, because there is no limit to the practical applications of this tool. It would be impractical to generate and store a new symmetric key for every single application. Thus, public-key crypto is the only sensible approach.

### [[digital signature]]
There is no need to actually encrypt data, and the [[#Requirements]] can be met simply with a signature service

### A well-known, trusted, and public digital signature scheme
The eID scheme uses [[RSA]] digital signatures with appendix

## Provision of core functions
