import random
from test.list_utils import gen_list

check_m = None
check_m2 = None
g_max = None
old_n = 1


def init_globals():
    global check_m, check_m2, g_max, old_n
    check_m = None
    check_m2 = None
    g_max = None
    old_n = 1


def find(num):
    global check_m, g_max, old_n, check_m2
    if check_m is None:
        check_m = num
        g_max = check_m
        check_m2 = check_m
    else:
        check_m = check_m * num
        check_m2 = check_m2 * num
        if check_m > g_max:
            g_max = check_m
        elif check_m2 > g_max:
            g_max = check_m2
        elif check_m // old_n > check_m and check_m // old_n > 0:
            check_m2 = check_m // old_n
            if check_m2 > g_max:
                g_max = check_m2
            g_max = check_m2

    old_n = old_n * num


def find_max_product(lst):
    max_factor = lst[0]
    for i in range(len(lst)):
        factor_from_i = lst[i]
        max_factor_from_i = lst[i]
        for j in range(i + 1, len(lst)):
            factor_from_i *= lst[j]
            if factor_from_i > max_factor_from_i:
                max_factor_from_i = factor_from_i
        if max_factor_from_i > max_factor:
            max_factor = max_factor_from_i
    return max_factor


def test_list(lst):
    init_globals()
    for num in lst:
        find(num)
    correct_result = find_max_product(lst)
    if correct_result != g_max:
        print('Error found for: {}'.format(lst))
        print('Result: {}, should be: {}'.format(g_max, correct_result))
        return False
    else:
        return True


def test():
    for i in range(1000):
        lst = gen_list(length=random.randint(1, 12), min_value=-10, max_value=10)
        i = 0
        while i < len(lst):
            if lst[i] == 0:
                del lst[i]
            else:
                i += 1
        print(lst)
        success = test_list(lst)
        if not success:
            return


if __name__ == '__main__':
    test_list([3, -1, 2])
    test_list([-1, -2, -3, 4])
    # test()

# lst = [-2, 2, -2, -2, 2]
#
# for val in lst:
#     find(val)
#
# print(g_max)
