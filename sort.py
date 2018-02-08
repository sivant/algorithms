from test.list_utils import *


def sort(lst):
    for i in range(len(lst)):
        min_val = lst[i]
        min_ind = i
        for index in range(i+1, len(lst)):
            if lst[index] < min_val:
                min_val = lst[index]
                min_ind = index
        val = lst[i]
        lst[i] = lst[min_ind]
        lst[min_ind] = val


def bubble_sort(lst):
    for i in range(len(lst), 0, -1):
        for index in range(i - 1):
            if lst[index] > lst[index + 1]:
                val = lst[index]
                lst[index] = lst[index+1]
                lst[index+1] = val

def merge(lst1, lst2):
    lst3 = []
    index1 = 0
    index2 = 0
    while index1 < len(lst1) and index2 < len(lst2):
        if lst1[index1] < lst2[index2]:
            lst3.append(lst1[index1])
            index1 += 1
        else:
            lst3.append(lst2[index2])
            index2 += 1
    if index1 == len(lst1):
        lst3.extend(lst2[index2:])
    else:
        lst3.extend(lst1[index1:])
    return lst3


for i in range(100):
    l1 = gen_sorted_list(random.randint(0, 20))
    l2 = gen_sorted_list(random.randint(0, 20))
    l3 = merge(l1, l2)
    print(l1)
    print(l2)
    print(l3)
    print()
    assert is_sorted(l3), "the merged list is not sorted"
    assert len(l3) == (len(l1) + len(l2)), "the merged list length is wrong"










#my_list = [21, 4, 1, 3, 6, 56, 8, 0]
#sort(my_list)
#print(my_list)





#l1 = gen_list(20)
#print(l1)
#print('The list is {}sorted'.format('' if is_sorted(l1) else 'not '))

#l2 = gen_sorted_list(10)
#print(l2)
#print('The list is {}sorted'.format('' if is_sorted(l2) else 'not '))

