import os
import magic

objects = []
pathString = ''
filters = {}

def listFiles():
    files = 0
    directories = 0
    for root,dir,filess in os.walk(pathString):
        for directory in dir:
            directories += 1
        for f in filess:
            files += 1
    print('')
    print(str(files) + ' files')
    print('')
    print(str(directories) + ' directory')
    print('')

if __name__ == "__main__":
    print("1. Current Directory")
    print("2. Desktop Directory")
    print("3. Root Directory")
    print("4. Documents Directory")
    choice = int(input("Choose an option: "))
    cases = {
        1 : '.',
        2 : '/Users/kaushik/Desktop',
        3 : '/',
        4 : '/Users/kaushik/Documents/'
    }
    if(choice > 0 and choice < 5):
        pathString = cases[choice]
        listFiles()
    else:
        print("Invalid choice")
