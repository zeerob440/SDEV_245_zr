from cryptography.fernet import Fernet
import rsa
 

#print (dir(fernet.Fernet))
#print (help(fernet))
symmetrical_welcome: str ='Below is an example of symmetrical encryption.\n'

print (symmetrical_welcome)

# hard coded input string for symmetrical encryption.
tutanota: str = "Hello World"
print(f'The hardcoded input that will be encrypted is:\n{tutanota}.\n')

# convert string into bytes in order for encryption to function as expected. 
tutanota_bytes = tutanota.encode()
# generate key to be used for encrypt and decrypt process.
symmetrical_key = Fernet.generate_key()

print(f'This is the shared key used to encrypt and decrypt the string:\n{symmetrical_key}\n')

# declare var to store generated key
cipher_process = Fernet(symmetrical_key)

# encrypt 'tutanota'
encrypted = cipher_process.encrypt(tutanota_bytes)
# confirm cipher text is returned
print(f'The string has been encrypted into the following cipher text:\n {encrypted}\n')

# recall shared key to decrypt cipher text
decrypted = cipher_process.decrypt(encrypted)
# Convert bytes to string
cleaned_decrypted_output = decrypted.decode()
print(f'Shared key is used to decrypt bytes, then converted to from bytes to string, original message is output:\n{cleaned_decrypted_output}\n')
print('End of symmetrical encryption demonstration.\n')

print('Asymmetric Encryption Demo.\n')

#print(dir(rsa))

msg: str = '''
TURKEY TROTS TO WATER GG FROM CINCPAC ACTION
COM THIRD FLEET INFO COMINCH CTF SEVENTY-SEVEN X
WHERE IS RPT WHERE IS TASK FORCE THIRTY FOUR RR
THE WORLD WONDERS.'''

#convert message to bytes
msg_bytes = msg.encode()

public_key, private_key = rsa.newkeys(2048)

print(f'public_key is:{public_key}')
print()
print(f'private_key is:{private_key}')




