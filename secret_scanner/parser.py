import argparse

'''
parser.py uses argparse to parse CLI files.
'''
def obtain_args():

    # declare parser
    parser = argparse.ArgumentParser(
        prog = 'secret_scanner',
        description = '''Welcome the the secret_scanner application! secret_scanner scans files 
        for secrets that may have been improperly stored. It generates a report on the location and 
        nature of potentially sensitive information.\n
        Scan a file for potential hardcoded secrets including: usernames, passwords, API keys, GitHub tokens, and AWS keys.\n'''
        )

    # obtain input from CLI
    parser.add_argument('path', help = 'Enter path to file or directory to scan for secrets.\n')

    # read CLI input, and return args
    args = parser.parse_args()
    return args
