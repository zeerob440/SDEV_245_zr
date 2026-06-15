from cryptography.fernet import Fernet

#print (dir(fernet.Fernet))
#print (help(fernet))

# test message to encrypt. 
tutanota: str = "Hello World"
# generate key
symmetrical_key = Fernet.generate_key()
print(symmetrical_key)

# declare var to store generated key
cipher_process = Fernet(symmetrical_key)

print(cipher_process)
# encrypt 'tutanota'
encrypted = cipher_process.encrypt(tutanota)
# confirm cipher text is returned
print('Print Check: Is cipher text output below?\n')
print(encrypted)



