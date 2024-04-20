class ClassicMultiplication:
    multiplicand = []
    multiplier = []


def multiply(multiplicand, multiplier):
    multiplicand_digits = [int(digit) for digit in str(multiplicand)]

    multiplier_digits = [int(digit) for digit in str(multiplier)]

    results = [0] * (len(multiplicand_digits) + len(multiplier_digits))

    for i in range(len(multiplicand_digits)-1, -1, -1):
        for j in range(len(multiplier_digits)-1, -1, -1):
            results[i + j + 1] += multiplicand_digits[i] * multiplier_digits[j]
            results[i + j] += results[i + j + 1] // 10
            results[i + j + 1] %= 10

    return int(''.join(map(str, results)))
