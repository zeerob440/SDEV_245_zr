from cryptography.fernet import Fernet

#print (dir(fernet.Fernet))
#print (help(fernet))

# test message to encrypt. 
tutanota: str = "Hello World"
# must be encoded into bytes first
tutanota_bytes = tutanota.encode()
# generate key
symmetrical_key = Fernet.generate_key()
print('Semmetrical Key below:\n')
print(symmetrical_key)

# declare var to store generated key
cipher_process = Fernet(symmetrical_key)

print(cipher_process)
# encrypt 'tutanota'
encrypted = cipher_process.encrypt(tutanota_bytes)
# confirm cipher text is returned
print('Print Check: Is cipher text output below: TRUE\n')
print(encrypted)

print('Test: printed decrypted tutanota below\n')

decrypted = cipher_process.decrypt(encrypted)
print(decrypted)



