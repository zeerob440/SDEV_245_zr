import hashlib
import sqlite3

def theOtherDataBase():
    connect_to_db = sqlite3.connect('mod_5/test_programs/the_other_db.db')
    cursor = connect_to_db.cursor()
    query = 'SELECT * FROM '

class User:
    def __init__(self, name, password, user_id):
        self.name = name
        self.password = password
        self.user_id = user_id

user_1 = User(name = 'Dennis', password = hashlib.sha256("mr goodbytes".encode()).hexdigest(),
               user_id = '040/#xy/67&')
user_2 = User(name = 'Ray', password = hashlib.sha256('sysadmin1993'.encode()).hexdigest(),
              user_id = '023/#wp/42^')

# stores authorized users
auth_users: list = [user_1, user_2]

# get user input
u_login = input('Enter your username: ')
u_password = input('Enter your password: ')
# hash input password
pass_hash = hashlib.sha256(u_password.encode()).hexdigest()

# create flag value, if password exists and user exist evaluate as true
access_granted: bool = False
# compare pass_hash to object attribute password hash with for loop
for user in auth_users:
    if u_login == user.name and pass_hash == user.password:
        print('Access granted\n')
        print(f'user_id is: {user_1.user_id}')
        access_granted: bool = True
        break

# if access_granted == False, deny access.   
if access_granted == False:
    print('Access Denied')
    exit()

print('process good')