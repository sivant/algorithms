import random


def get_sum(lst):
    sum = 0
    for index in range(len(lst)):
        for index2 in range(len(lst) - 1, index, -1):
            if lst[index2] < lst[index]:
                check_sum = 0
                i = index
                while i <= index2:
                    check_sum += lst[i]
                    i += 1
                if check_sum > sum:
                    sum = check_sum
                break
    return sum


def main():
    # N = int(input("ENTER A NUMBER: "))
    # lst = []
    # for i in range(N):
    #     num = random.randint(0, 49)
    #     lst.append(num)
    lst = [2, 4, 12, 16, 3, 19, 5, 20, 18, 24]
    print(lst)
    print(get_sum(lst))


main()
