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
class Crew:
    def __init__(self, name, role):
        self.name = name
        self.role = role 

    #instantiate class

        user_warrant_officer = Crew(name ='Ripley', role = 'user')

        admin_science_officer = Crew(name = 'Ash', role = 'admin')

if Crew.role == 'user':
    print(user_return)
elif Crew.role == 'admin':
    print(admin_return)
else: 
    print('UNABLE TO COMPUTE.\n')

    

