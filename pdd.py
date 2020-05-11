# Created by Somaditya Sinha
# 4:20 PM
# 10th May 2020
# A program that creates an alias which can be used to go to the current development directory easily

# Modules
import os
import re

def main():

    cwd = os.getcwd()
    writeLine = "alias ppd=\"{cwd}\""
    searchLine = re.compile("alias ppd")

    home = os.path.expanduser('~')
    bash_aliases = os.path.abspath(f"{home}/.bash_aliases")
    
    with open(bash_aliases, "a+") as aliases:
        lines = aliases.readlines()
        for line in lines:
            if searchLine.match(line):
                


if __name__ == "__main__":
    main()