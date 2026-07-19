'''
SPECS
Create a Python-based CLI tool that scans files or directories for common patterns indicating hardcoded secrets, such as:

- API keys
- Passwords
- Tokens
- Private keys

Accept a directory path or file as input
    * use argparse
    * input validation 
    * help messages
    * error handling 

- Use regex to detect common secret patterns
    * include 5 Regex patterns

- Output a report includes:
    * filename
    * line number
    * matched string

- Include logging and a clear CLI interface (argparse)

- README with explanation of detection logic and usage
'''