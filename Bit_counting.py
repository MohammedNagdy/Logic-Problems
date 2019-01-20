def countBits(n):
    n = abs(n)
    binary = bin(n)[2:].zfill(8)
    num_ones = 0
    for i in binary:
        if i == "1":
            num_ones += 1
    return num_ones
