import hashlib
import string
import rsa
'''

SPECS
X Choose a language (Python, Java, C/C++, or any language of your choice).

Write an app that generates SHA-256 hashes for input strings or files

Write an app that uses a simple substitution cipher (Caesar cipher or similar) to encrypt/decrypt input text

Use OpenSSL or a tool to simulate a digital signature (sign/verify).
X Include a short README explaining your code's functionality
'''
# return user input when cipher is complete
user_hash_input: str = 'Enter something to be hashed: '
# encode into bytes
input_string1_bytes = user_hash_input.encode()
#print(input_string1_bytes)
# create hash object
hash_obj = hashlib.sha256(input_string1_bytes)

hashed_input = hash_obj.digest()

print(hashed_input)


all_runes: str = string.ascii_letters
for rune in string.ascii_letters:
    print(rune)









