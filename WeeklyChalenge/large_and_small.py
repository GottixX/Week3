def to_digits(n):
    digits = []
    while n != 0:
        digit = n % 10
        digits = digits + [digit]

        n = n // 10
    return digits

def to_number(digits):
    number = 0

    for digit in digits:
        number = number * 10 + digit

    return number

def max_num(digits):
    digits = sorted(digits, reverse = True)

    return digits

def min_num(digits):
    digits = sorted(digits)

    return digits

n = input("Enter n: ")
n = int(n)

digits = to_digits(n)

maximum = max_num(digits)
minimum = min_num(digits)

max = to_number(maximum)
min = to_number(minimum)

print("Largest: " + str(max))
print("Smallest: " + str(min))
