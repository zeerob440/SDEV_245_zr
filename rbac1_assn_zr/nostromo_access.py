# A simple model of access control.
admin_return = '''
NOSTROMO REROUTED\n
TO NEW CO-ORDINATES\n
INVESTIGATE LIFE FORM. GATHER SPECIMEN.\n
PRIORITY ONE\n
INSURE RETURN OF ORGANISM\n
FOR ANALYSIS.\n
ALL OTHER CONSIDERATIONS SECONDARY.\n
CREW EXPENDABLE.\n
'''
user_return ='''
UNABLE TO CLARIFY.\n
NO FURTHER ENHANCEMENT\n
SPECIAL ORDER 937\n
SCIENCE OFFICER EYES ONLY.\n
'''
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role 

    #instantiate class

    warrant_officer = User(name ='Ripley', role = 'user')

    science_officer = User(name = 'Ash', role ='admin')

if User.role == 'user':
    print(user_return)
elif User.role == 'admin':
    print(admin_return)

    

