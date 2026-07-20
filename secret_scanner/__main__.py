from parser import obtain_args
import scanner

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

   
    




