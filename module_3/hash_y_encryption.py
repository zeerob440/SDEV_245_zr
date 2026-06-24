import hashlib
import rsa

# function makes the three demos easier to read by asking for user input to advance between examples
def AKC():
   any_key_continue = input('Press any key to move to next demo.\n')

'''

SPECS
X Choose a language (Python, Java, C/C++, or any language of your choice).

X Write an app that generates SHA-256 hashes for input strings or files

X Write an app that uses a simple substitution cipher (Caesar cipher or similar) to encrypt/decrypt input text

X Use OpenSSL or a tool to simulate a digital signature (sign/verify).
 Include a short README explaining your code's functionality
'''

print('SHA-256 DEMO BELOW\n')
# SHA-256 DEMO Below
user_hash_input: str = input('Enter something to be hashed: ')
# encode into bytes
input_string1_bytes = user_hash_input.encode()
#print(input_string1_bytes)
# create hash object
hash_obj = hashlib.sha256(input_string1_bytes)

hashed_input = hash_obj.digest()

print(f'this is your hashed input: {hashed_input}\n')

AKC()

# CREATE SIMPLE CIPHER 
print('SIMPLE CIPHER DEMO BELOW.\n')
# create two lists with the same set of 'runes', but the 'runes' are located at different indices. 
PLAIN_TEXT_RUNES: list = [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    
CAESAR_RUNES: list = [' ', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']

# input to be encrypted
caesar_input: str = ' my dogs are named Mia and Rico'

print(f'Message to be converted to cipher text is: {caesar_input}\n')

# Convert input to an all upper case list so input matches PLAIN_TEXT_RUNES and CAESAR_RUNES expectations.
caesar_list = list(caesar_input.upper())

# declare a list for the encrypted runes to populate
encrypted_list: list = []

#parse each 'rune' in caesar_list
for rune in caesar_list:
 # retrieve index of current 'rune' in PLAIN_TEXT_RUNES
 cipher_rune: int = PLAIN_TEXT_RUNES.index(rune)
 # retrieve the 'rune' from CAESAR_RUNES using index of current 'rune' in PLAIN_TEXT_RUNES
 # append it to encrypted_list
 encrypted_list.append(CAESAR_RUNES[cipher_rune])

# convert encrypted_list elements to string with .join() method
encrypted_message: str = ''.join(encrypted_list)

print('Encrypted message below.\n')
print(encrypted_message, '\n')

# decryption process
print('Decrypted message below.\n')

# list where decrypted 'rune' are stored
decrypted_list: list = []

# parse each rune in encrypted_list
for rune in encrypted_list:
   # retrieve index of current 'rune' in CAESAR_RUNES
   plain_text_rune: int = CAESAR_RUNES.index(rune)
   # Retrieve the 'rune' from PLAIN_TEXT_RUNES using the index of the current 'rune' in CAESAR_RUNES
   # append it to the decrypted_list
   decrypted_list.append(PLAIN_TEXT_RUNES[plain_text_rune])
   # converts list to string with .join() method
   decrypted_message: str = ''.join(decrypted_list)

print(decrypted_message, '\n')

# DIGITAL SIGNATURE DEMO BELOW

AKC()

print('SIGNATURE VALIDATION DEMO BELOW.\n')

# msg to be signed and verified
MASTERCHIEF_MSG: str ='''
UNSC SECURE TRANSMISSION\n
FROM: SIERRA 117
TO ADM. HOOD\n
To give the Covenant back their bomb.\n'''

print(f'Message to be signed is: {MASTERCHIEF_MSG}')

# convert msg to bytes
bytes_msg = MASTERCHIEF_MSG.encode()

# generate public and private key
public_key, private_key = rsa.newkeys(2048)

# sign message with private_key
signature = rsa.sign(bytes_msg, private_key, 'SHA-256')

# TEST: attempt to tamper with message
# bytes_msg = b'222'
# returned VerificationError, confirms verification works

print(f'Signature is:\n {signature}\n')

#encrypt_message with public_key
encrypt = rsa.encrypt(bytes_msg, public_key)

message_receiver: str = 'SIMULATED MESSAGE RECEIVER SIDE.\n'
print(message_receiver)
# decrypt message with private_key
decrypt = rsa.decrypt(encrypt, private_key)
verified = rsa.verify(bytes_msg, signature, public_key)

print(f'signature verified is: \n{verified}\n')

# decode bytes to string
decrypt = decrypt.decode()

print(f'decrypted message is:\n{decrypt}')

  











