# LANG.PY
# THIS FILE IS THE INTERPRETER FOR THE LANGUAGE
# OUTPUTS MINECRAFT COMMANDS FROM INPUT
# INPUT EX. python lang.py "print(@a,'hello')" "print(@a,'hi')"

# Imports

import sys

# Code

global mode # stupid

def compile(args, silent=False):
    # define supported commands
    supported_commands = ["print", "summon", "give","setblock", "fill"]
    what_the_commands_do = {
        "print": {"desc":"prints something to the chat","args": [{"key":"target","pos":1, "input_pos": 0},{"key":"message","pos":3, "input_pos": 1}],"script": "tellraw ;target; [\"\",{\"text\":\";message;\"}]"},
        "summon": {"desc":"summons an entity","args": [{"key":"entity","pos":1,"input_pos": 0},{"key":"position","pos":3,"input_pos": 1}],"script": "summon ;entity; ;position;"},
        "give": {"desc":"gives a player an item","args": [{"key":"target","pos":1,"input_pos": 0},{"key":"item","pos":3,"input_pos": 1}],"script": "give ;target; ;item;"},
        "setblock": {"desc":"sets a block","args": [{"key":"block","pos":1,"input_pos": 1},{"key":"position","pos":3,"input_pos": 0}],"script": "setblock ;position; ;block;"},
        "fill": {"desc":"fills an area","args": [{"key":"from","pos":1,"input_pos": 0},{"key":"to","pos":3,"input_pos": 1},{"key":"block","pos":5,"input_pos": 2}],"script": "fill ;from; ;to; ;block;"}
    }

    # 🍝 spaghetti code time!!! 🍝

    output = ""
    for line in args: # for each line of code'
        if silent == False: print("Line: " + line)
        # break down the line into parts (I wish I knew a better way to do this)
        line = line.replace("(",",") # replace the brackets with commas
        line = line.replace(")",",") # replace the brackets with commas
        parts = line.split(",") # split the line into parts
        parts.pop(len(parts)-1) # remove the last part because it's empty
        if silent == False: print(parts) # should be the parts of the line!
        if parts == []:
            return output
        if parts[0] in supported_commands:
            if silent == False: print(parts[0] + " is supported!")
            # get the data for the command
            command_data = what_the_commands_do[parts[0]]
            if silent == False: print("continuing with data for " + parts[0] + " being " + str(command_data))
            #split the command into parts
            command_parts = command_data["script"].split(";")
            if silent == False: print("command parts: " + str(command_parts))
            # get args positions
            args_pos = []
            for i in command_data["args"]:
                if silent == False:print(i)
                args_pos.append(i["pos"])
            # replace the args in the command
            for i in args_pos:
                if silent == False: print(args)
                if silent == False: print(parts)
                if silent == False: print(i)
                command_parts[i] = parts[args_pos.index(i)+1]
            if silent == False: print(command_parts)
            # join the command parts
            line = ""
            for i in command_parts:
                line = line + i
            #finished!
            if silent == False: print(line)
            output = output + line + "\n"
        else:
            if silent == False: print(parts[0] + " is not supported!")
            if silent == False: print("Is it an import statement?")
            if parts[0] == "import":
                if silent == False: print("It is!")
                if silent == False: print("Importing Module Refrenced") # Warning: your about to see garbage code
                try:
                    with open(parts[1], "r") as f:
                        langmodule = f.readlines()
                    if silent == False: print(langmodule)
                    global mode  # Declare mode as global here
                    mode = "none"
                    for modline in langmodule:
                        if silent == False: print("Current mode:", mode)
                        if silent == False: print("Current line:", repr(modline))  # repr() shows hidden characters
                        if modline.startswith("#"):
                            if silent == False: print("thats just a comment, continue")
                        elif modline.strip() == "$START WHAT IT DOES$":  # Removed \n
                            if silent == False: print("Found WHAT IT DOES marker")
                            mode = "what it does"
                        elif modline.strip() == "$START SUPPORTED COMMANDS$":  # Removed \n
                            if silent == False: print("Found SUPPORTED COMMANDS marker")
                            mode = "supported commands"
                        else:
                            if mode == "supported commands":
                                supported_commands.append(modline.strip())
                            elif mode == "what it does":
                                import json
                                command_data = json.loads(modline)
                                what_the_commands_do.update(command_data)
                    if silent == False: print("Module Loaded")
                    if silent == False: print(supported_commands)
                    if silent == False: print(what_the_commands_do)
                except:
                    if silent == False: print("Module Not Accessable!")
                    return Exception
            else:
                if silent == False: print("Nope, ending!")
                return Exception
    return output

if __name__ == "__main__":
    args = sys.argv # get all args
    args.pop(0) # get run of lang.py
    print(args) # should be our lines of code! 
    print("Finished!")
    compiled = compile(args)
    if compiled == Exception:
        exit(-1)
    print(compiled)