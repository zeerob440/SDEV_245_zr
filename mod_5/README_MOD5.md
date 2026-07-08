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
they are any instance of any other user. 
The attacker could just use any user_id and gain unauthorized access.


```research implementation repair```

- explanation here 

2. Broken Access (Python)

```
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
```
- This example allows a user to interact directly with a database without authentication or authorization, it returns the first user record that matches user input as a dict with user, user_id

```
# repair here
```
- explain

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

```
public String hashPassword(String password) throws NoSuchAlgorithmException {
    MessageDigest md = MessageDigest.getInstance("SHA-256");
    md.update(password.getBytes());
    byte[] digest = md.digest();
    return DatatypeConverter.printHexBinary(digest);
}
```


- Upgrading to a more computationally expensive hashing algorithm will provide better protection.Replacing MD5 with SHA-256 would be less vulnerable to brute force attacks. 

4. Cryptographic Failure (Python)

```
import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
```
- this example uses weak SHA-1 hashing. 

```
# SECURE REFACTOR
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

```

- This implementation uses much stronger hashing than SHA-1 with SHA-256.which vastly improves password hashing, and make passwords more secure against brute force attacks.

5. Injection (Java)

```
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = '" + username + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
```
- This example is vulnerable to SQL injection because, because user input becomes part of the query.

```
String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = ?";
PreparedStatement stmt = connection.prepareStatement(query);
stmt.setString(1, username);
ResultSet rs = stmt.executeQuery();

```
- This secure implementation creates a parameterized statement with PreparedStatement, which interdicts SQL injection.

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

- This Python with SQLite3 implementation increases security by introducing input sanitization and parameterized inputs to access the database. This prevents SQL injection attacks. 

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

```
# dump whatever framework this implemented with.

# login 
import hashlib

input()

```

- explain here


8. Software and Data Integrity Failures (HTML)

```
<script src="https://cdn.example.com/lib.js"></script>
```

- This implementation runs script from a third-party URL without a verification hash. As designed it could retrieve a malicious script.  

```
<!--Refactored script -->
<script
    src =">https://cdn.example.com/lib.js"
    integrity='sha256-34f53e5...'
<script>
```
- The refactored version validates the JavaScript program with a sha-256 hash with the integrity attribute. It ensures the JavaScript program is the JavaScript program it expects and not tampered with.  

9. Server Side Request Forgery (HTML)

```
url = input("Enter URL: ")
response = requests.get(url)
print(response.text)
```

- This implementation allows the user to directly input an URL. The server would send the request without validating the URL. An attacker could send requests to unapproved URLs

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

- The refactored implementation checks the user's URL input against an approved list of valid URLs, else it denies access. 

10. Identification and Authentication Failures (Java)

```
if (inputPassword.equals(user.getPassword())) { 
    // Login success
}

```
- This implementation appears to store plaintext passwords. This is vulnerable because if a attacker gain access to the database, the plaintext password would be available.

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

- This Python implementation refactors the original Java implementation. Instead of storing plaintext passwords this implementation stores a sHA-256 hash and a salt value. This increases overall security of the password storage process. 