import hashlib

def createAccount():

    create_email = input('Create Email: \n')
    # prompt for password
    create_password_input = (input('Enter your password: \n'))
    # hash password
    password_hash = hashlib.sha256(create_password_input.encode()).hexdigest()
    # store email and password hash in dict
    emailPass: dict = {'email': create_email, 'password': password_hash}
    
    return emailPass

# simulated user instance
user = createAccount()

login_email = input('enter your email to login: ')
login_password = input('Enter your password: ')

login_hash = hashlib.sha256(login_password.encode()).hexdigest()
# check login_email and login_hash against emailPass values. 
if login_email == user['email'] and login_hash == user['password']:
    print('Access granted, email can be updated now.')
else:
    print('Access Denied')
    exit()
