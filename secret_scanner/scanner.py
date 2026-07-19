import os
import re

'''
regex pattern function, this function searches for strings that match
potential sensitive information in selected files. 
''' 
def regexPatterns(path, line_no, line):
    
    #PWORD_SEARCH_PATTERN matches 'password=' along with > 0 whitesepace characters
    PWORD_SEARCH_PATTERN = r"password\s*="

    pmatch = re.search(PWORD_SEARCH_PATTERN, line, re.IGNORECASE)
        
    if pmatch:
        print(f'Possible password found at in file: {path}, line number:{line_no}, match: {line}')


    USERNAME_SEARCH_PATTERN = r"username=\s*="

    umatch = re.search(USERNAME_SEARCH_PATTERN, line, re.IGNORECASE)

    if umatch:
        print(f'Possible username found at in file: {path}, line number:{line_no}, match: {line}')
    

def usernameRegex(line):
    pass

def phoneNumberRegex(line):
    pass 

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



