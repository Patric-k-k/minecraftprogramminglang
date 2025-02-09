def getLineParts(line):
    line = line.replace("(",",") # replace the brackets with commas
    line = line.replace(")",",") # replace the brackets with commas
    parts = line.split(",") # split the line into parts
    parts.pop(len(parts)-1) # remove the last part because it's empty
    return parts