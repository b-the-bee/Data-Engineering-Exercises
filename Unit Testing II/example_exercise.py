import random

def get_random_number():
    return random.randint(1, 10)

def random_list_generator(n):
    result = []
    for _ in range(n):
        result.append(get_random_number())
    return result