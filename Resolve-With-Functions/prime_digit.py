def to_digits(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = digits + [digit]

        n = n // 10
    return digits

def is_prime(n):
    divisors = range(1, n - 1)
    is_prime = True
    
    for divisor in divisors:
        if n % divisor == 0:
            is_prime = False
    return is_prime

n = input("Enter n: ")
n = int(n)

digits = to_digits(n)

for digit in digits:
    digit = is_prime(digit)


if True in digits:
    print("Yes")
else:
    print("No")
