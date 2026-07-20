# secret_scanner overview

secret_scanner is a CLI utilities application implemented with argparse, and re. It designed as a package containing __main__.py, scanner.py, parser.py, and a directory called ***depository*** which contains two .txt files. This design decision emphasizes separation of concerns which enhances maintainability, readability. 

secret_scanner allows the user to input a **file or directory** via CLI. __main__.py serves as the application entry point and orchestrator. parser.py handles argparse, user input, and help functionality. scanner.py contains functions for scanning files and directories as well as the regex pattern matching function. Detected secrets are reported to the user by filepath, line number, potential secret found, and specif match.

## How to Use secret_scanner
The entry point to secret_scanner is __main__.py

To scan files or directories they need to first be added to secret_scanner package, otherwise use the default 'depository' directory or child files. 




## Program structure

```
secret_scanner/
├── depository       # directory containing .txt
├── __init__.py
├── __main__.py      # Program entry point
├── parser.py        # Command-line argument parsing
├── scanner.py       # File scanning and regex detection
└── README.md

```

## scanner.py Workflow

1. Receive a path from parser.py.

2. Determine if path is:
    • a file
    • a directory

3. If directory:
    • iterate through each file
    • call scan_file() for every file

4. scan_file() opens the file and reads it one line at a time.

5. Each line is passed to regexPatterns().

6. regexPatterns():
    • compares the line against each secret regex pattern
    • prints a report if a match is found
    • returns True if any pattern matched
    • Otherwise returns False

7. scan_file() tracks whether any call to regexPatterns()
   returned True.

8. After every line has been scanned:
    • if no secrets were found, report that 'No secrets found.'
    • otherwise continue to the next file.

9. When all files have been processed, scanner.py returns
   control to the calling program.

## scanner.py regexPatterns()

regexPatterns() is the function that matches secrets in a given file. regexPatterns() scans for 5 kinds of secrets. if any potential secrets are found they are reported to the user. All patterns used are paired with re.IGNORECASE so literals are not case-sensitive to match.

1. Username
Pattern: username\s*=\S+

Matches potential username assignments by matching 'username', followed by an optional amount of whitespace, an equals sign, and a username value consisting of one or more non-whitespace characters. 

2. Password
Pattern: password\s*=\S+

Matches potential hardcoded 'password', followed by optional whitespace, an equals sign, and one or more non-whitespace characters representing the password value.

3. API Keys
Pattern: (api[_-]?key|apikey)\s*=\s*\S+

Matches possible hardcoded API keys and common API key variable names followed by optional whitespace, an equals sign, another optional whitespace, and one or more non-whitespace characters representing the API key value.

4. GitHub Tokens
Pattern: `^\s*token\s*=\s*ghp\S*`

Matches GitHub personal access tokens when a line starts with 'token', followed by an equals sign and a value beginning with 'ghp' prefix. Optional whitespace is permitted around the assignment operator.

5. AWS Access Tokens

Pattern:`\s*AKIA\S*`

Detects possible AWS Access Key IDs by matching the common AKIA prefix followed by zero or more non-whitespace characters.
