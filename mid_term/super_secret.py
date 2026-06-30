import hashlib
from cryptography.fernet import Fernet

'''
Creates hash and encrypts user message after RBAC confirmed.
returns packet that is decrypted by decrypt.py 
'''
def superSecretSauce():

    message: str = input('Enter a message to be hashed, encrypted, and transmitted:\n>>>')
    # converts message to bytes
    msg_bytes: bytes = message.encode()
   
    og_hash = (hashlib.sha256(msg_bytes).digest())
    
    '''
    #test if hash functions as designed:

    msg_bytes = b'1324'

    data tampering detected, decrypt.py output 'Data Integrity not validated!'

    Program functions as designed. 
    '''
    # generate symmetrical key
    sym_key: bytes = Fernet.generate_key()

    #instantiate key
    encrypt_y_decrypt: Fernet = Fernet(sym_key)

    # encrypt message
    encrypted_msg: bytes = encrypt_y_decrypt.encrypt(msg_bytes)
    
    packet_for_decryption = (encrypted_msg, og_hash, encrypt_y_decrypt)
    return packet_for_decryption