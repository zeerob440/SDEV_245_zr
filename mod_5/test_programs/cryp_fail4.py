#4
import hashlib
# modified unsecure example
bad_password = 'guest'
def hash_password_bad(bad_password):
    return hashlib.sha1(bad_password.encode()).hexdigest()

print(hash_password_bad(bad_password))

# refactored 
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

password = 'seven'

print(hash_password(password))
