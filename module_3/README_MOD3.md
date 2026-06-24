# hash_y_encryption.py
hash_y_encryption.py demonstrates three mini programs, each demonstration is separated by function AKC().
AKC() pauses the program and awaits user input to continue the program. It is intended to make grading the assignment easier since each demo is on hash_y_encryption.py.

## HASH DEMO

The hash demo uses the hashlib library to hash an input from the user. The process is user input> encoded to bytes > create hash object > convert has to binary > output the hashed value to user. 

## Create Simple Caesar Cipher

This program converts message 'My dogs are named Mia and Rico, into cipher text, and prints the cipher text. Next it decrypts the cipher text and prints the decrypted original message. It works kind of like an intangible decoder ring. 

1. It stores the character sets the cipher and plain text use in two lists. 
    * CAESAR_RUNES contains cipher text order
    * PLAIN_TEXT_RUNES contains the plain text order

element zero (I love saying that I'm a huge Mass Effect fan) were both set to ' ' because they need to match  indices between the lists to decrypt the message, but CAESAR_RUNES 'runes' were offset by -3. 

2. Next it takes the message to be encrypted, makes all 'runes' upper case then breaks it into a list so it can be iterated through.

3. encrypted_list is declared, it is intended to store the encrypted message as a list. 

4. next caesar_list is iterated through, by element. INT: cipher_rune stores the index, INT: cipher_rune is then used to index the CAESAR_RUNES, pull the 'rune' stored in the index and append encrypted_list with it. I used 'rune' for the elements because cha() is a function in Python. 

5. encrypted_list is converted to a string with .join() and the string is printed to the grader.

7. The the message is decrypted using a similar process as encryption and the decrypted message is printed.

## Signature Validation

This demo asymmetrically encrypts MASTERCHEIF_MSG signs and validates using the rsa library. Next it prints the signature hash to the grader A message transmission is simulated. Next the signature is verified, and prints the encryption method 'SHA-256'. The message is decrypted and printed to the user. 


