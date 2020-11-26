def mantisse(string):
    if len(string) != 32:
        return "Number must be 32 bits"
    else:
        man = string[9:32]
        return man

print(mantisse('11000001001000100000000000000000'))