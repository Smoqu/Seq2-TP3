def mantisse(string):
    if len(string) != 32:
        return "Number must be 32 bits"
    else:
        man = string[9:32]
        return man