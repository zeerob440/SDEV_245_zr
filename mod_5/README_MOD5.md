1. Broken Access (JavaScript)

```
app.get('/profile/:userId', (req, res) => {
    User.findById(req.params.userId, (err, user) => {
        if (err) return res.status(500).send(err);
        res.json(user);
    });
});
```

- This example appears to fail to authenticate a user's user_id,
and also fails to authorize a user as a result because as written any user can say
they are any instance of any other user. The attacker could just use any user_id and gain unauthorized access.

- REFACTORED IMPLEMENTATION: This Python implementation first authenticates a user with a password before a user is granted access to the user_id. This refactor prevents users from gaining sensitive information by just using a known user_id to access the system.

- [problem1 link]('mod_5/test_programs/b_access1.py)

```
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
```

2. Broken Access (Python)

```
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
```
- This example allows a user to interact directly with a database without authentication or authorization, it returns the first user record that matches user input as a dict with user, user_id

- This Python implementation expands on the previous refactor. It uses RBAC to authenticate and authorize a user before the database is accessed. With this implementation authorization and authentication must be verified before the the database can be accessed. 
```
import hashlib
import sqlite3

def theOtherDatabase():
    # database is not accessed without authorization
    connect_to_db = sqlite3.connect('mod_5/test_programs/the_other_db.db')
    cursor = connect_to_db.cursor()
    # no user input, parameterized input not required
    query = 'SELECT phrase FROM user WHERE user_id = 1'
    cursor.execute(query)
    result = cursor.fetchone()

    return result

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
        print(f'user_id is: {user_1.user_id}\n')
        access_granted: bool = True
        break

# if access_granted == False, deny access.   
if access_granted == False:
    print('Access Denied')
    # exit program before database is reachable.
    exit()
# database query return. 
print('Database accessed!')
print(theOtherDatabase())
```


3. Cryptographic Failure (Java)
```
public String hashPassword(String password) throws NoSuchAlgorithmException {
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update(password.getBytes());
    byte[] digest = md.digest();
    return DatatypeConverter.printHexBinary(digest);
}
```
- MD5 is a weak hashing algorithm, GPUs can calculate them quickly. Therefore, a more computationally costly hashing algorithm should be used. 


- REFACTORED IMPLEMENTATION: Upgrading to a more computationally expensive hashing algorithm will provide better protection.Replacing MD5 with SHA-256 would be less vulnerable to brute force attacks. 
```
public String hashPassword(String password) throws NoSuchAlgorithmException {
    MessageDigest md = MessageDigest.getInstance("SHA-256");
    md.update(password.getBytes());
    byte[] digest = md.digest();
    return DatatypeConverter.printHexBinary(digest);
}
```

4. Cryptographic Failure (Python)

```
import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
```
- This example uses weak SHA-1 hashing. 


- REFACTORED IMPLEMENTATION: This implementation uses much stronger hashing than SHA-1 with SHA-256.which vastly improves password hashing, and make passwords more secure against brute force attacks.
```
# SECURE REFACTOR
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

```



5. Injection (Java)

```
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = '" + username + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
```
- This example is vulnerable to SQL injection because, because user input becomes part of the query.

- REFACTORED IMPLEMENTATION: This secure implementation creates a parameterized statement with PreparedStatement, which interdicts SQL injection.
```
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setString(1, username);
ResultSet rs = stmt.executeQuery();

```

6. Injection (JavaScript)

```
app.get('/user', (req, res) => {
    // Directly trusting query parameters can lead to NoSQL injection
    db.collection('users').findOne({ username: req.query.username }, (err, user) => {
        if (err) throw err;
        res.json(user);
    });
});
```

- This implementation directly trusts user input to parse a database. This is unsecure because SQL Injection can occur. 

- REFACTORED IMPLEMENTATION: This Python with SQLite3 implementation increases security by introducing input sanitization and parameterized inputs to access the database. This prevents SQL injection attacks.
```
import sqlite3

# sanitize user input. 
while True:
    user_id = input('enter id: ')
    if user_id.isdigit():
        user_id = int(user_id)
        break
    else:
        print('ENTER A DIGIT!\n')
        
connect_db = sqlite3.connect('mod_5/test_programs/the_database.db')
db_cursor = connect_db.cursor()
# create SQL query string with placeholder
query_string: str='SELECT * FROM users WHERE user_id = ?'
# use parameterized input
db_cursor.execute(query_string, (user_id,))

result = db_cursor.fetchone()

print(result)
```

7. Insecure Design (Python)
```
@app.route('/reset-password', methods=['POST'])
def reset_password():
    email = request.form['email']
    new_password = request.form['new_password']
    user = User.query.filter_by(email=email).first()
    user.password = new_password
    db.session.commit()
    return 'Password reset'
```
- This implementation is insecure because if an attacker knows the user's email, they can simply 
    change the user's password to something the attacker knows. 

- REFACTORED IMPLEMENTATION: This plain Python implementation requires the user to create an account, then login to the account to change their email. The implementation stores user passwords as hashes, then compares the login_inputs to the stored password hashes to grant access. Else it denies access. 

```
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
```

# login 
import hashlib

input()

```

8. Software and Data Integrity Failures (HTML)

```
<script src="https://cdn.example.com/lib.js"></script>
```

- This implementation runs script from a third-party URL without a verification hash. As designed it could retrieve a malicious script. 

- REFACTORED IMPLEMENTATION: The refactored version validates the JavaScript program with a sha-256 hash with the integrity attribute. It ensures the JavaScript program is the JavaScript program it expects and not tampered with. 

```
<!--Refactored script -->
<script
    src =">https://cdn.example.com/lib.js"
    integrity='sha256-34f53e5...'
<script>
```
 
9. Server Side Request Forgery (HTML)

```
url = input("Enter URL: ")
response = requests.get(url)
print(response.text)
```

- This implementation allows the user to directly input an URL. The server would send the request without validating the URL. An attacker could send requests to unapproved URLs

- REFACTORED IMPLEMENTATION: The refactored implementation checks the user's URL input against an approved list of valid URLs, else it denies access.

```
approved_server_lst: list = ['URL1', 'URL2', 'URL3']

url = input('Enter URL: ')

if url in approved_server_lst:
    response: str = 'URL Approved!'
    print(response)
else:
    print('Sorry, something went wrong!')
    exit()

```

10. Identification and Authentication Failures (Java)

```
if (inputPassword.equals(user.getPassword())) { 
    // Login success
}

```
- This implementation appears to store plaintext passwords. This is vulnerable because if a attacker gain access to the database, the plaintext password would be available.

- REFACTORED IMPLEMENTATION: This Python implementation refactors the original Java implementation. Instead of storing plaintext passwords this implementation stores a sHA-256 hash and a salt value. This increases overall security of the password storage process. 

```
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
```

