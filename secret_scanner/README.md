# secret_scanner overview

secret_scanner is a CLI utilities application implemented with argparse, and re. It designed as a package containing __main__.py, scanner.py, parser.py, and a directory called ***depository*** which contains two .txt files. This design decision emphasizes separation of concerns which enhances maintainability, readability. 

secret_scanner allows the user to input a **file or directory** via CLI. __main__.py serves as the application entry point and orchestrator. parser.py handles argparse, user input, and help functionality. scanner.py contains functions for scanning files and directories as well as the regex pattern matching function. Function regexPatterns() 

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