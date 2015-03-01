#begin_functions.py
def square(a):
    return a ** 2

def fact(a):
    numbers = range(1, a)
    result = 1
    for number in numbers:
        result = result * number

    return result

def count_elements(items):
    result = 0

    for item in items:
        result += 1

    return result

def member(x, xs):
    is_member = False
    
    for member in xs:
        if member == x:
            is_member = True

    return is_member

def grades_that_pass(students, grades, limit):
    result = []
    index = 0

    for grade in grades:
        student = students[index]

    
        if grade >= limit:
            result = result + [student]

        index += 1

    return result
