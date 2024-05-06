
def cios_multiply(multiplicand, multiplier):
    sum = 0
    split_array = [multiplicand[i:i+2] for i in range(0, len(multiplicand), 2)]
    print(split_array)
    for i in range(0,len(split_array), 1):
        sum += int(split_array[i]) * int(multiplier) * 10 ** (len(split_array) - i - 1)
    return sum








