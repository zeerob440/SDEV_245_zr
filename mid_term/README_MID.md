# About secure_app.py

Entry to the program is 'secure_app.py'

secure_app.py is a modular program that applies SoC for authorization & authentication, hashing & encryption, and decryption.  

secure_app.py lightly simulates RBAC. This is simulated by inputting 'Admin'. Once authentication and authorization are complete, secure_app.py allows the 'Admin' to
enter a message to be hashed and encrypted in super_secret.py. Next the message is decrypted and hash is verified in decrypt.py. Finally, the decrypted message is returned to the user in secure_app.py

## Requirements

1. Python 3.13 or greater
2. pip install
    * cryptography

## How secure_app.py upholds the CIA Triad

1. secure_app.py upholds the CIA triad by:
    * Simulated RBAC (confidentiality)
        - The user needs to be an 'Admin' to access the hash an encryption functions.
    * Max login attempt limits (confidentially)
        - secure_app.py limits login attempts to three. If 3 attempts are made, the user is booted from the program.
    * SHA-256 encryption (integrity)
        - SHA-256 hashing is applied to the message
    * Symmetrical Encryption (integrity)
        - Fernet uses AES encryption on the message.
    * Modular Design (availability)
        - secure_app.py is a local CLI app, so traditional availability does not apply well here. However my using modular design, if a bug were to occur, it could potentially
        be quickly identified and debugged because of the SoC designed into the program.

## Entropy and Key Generation 

keys should always be generated from high-entropy true random occurrences. secure_app.py uses Fernet to generate a key. Fernet is a class from Python's cryptography library. Fernet provides the high-entropy source that super_secret.py uses to create the symmetrical key. This key is generated each time the program runs.


