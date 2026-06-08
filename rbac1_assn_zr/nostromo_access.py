import random

# A model of an RBAC program, in cyberspace no one can hear you scream.


def adminQuery(): 
    admin_return: str ='''
    NOSTROMO REROUTED\n
    TO NEW CO-ORDINATES\n
    INVESTIGATE LIFE FORM. GATHER SPECIMEN.\n
    PRIORITY ONE\n
    INSURE RETURN OF ORGANISM\n
    FOR ANALYSIS.\n
    ALL OTHER CONSIDERATIONS SECONDARY.\n
    CREW EXPENDABLE.\n
    '''
    return admin_return


def userQuery():
    user_return: str ='''
    UNABLE TO CLARIFY.\n
    NO FURTHER ENHANCEMENT\n
    SPECIAL ORDER 937\n
    SCIENCE OFFICER EYES ONLY.\n
    '''
    return user_return

class Crew:
    def __init__(self, name, role):
        self.name = name
        self.role = role 

#instantiate class

user_warrant_officer = Crew(name ='Ripley', role = 'user')

admin_science_officer = Crew(name = 'Ash', role = 'admin')


# simulate logged in user without input

nostromo_compliment: list = [user_warrant_officer, admin_science_officer]

simulated_logged_user = random.choice(nostromo_compliment)

    


if Crew.role == 'user':
    execute_user_query = userQuery()
    print(execute_user_query)
elif Crew.role == 'admin':
    execute_admin_query = adminQuery()
    print(execute_admin_query)
else: 
    print('UNABLE TO COMPUTE.\n')

    

