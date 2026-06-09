import random

# A model of an RBAC program, in cyberspace no one can hear you scream.

# returns this doc string if role == 'admin'
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

# returns this doc string if role == 'user'
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


# simulate logged in user without input, by placing class instances into list.

nostromo_compliment: list = [user_warrant_officer, admin_science_officer]

# selects class instance with random.choice
simulated_logged_user = random.choice(nostromo_compliment)

welcome: str = f'''WELCOME {simulated_logged_user.name}\n
INTERFACE 2037 READY FOR INQUIRY
________________________________\n'''  


if simulated_logged_user.role == 'user':
    execute_user_query = userQuery()
    print (welcome)
    print(execute_user_query)
elif simulated_logged_user.role == 'admin':
    execute_admin_query = adminQuery()
    print (welcome)
    print(execute_admin_query)
else: 
    print('UNABLE TO COMPUTE.\n')

    

