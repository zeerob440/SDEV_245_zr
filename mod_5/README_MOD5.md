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

```research implementation```

2. Broken Access (Python)

```
@app.route('/account/<user_id>')
def get_account(user_id):
    user = db.query(User).filter_by(id=user_id).first()
    return jsonify(user.to_dict())
```
- This example allows a user to interact directly with a database with out authentication or authorization, it returns the first user record that matches user input as a dict with user, user_id

3. Cryptographic Failure (Java)
```
public String hashPassword(String password) throws NoSuchAlgorithmException {
    MessageDigest md = MessageDigest.getInstance("MD5");
    md.update(password.getBytes());
    byte[] digest = md.digest();
    return DatatypeConverter.printHexBinary(digest);
```
4. Cryptographic Failure (Python)

```
import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()
```
- this example uses weak SHA-1 hashing. 

```
# correction
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

```

- This implementation uses much stronger hashing than SHA-1 with SHA-256.

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

6.