# pdd
present development directory
I wanted to make "something" in python to practice I made this. It works tho, so that must be a good thing.

### Installation:
**Note: I have tested this on Linux only(Ubuntu 20.04 Foccal Fossa). However it should run on any unix-like system that uses bash/zsh**
1. Clone the files.
2. Using python3 from your terminal run pdd.py from its directory.
   
   `python3 /PATH/TO/pdd.py`
3. You only need to do this once!

### Usage:
**Note: if using zsh, put this into your .zshrc**
                                          
```
if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi
```
1. Open the directory where you're working in the terminal. 
2. run `pdd-here`.
3. From now on whenever you type ppd it will take you to that directory.
4. If you want to change the directory just run `pdd-here` again wherever you are working.

### Updates:
#### First version:
As I wrote this in a day's time, I wasn't able to focus on the readability. Currently the code is basically unreadable unless you are me!
I wrote this just to get more comfortable programming. It is just my first independent project.

### TODO
1. Add Comments
2. Break the program into independent functions
3. Add print()s to notify user as to what is happening
