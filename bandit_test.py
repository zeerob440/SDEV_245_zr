
password: str = 'guest'

def beholdMyStuff():
    return 'Behold... my stuff.'

print(password)

if password == 'guest':
    print("pls don't steal my stuff")
    print(beholdMyStuff())
else:
    print(beholdMyStuff())
    