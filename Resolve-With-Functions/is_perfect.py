def sum_ints(numbers):
    sum_ints = 0

    for number in numbers:
        sum_ints += number

    return sum_ints

def is_perfect(n):
    pot_divisors = range(1, n - 1)
    divisors = []
    is_perfect = False
    
    for divisor in pot_divisors:
        if n % divisor == 0:
            divisors = divisors + [divisor]
    if n == sum_ints(divisors):
        is_perfect = True

    return is_perfect


n = input("Enter n: ")
n = int(n)

n_is_perfect = is_perfect(n)

if n_is_perfect == True:
    print("n is perfect")
else:
    print("n is not perfect")
