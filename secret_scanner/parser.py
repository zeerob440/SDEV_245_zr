import argparse

'''
parser.py uses argparse to parse CLI files.
'''
def obtain_args():

    # declare parser
    parser = argparse.ArgumentParser(
        prog = 'secret_scanner',
        description = 'Scan a file for potential hardcoded secrets including: usernames, passwords, API keys, GitHub tokens, and AWS keys.'
        )

    # obtain input from CLI
    parser.add_argument('path', help = 'path to file or directory to scan for secrets.')

    # read CLI input, and return
    args = parser.parse_args()
    return args
