def expo(string):
    if len(string) != 32:
        return 'The number must be 32 bits'
    else:
        exp = string[1:9]
        e = int(exp, 2) - 127
        return e
