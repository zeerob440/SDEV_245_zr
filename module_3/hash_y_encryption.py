import hashlib
import rsa

'''
SPECS
X Choose a language (Python, Java, C/C++, or any language of your choice).

Write an app that generates SHA-256 hashes for input strings or files

Write an app that uses a simple substitution cipher (Caesar cipher or similar) to encrypt/decrypt input text

X Use OpenSSL or a tool to simulate a digital signature (sign/verify).
X Include a short README explaining your code's functionality
'''
input_string1: str ='''
UNSC PRIORITY TRANSMISSION\n
FROM: SIERRA 117\n
TO: ADM HOOD\n

To give the Covenant back their bomb.\n'''

input_string1_bytes = input_string1.encode()
#print(input_string1_bytes)
hash_obj = hashlib.sha256(input_string1_bytes)

hashed_input = hash_obj.digest()

print(hashed_input)






