def conv_bin_dec_coma(b):
    split = b.split(",")
    
    integer = split[0][::-1]
    floating = split[1]
    
    result_int = 0
    for i in range(len(integer)):
        result_int += int(integer[i]) * (2 ** i)

    result_float = 0
    for j in range(len(floating)):
        result_float += int(floating[j]) * (2 ** -(j + 1))
        
    return result_int + result_float


print(conv_bin_dec_coma("1010,0001"))
