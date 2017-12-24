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

def merge(lst, lst2):
    lst3 = []
    for index in range(len(lst)):
        for index in range(len(lst2)):
            if lst[index] < lst2[index]:
                lst3.append(lst[index])
            elif lst[index] > lst2[index]:
                lst3.append(lst2[index])
            else:
                lst3.append(lst[index])
                lst3.append(lst2[index])
    print(lst3)







lstt = [1, 3, 4, 7]
lstt2 = [2, 5, 6]

merge(lstt, lstt2)





list4 = [21, 41, 45, 1, 11, 2, 12, 10, 91, 11]


#bubble_sort(list2)
#print(list2)









my_list = [21, 4, 1, 3, 6, 56, 8, 0]
sort(my_list)
#print(my_list)





l1 = gen_list(20)
print(l1)
print('The list is {}sorted'.format('' if is_sorted(l1) else 'not '))

l2 = gen_sorted_list(10)
print(l2)
print('The list is {}sorted'.format('' if is_sorted(l2) else 'not '))

