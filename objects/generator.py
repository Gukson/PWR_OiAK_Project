import random

def generate_numbers(amount, file_path):
    with open(file_path, 'w') as file:
        for _ in range(amount):
            random_number = random.randint(10**10, 10**16)
            file.write(str(random_number) + '\n')


def read_file(file_path):
    pairs = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            if i+1 < len(lines):
                pairs.append((lines[i].strip(), lines[i+1].strip()))

    return pairs


