import os
import re

# scanner.py is responsible for scanning files or directories and applying regex pattern to scan for secrets.


'''
regex pattern function, this function searches for strings that match
potential sensitive information in selected files. 
''' 
def regexPatterns(path, line_no, line):

    # flag, evaluates to true is a secret is found. value is returned to scan() 
    secret_found: bool = False

    #PWORD_SEARCH_PATTERN matches 'password', allows optional whitespace before '=' and requires a non-empty password after '='.
    PWORD_SEARCH_PATTERN = r"password\s*=\S+"

    pmatch = re.search(PWORD_SEARCH_PATTERN, line, re.IGNORECASE)
        
    if pmatch:
        print(f'Possible password found in file: {path}, line number:{line_no}, match: {line}')
        secret_found: bool = True
      

    #UNAME_SEARCH_PATTERN matches 'username', allows optional whitespace before '=' and requires a non-empty username after '='.
    USERNAME_SEARCH_PATTERN = r"username\s*=\S+"

    umatch = re.search(USERNAME_SEARCH_PATTERN, line, re.IGNORECASE)

    if umatch:
        print(f'Possible username found in file: {path}, line number:{line_no}, match: {line}')
        secret_found: bool = True

    # Detects hardcoded API key assignments (apikey, api_key, or api-key).
    API_KEY_PATTERN = r"(api[_-]?key|apikey)\s*=\s*\S+"

    api_match = re.search(API_KEY_PATTERN, line, re.IGNORECASE)

    if api_match:
        print(f'Possible API key found in file: {path}, line number:{line_no}, match: {line}')
        secret_found: bool = True

    # matches GitHub tokens beginning with "ghp".
    GITHUB_TOKEN_PATTERN = r"^\s*token\s*=\s*ghp\S*"

    github_token_match = re.search(GITHUB_TOKEN_PATTERN, line, re.IGNORECASE)

    if github_token_match:
        print(f'Possible Github token found in file: {path}, at line number:{line_no}, match: {line}')
        secret_found: bool = True

    # matches any file with 'AKIA' after the '='
    AWS_KEY_PATTERN = r"=\s*AKIA\S*"

    aws_key_match = re.search(AWS_KEY_PATTERN, line, re.IGNORECASE)

    if aws_key_match:
        print(f'Possible AWS key found in file: {path}, at line number:{line_no}, match: {line}')
        secret_found: bool = True

    # returns value to scan()
    return secret_found

'''
scan(path) determines if path and file are valid in try/except block
if files and paths are valid, read file one line at a time
otherwise except FileNotFound error and inform user.
''' 
def scan_file(path):
    
  

    # validate if path and file are valid. 
    try:
            with open(path, 'r') as file:
                any_secrets_found: bool = False
                # enumerate through file lines to assign line number
                # each iteration is passed to regexPatterns()
                # if True secrets were found in this iteration/line
                # if False no secrets were found in this iteration/line
                for line_no, line in enumerate(file, start=1):
                    if regexPatterns(path, line_no, line):
                        any_secrets_found = True

                # if all calls to regexPatterns() False
                # Inform user file is free of secrets.    
                if not any_secrets_found:
                    print(f'No secrets found in: {path}.\n')

    except FileNotFoundError:
        print('File not found!\n')
    
    except PermissionError:
        print(f'Permission denied: {path}')

    
# determine if path is directory or file.
def scan(path):

    if os.path.isfile(path):
        scan_file(path)

    elif os.path.isdir(path):

        print(f'Scanning directory: {path}\n')

        for filename in os.listdir(path):

            complete_file_path = os.path.join(path, filename)
            scan_file(complete_file_path)
    else:
        print(f'invalid path\n')



