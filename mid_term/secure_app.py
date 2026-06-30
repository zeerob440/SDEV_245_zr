from super_secret import superSecretSauce
from decrypt import decryption
from access_denied import nedry

'''
SPECS
In this project, students will create a small application or script that:
    ? Assignment contains same RBAC preamble as all other assignments, uncertain if included in specs.
    X Accepts user input (e.g., a message or file)
    X Hashes the input using SHA-256 to ensure integrity
    X Encrypts the input using symmetric encryption (e.g., AES)
    X Decrypts the content and verifies its integrity via hash comparison
2. Students must also:

Write a short explanation describing how their solution upholds confidentiality, integrity, and availability
Explain the role of entropy and key generation in their implementation.
'''

if __name__ == '__main__':   
# validate user Role for RBAC simulation
# allows user to three attempts before booting them out.
    attempt: int = 0
    while attempt <= 3:
        role = input(
    '''\nSIMULATES RBAC, ENTER 'Admin' TO ACCESS HASHING AND ENCRYPTION FUNCTION,
OTHERWISE ENTER SOMETHING ELSE.\n
Enter your role:\n>>>''')
        
        if role == 'Admin':
            # access encryption function. 
            encrypted_packet = superSecretSauce()
            # unpack superSecretSauce returns
            encrypted_msg, og_hash, encrypt_y_decrypt = encrypted_packet

            # pass unpacked values through decryption(), print decrypted message. 
            secure_verified_transmission = decryption(og_hash, encrypt_y_decrypt, encrypted_msg)
            print(f'\nSECURE VERIFIED TRANSMISSION FOLLOWS:\n\n{secure_verified_transmission}\n\nEND TRANSMISSION')
            # increment attempt after each attempt instance. 
        else:
            attempt += 1
        # dump user after 3 invalid attempts made. 
        if attempt == 3:
            nedry()
            exit()

