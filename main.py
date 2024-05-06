#implementacja pisemnego mnożenia
#implementacja mnożenia montomerego

#test na zasadzie AiZO

#mnożenie dla liczb

# i  = a * b

from objects.sos_multiply import sos_multiply
from objects.cios_multiply import cios_multiply
from objects.generator import generate_numbers
from objects.generator import read_file
import time

print(sos_multiply('123', '45'))
print(cios_multiply('123', '45'))

amount = 200
generate_numbers(amount, 'random_numbers.txt')
numbers = read_file('random_numbers.txt')
for pair in numbers:
    start_time = time.time()
    sos_multiply(pair[0], pair[1])
    end_time = time.time()

    execution_time = end_time - start_time

    with open('sos_multiply.txt', 'a') as file:
        file.write(f"{execution_time}\n")

    start_time = time.time()
    cios_multiply(pair[0], pair[1])
    end_time = time.time()

    execution_time = end_time - start_time

    with open('cios_multiply.txt', 'a') as file:
        file.write(f"{execution_time}\n")


