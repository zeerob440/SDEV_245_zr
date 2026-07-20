from parser import obtain_args
import scanner

'''
SPECS
Create a Python-based CLI tool that scans files or directories for common patterns indicating hardcoded secrets, such as:

- C API keys
-  C Passwords
- C Tokens
- C Private keys

C Accept a directory path or file as input
    * use argparse
    * input validation 
    * help messages
    * error handling 

- C Use regex to detect common secret patterns
    * include 5 Regex patterns

- C Output a report includes:
    * filename
    * line number
    * matched string

- Include logging and a clear CLI interface (argparse)

- README with explanation of detection logic and usage
'''

'''
secret_scanner application: secret_scanner scans files and directories
for secrets that may have been improperly stored. It generates a report on the location and 
nature of potentially sensitive information.

Proudly Engineered by Zachary Roberts 19 JUL 2026
"Trust...but verify."
'''
# start program
if __name__ == '__main__':
    args = obtain_args()
    scanner.scan(args.path)

   
    




