def to_digits(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = digits + [digit]

        n = n // 10
    return digits

def reverse_int(n):
    result = 0

    while n != 0:
        digit = n % 10
        result = result * 10 + digit

        n = n // 10

    return result

def sum_ints(n):
    digits = to_digits(n)
    total_sum = 0
    
    for digit in digits:
        total_sum += digit

    return total_sum

def product_digits(n):
    digits = to_digits(n)
    total = 1

    for digit in digits:
        total = total * digit

    return total

n = input("Enter n: ")
n = int(n)

print(reverse_int(n))
print(sum_ints(n))
print(product_digits(n))
