
password: str = 'guest'

def beholdMyStuff():
    return 'Behold... my stuff.'

print(password)

if password == 'guest':
    print("pls don't steal my stuff\n")
    print(beholdMyStuff())
else:
    print(beholdMyStuff())
    