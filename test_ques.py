
check_m = None
check_m2 = None
max = None
old_n = 1


def find(num):
    global check_m, max, old_n, check_m2
    if check_m == None:
        check_m = num
        max = check_m
        check_m2 = check_m
    else:
        check_m = check_m * num
        check_m2 = check_m2 * num
        if check_m > max:
            max = check_m
        elif check_m2 > max:
            max = check_m2
        elif check_m // old_n > check_m and check_m // old_n > 0:
            check_m2 = check_m // old_n
            if check_m2 > max:
                max = check_m2
            max = check_m2


    old_n = old_n * num




lst = [-2, 2, -2, -2, 2]

for val in lst:
    find(val)

print(max)