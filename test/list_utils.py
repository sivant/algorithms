import random


def gen_list(length: int, max_value: int=None, min_value: int=None):
    """
    generate a list with random integer values
    :param length: the length of the generated list
    :param min_value: the minimum value an element might have
    :param max_value: the maximum value an element might have
    :return: the generated list
    """
    assert (min_value is None) or (max_value is not None), "gen_list called with min_value without max_value"
    if max_value is None:
        max_value = length
    if min_value is None:
        min_value = min(max_value - length, 0)
    return list(random.randint(min_value, max_value) for i in range(length))


def gen_sorted_list(length: int, start_value: int=None, max_step=3):
    """
    generate a sorted list
    :param length: the length of the generated list
    :param start_value: the value of the first element. If not specified, generated between 0 and max_step
    :param max_step: the difference between each element and the one next to it is randomly generated between 0 and max_step
    :return: the generated list
    """
    assert max_step > 0, "gen_sorted_list called with invalid value in param max_step"
    if start_value is None:
        start_value = random.randint(0, max_step)
    lst = []
    current_value = start_value
    for i in range(length):
        lst.append(current_value)
        current_value = current_value + random.randint(0, max_step)
    return lst


def is_sorted(lst: list):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


if __name__ == '__main__':
    lst = gen_list(10)
    print(lst)
    assert len(lst) == 10
    assert min(lst) >= 0
    assert max(lst) <= 10

    lst = gen_list(20, 30)
    print(lst)
    assert len(lst) == 20
    assert max(lst) <= 30
    assert min(lst) >= 0

    lst = gen_list(20, 30, 15)
    print(lst)
    assert len(lst) == 20
    assert max(lst) <= 30
    assert min(lst) >= 15

    lst = gen_sorted_list(10)
    print(lst)
    assert len(lst) == 10
    assert sorted(lst) == lst

    lst = gen_sorted_list(10, 4, 5)
    print(lst)
    assert len(lst) == 10
    assert sorted(lst) == lst
    assert lst[0] == 4
    for i in range(len(lst) - 1):
        assert lst[i+1] <= (lst[i] + 5)

