# secret_scanner overview

secret_scanner is a CLI utilities application implemented with argparse, and re. It designed as a package containing __main__.py, scanner.py, parser.py, and a directory called ***depository*** which contains two .txt files. This design decision emphasizes separation of concerns which enhances maintainability, readability. 

secret_scanner allows the user to input a **file or directory** via CLI. __main__.py serves as the application entry point and orchestrator. parser.py handles argparse, user input, and help functionality. scanner.py contains functions for scanning files and directories as well as the regex pattern matching function. Detected secrets are reported to the user by filepath, line number, potential secret found, and specif match. 

# scanner.py workflow

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