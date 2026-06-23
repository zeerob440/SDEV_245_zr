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


caesar_input: str = input('Enter a message to be encoded: ')

PLAIN_TEXT_RUNES: list = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    
CAESAR_RUNES: list = [' ', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']


while True:
    if caesar_input.isdigit():
        print("Spell numbers out.")
        continue
    else:
        caesar_list = list(caesar_input.upper())
        break

encrypted_list: list = []

for rune in caesar_list:
 cipher_rune = PLAIN_TEXT_RUNES.index(rune)
 encrypted_list.append(CAESAR_RUNES[cipher_rune])

print(encrypted_list)
print(PLAIN_TEXT_RUNES)

    









