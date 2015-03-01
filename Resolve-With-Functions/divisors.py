def divisors(n):
    pot_divisors = range(1, n -1)
    divisors = []
    
    for divisor in pot_divisors:
        if n % divisor == 0:
            divisors = divisors + [divisor]
            
    return divisors


n = input("Enter n: ")
n = int(n)

print(divisors(n))
