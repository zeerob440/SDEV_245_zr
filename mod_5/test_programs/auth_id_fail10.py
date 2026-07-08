import hashlib
import random

u_name: str = ('Ray Arnold')
u_password: str = ('holdOnToYourButts1993')
    
salty = str(random.random())
u_password = (salty + u_password)
u_password = u_password.encode()

password = (hashlib.sha256(u_password).hexdigest())

# store hash of salt + u_password
userIdentity: dict = {
    'username': u_name, 'user_password': password
}

print(userIdentity)