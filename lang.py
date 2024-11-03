# LANG.PY
# THIS FILE IS THE INTERPRETER FOR THE LANGUAGE
# OUTPUTS MINECRAFT COMMANDS FROM INPUT
# INPUT EX. python lang.py "print(@a,'hello')" "print(@a,'hi')"

# Imports

import sys

# Code

# define supported commands
supported_commands = ["print"]
what_the_commands_do = {
    "print": {
        "desc":"prints something to the chat",
        "args": [
            {
                "key":"target",
                "pos":1, 
                "input_pos": 0
            },
            {
                "key":"message",
                "pos":3, 
                "input_pos": 1
            }
        ],
        "script": "tellraw ;target; [\"\",{\"text\":\";message;\"}]"
        }
}

args = sys.argv # get all args
args.pop(0) # get run of lang.py
print(args) # should be our lines of code! 

# 🍝 spaghetti code time!!! 🍝

for line in args: # for each line of code
    # break down the line into parts (I wish I knew a better way to do this)
    line = line.replace("(",",") # replace the brackets with commas
    line = line.replace(")",",") # replace the brackets with commas
    parts = line.split(",") # split the line into parts
    parts.pop(len(parts)-1) # remove the last part because it's empty
    print(parts) # should be the parts of the line!

    if parts[0] in supported_commands:
        print(parts[0] + " is supported!")
        # get the data for the command
        command_data = what_the_commands_do[parts[0]]
        print("continuing with data for " + parts[0] + " being " + str(command_data))
        #split the command into parts
        command_parts = command_data["script"].split(";")
        print("command parts: " + str(command_parts))
        # get args positions
        args_pos = []
        for i in command_data["args"]:
            print(i)
            args_pos.append(i["pos"])
        # replace the args in the command
        for i in args_pos:
            print(args)
            print(parts)
            print(i)
            command_parts[i] = parts[args_pos.index(i)+1]
        print(command_parts)
        # join the command parts
        line = ""
        for i in command_parts:
            line = line + i
        #finished!
        print(line)
    else:
        print(parts[0] + " is not supported!")
        exit(-1) # oh no!

