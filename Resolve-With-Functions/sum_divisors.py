def divisors(n):
    pot_divisors = range(1, n -1)
    divisors = []
    
    for divisor in pot_divisors:
        if n % divisor == 0:
            divisors = divisors + [divisor]
            
    return divisors

def sum_ints(numbers):
    sum_ints = 0

    for number in numbers:
        sum_ints += number

    return sum_ints


n = input("Enter n: ")
n = int(n)

numbers = divisors(n)

print(sum_ints(numbers))
