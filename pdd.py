# Created by Somaditya Sinha
# 4:20 PM
# 10th May 2020
# A program that creates an alias which can be used to go to the current development directory easily

# Modules
import os
import re

def main():

    cwd = os.getcwd()
    lineToWrite = f"alias pdd=\"cd {cwd}\"" + "\n\n"
    searchString = lineToWrite[0:11]

    home = os.path.expanduser('~')
    bash_aliases = os.path.abspath(f"{home}/.bash_aliases")

    with open(bash_aliases, 'r+') as aliases, open(f"{home}/.bash_aliases_copy", 'w') as copy:
        lines = aliases.readlines()
        copy.writelines(lines)

        matchFound = False
        for loc, line in enumerate(lines):
            if line[0:(len(searchString))] == searchString:
                lines.pop(loc)
                lines.append(lineToWrite)
                matchFound = True
        if not matchFound:
            lines.append(lineToWrite)

        aliases.seek(0)
        aliases.writelines(lines)


if __name__ == "__main__":
    main()