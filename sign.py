def sign(string):
    sign = string[0]

    if sign == "0":
        return "+"
    elif sign == "1":
        return "-"
    else:
        return "It has to be binary"