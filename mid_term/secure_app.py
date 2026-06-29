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

    message: str = input('Enter a message to be hashed, encrypted, and transmitted:\n>>>')
    # add salt
    salt_runes: list = list(string.ascii_letters)
    #print(salt_runes)
    rand_range: int = random.randint(33, 71)
    salted_list: list = []

    # create salt string
    for i in range(rand_range):
         random_salt_rune: int = random.randint(0, 51)
         selected_salt = (salt_runes[random_salt_rune])
         salted_list.append(selected_salt)
    processed_salt: str = ''.join(salted_list)
    
    r_salted_list: list = []
    for i in range(rand_range):
         random_salt_rune: int = random.randint(0, 51)
         r_selected_salt = (salt_runes[random_salt_rune])
         r_salted_list.append(r_selected_salt)

    r_processed_salt: str = ''.join(r_salted_list)
 

    print(processed_salt)
    #print(r_processed_salt)
    print(processed_salt + message )
         
         

def nedry():
    
    ydsmw: str = "YOU DIDN'T SAY THE MAGIC WORD!"
    
    for i in range(10000):
        print (ydsmw)

# Simulates RBAC 
def permissions():
    # validate user Role role
    attempt: int = 0
    while attempt <= 3:
            role = input(
'''SIMULATES RBAC, ENTER 'Admin' to access encryption function, otherwise enter something else.\n
Enter your role:\n>>>''')
            if role == 'Admin':
                # access encryption function. 
                superSecretSauce()
                # increment attempt after each attempt instance. 
            else:
                attempt += 1
            # dump user if too many invalid attempts made. 
            if attempt == 3:
                 nedry()
                 exit()

# start program
permissions()


# hash input
# hash with SHA-256
# Encrypt with AES symmetrical encryption
# Decrypt, verify with hash comparison. 