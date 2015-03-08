def to_number(digits):
    number = 0

    for digit in digits:
        number = number * 10 + digit

    return number

def fib_list(n):
    fib_list = []
    counter = 2
    if n == 1:
        fib_list = [1]
    elif n == 2:
        fib_list = [1, 1]
    else:
        fib_list = [1, 1]
        while counter < n:
            new_num = fib_list[len(fib_list) - 1] + fib_list[len(fib_list) - 2]
            fib_list = fib_list + [new_num]
            counter += 1
            
    return fib_list

def fib_number(n):
    n_list = fib_list(n)
    fib_n = to_number(n_list)

    return fib_n
