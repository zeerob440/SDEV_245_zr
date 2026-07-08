import hashlib
import random

class userIdentity():

    u_name: str = ('Ray Arnold')
    u_password: str = ('holdOnToYourButts1993'.encode())
    
    salty = str(random.random())
    u_name = (salty + u_name)
    u_name = u_name.encode()

    username = (hashlib.sha256(u_name).hexdigest())
    password = (hashlib.sha256(u_password).hexdigest)
    print(username)

    def __init__(self, username, password):
        self.username = username
        self.password = password

ray = userIdentity()

