import random
import hashlib
import string

'''
SPECS
In this project, students will create a small application or script that:
    Assignment contains same RBAC preamble as all other assignments, uncertain if include in specs.
    Accepts user input (e.g., a message or file)
    Hashes the input using SHA-256 to ensure integrity
    Encrypts the input using symmetric encryption (e.g., AES)
    Decrypts the content and verifies its integrity via hash comparison
2. Students must also:

Write a short explanation describing how their solution upholds confidentiality, integrity, and availability
Explain the role of entropy and key generation in their implementation.
'''
def superSecretSauce():

    message = input('Enter a message to be hashed, encrypted, and transmitted:\n>>>')

def nedry():
    ydsmw: str = "YOU DIDN'T SAY THE MAGIC WORD!"
    
    for i in range(10000):
        print (ydsmw)
        exit()



# RBAC required? 
class Permissions:
    def __init__(self, role):
        self.__role = input('Enter your role:\n>>>')

if Permissions.__role == "Admin":
    superSecretSauce()
else:
    
    





# hash input
# hash with SHA-256
# Encrypt with AES symmetrical encryption
# Decrypt, verify with hash comparison. 