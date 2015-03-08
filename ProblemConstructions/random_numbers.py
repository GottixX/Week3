from random import randint

def generate_random_list(n, start, end):
    random_list = []
    start_end = randint(start, end)
    index = 0
    while index < n:
        random_list = random_list + [start_end]
        index += 1

    return random_list
