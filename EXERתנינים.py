
def sort(lst):
    lst2 = []
    lst3 = []
    lst4 = []
    lst_ind = []
    for index in range(len(lst)):
        for year in range(lst[index][0], lst[index][1] + 1):
            lst2.append(year)
    # print(lst2)
    for index in range(len(lst2)):
        num = 0
        for index2 in range(len(lst2)):
            if lst2[index] == lst2[index2]:
                num += 1
        lst3.append(num)
    # print(lst3)
    first_place = 0
    sum_place = 0
    for index in range(len(lst3)):
        curr_sum = 0
        for index2 in range(len(lst3)):
            if lst3[index] > lst3[index2]:
                curr_sum += 1
        if curr_sum >= sum_place:
            sum_place = curr_sum
            first_place = lst2[index]
            check = True
            for i in range(len(lst4)):
                if lst4[i] == first_place:
                    check = False
            if check:
                lst4.append(first_place)
                lst_ind.append(sum_place)
    # print(lst_ind)
    # print(lst4)
    lst_5 = []
    for i in range(len(lst_ind)):
        check = True
        for i2 in range(len(lst_ind)):
            if lst_ind[i] < lst_ind[i2]:
                check = False
        if check:
            lst_5.append(lst4[i])

    # print(lst_ind)
    # print(lst4)
    return lst_5


def main():
    lst = []
    N = int(input("Enter a Number: "))
    for i in range(N):
        i, j = map(int, input('Enter two numbers separated by space: ').split())
        # print(i, j)
        lst.append([i, j])
    sorted_list = sort(lst)
    print(sorted_list)


main()
