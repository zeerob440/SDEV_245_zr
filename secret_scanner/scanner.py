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
    try:
        if is_path_valid == True and is_file == True:
            with open(path, 'r') as file:
                # enumerate through file lines to assign line number
                for line_no, line in enumerate(file, start=1):
                    print(f'{line_no}: {line}')
    except FileNotFoundError:
        print('File not found!\n')



