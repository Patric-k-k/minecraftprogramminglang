# MAIN.PY
# THIS FILE IS THE MAIN FILE FOR THE LANGUAGE
# JUST GENERAL STUFF
# INPUT EX. python main.py compile in input.mclang out output.mcfunction

# Imports

import sys
from lang import compile

# Code

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "compile":
            if len(sys.argv) == 6:
                print("Compiling...")
                sys.argv.pop(0)
                with open(sys.argv[2], "r") as file:
                    lines = file.readlines()
                    compiled = compile(lines)
                    print("Compiled!")
                    with open(sys.argv[4], "w") as output:
                        output.write(compiled)
            else:
                print("Invalid number of arguments!")
        else:
            print("Invalid command!")
