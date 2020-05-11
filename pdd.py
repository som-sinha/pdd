# Created by Somaditya Sinha
# 4:20 PM
# 10th May 2020
# A program that creates an alias which can be used to go to the current development directory easily

# TODO
# 1. Add Comments
# 2. Break the program into independent functions
# 3. Add print()s to notify user as to what is happening


# Modules
import os


# Main Function
def main():

    cwd = os.getcwd()
    lineToWrite = f"alias pdd=\"cd {cwd}\"" + "\n\n"
    searchString = lineToWrite[0:10]

    home = os.path.expanduser('~')
    bash_aliases = os.path.abspath(f"{home}/.bash_aliases")


    with open(bash_aliases, 'a+') as aliases, open(f"{home}/.bash_aliases_copy", 'w') as copy:
        aliases.seek(0)
        lines = aliases.readlines() 
        

        initCheck = False
        for line in lines:
            if line[0:15] == "alias pdd-here=":
                initCheck = True

        if initCheck:
            aliases.seek(0)
            for line in lines:
                if not (line[0:(len(searchString))] == searchString):
                    copy.write(line)
            copy.write(lineToWrite)
            
            os.remove(bash_aliases)
            os.replace(bash_aliases + "_copy", bash_aliases)            
        
        else:
            aliases.write(f"alias pdd-here=\"python3 {cwd}/pdd.py\" \n\n")


if __name__ == "__main__":
    main()