import hashlib
class User:
    def __init__(self, name, password, user_id):
        self.name = name
        self.password = password
        self.user_id = user_id

user_1 = User(name = 'Dennis', password = hashlib.sha256("mr goodbytes".encode()).hexdigest(),
               user_id = '040/#xy/67&')

# get user input
u_login = input('Enter your username: ')
u_password = input('Enter your password: ')
# hash input password
pass_hash = hashlib.sha256(u_password.encode()).hexdigest()

# compare pass_hash to object attribute password hash
if u_login == user_1.name and pass_hash == user_1.password:
    print('Access granted\n')
    print(f'user_id is: {user_1.user_id}')
else:
    print('Access Denied')
    exit()