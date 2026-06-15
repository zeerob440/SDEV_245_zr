from cryptography.fernet import Fernet

#print (dir(fernet.Fernet))
#print (help(fernet))

makes_a_key = Fernet.generate_key()
print(makes_a_key)
tutanota: str = "Hello World"

#encrypted = encrypt(tutanota)

#print(encrypted)
