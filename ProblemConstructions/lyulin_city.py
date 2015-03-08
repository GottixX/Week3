def n_long_list(n):
    n_list = []
    n_input = 0
    start = 0
    while start < n:
        n_input = input("Височина на блока: ")
        n_list = n_list + [n_input]
        start += 1

    return n_list

def int_list(n_list):
    for n in n_list:
        n = int(n)

    return n_list

def visible(n_list):
    visible = []
    visible = visible + [n_list[0]]
    start = 0
    ran = range(1, len(n_list) - 1)

    for number in ran:
        if n_list[number] > visible[start]:
            visible = visible + [n_list[number]]
            start += 1

    return visible

n = input("Брой на блоковете: ")
n = int(n)

n_list = n_long_list(n)
n_list = int_list(n_list)

visibles = visible(n_list)

for visible in visibles:
    print(visible)
