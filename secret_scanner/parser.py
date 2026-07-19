import argparse

'''
parser.py uses argparse to parse files and directories
'''
def obtain_args():

    # declare parser
    parser = argparse.ArgumentParser()
    
    # obtain input from CLI
    parser.add_argument('path')

    # read CLI input, and return
    args = parser.parse_args()
    return args
