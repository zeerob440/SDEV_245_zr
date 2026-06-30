import hashlib

'''
decrypt.py serves as the decryption program for the message.
it passes args from superSecretSauce() into decryption(), verifies the hash 
then returns decode_msg
''' 

def decryption(og_hash, encrypt_y_decrypt, encrypted_msg):

    decrypted_message = encrypt_y_decrypt.decrypt(encrypted_msg)

    # verifies hash
    verify_hash = hashlib.sha256(decrypted_message).digest()

    # selection returns verified message, or warns user of integrity issues.
    if og_hash == verify_hash:
         decode_msg = (decrypted_message.decode())
         return(decode_msg)

    else:
         decode_msg = 'Data Integrity not validated!\n'
         return(decode_msg)
