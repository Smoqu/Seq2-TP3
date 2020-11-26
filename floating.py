from sign import sign
from e import expo
from mantisse import mantisse

def floating(string):
    s = sign(string)
    exp = bin(expo(string))
    exp = exp[2:]
    man = mantisse(string)[::-1]
    remove_zeros = man.index('1')
    man = man[remove_zeros:][::-1]

    return f'{s}1,{man}x2^{exp}'

print(floating("11000001001000100000000000000000"))
