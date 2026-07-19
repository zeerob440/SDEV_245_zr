import os
import re

'''
regex pattern function, this function searches for strings that match
potential sensitive information in selected files. 
''' 
def regexPatterns(path, line_no, line):
    
    #PWORD_SEARCH_PATTERN matches 'password', allows optional whitespace before '=' and requires a non-empty password after '='.
    PWORD_SEARCH_PATTERN = r"password\s*=\S+"

    pmatch = re.search(PWORD_SEARCH_PATTERN, line, re.IGNORECASE)
        
    if pmatch:
        print(f'Possible password found at in file: {path}, line number:{line_no}, match: {line}')

    #UNAME_SEARCH_PATTERN matches 'username', allows optional whitespace before '=' and requires a non-empty username after '='.
    USERNAME_SEARCH_PATTERN = r"username\s*=\S+"

    umatch = re.search(USERNAME_SEARCH_PATTERN, line, re.IGNORECASE)

    if umatch:
        print(f'Possible username found at in file: {path}, line number:{line_no}, match: {line}')

    # Detects hardcoded API key assignments (apikey, api_key, or api-key).
    API_KEY_PATTERN = r"(api[_-]?key|apikey)\s*=\s*\S+"

    api_match = re.search(API_KEY_PATTERN, line, re.IGNORECASE)

    if api_match:
        print(f'Possible username found at in file: {path}, line number:{line_no}, match: {line}')


def gHToken(line):
    pass

def accountNumber(line):
    pass 


# scanner.py reads cli args
def scan(path):
    # determine if path is directory or file.
    is_path_valid = os.path.exists(path)
    is_file =os.path.isfile(path)

    # print checks
    print(path)
    print(is_path_valid)
    print(is_file)

    # validate if path and file are valid. 
    try:
        if is_path_valid == True and is_file == True:
            with open(path, 'r') as file:
                # enumerate through file lines to assign line number
                for line_no, line in enumerate(file, start=1):
                    regexPatterns(path, line_no, line)
                    #print(f'{line_no}: {line}')
    except FileNotFoundError:
        print('File not found!\n')



