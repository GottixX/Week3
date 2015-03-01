def is_prime(n):
    divisors = range(2, n - 1)
    is_prime = True
    
    for divisor in divisors:
        if n % divisor == 0:
            is_prime = False
    return is_prime

p = input("Enter p: ")
p = int(p)

q = p + 2
q1 = p - 2

if is_prime(p) == False:
    print(str(p) + " is not a prime.")
elif is_prime(q):
    print(str(q) + " " + str(p))
elif is_prime(q1):
    print(str(p) + " " + str(q1))
elif is_prime(q) and is_prime(q1):
    print(str(q1) + " " + str(p) + " " + str(q))
else:
    print(p + " doesn't have prime twins")
