import os
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
    if is_path_valid == True and is_file == True:
        with open(path, 'r') as file:
            print(file.read())


