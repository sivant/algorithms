import random

diff = 0
count = 0

# def get_lists(num1, num2):
#     global  diff, count
#     if count == 3:
#         diff = 0
#     count += 1
#     print("count: " + str(count))
#     if num1 != num2 and num2 + diff != num1:
#         old_diff = diff
#         diff = num2 - num1 + diff
#         if num2 + diff + old_diff > num1:
#             diff = -(abs(diff))
#         else:
#             diff = abs(diff)
#         if old_diff != diff:
#             count = 0
#     print(diff)

old_diff1 = 0
old_diff2 = 0
diff = 0
count = 0

def get_lists(num1, num2):
    global  diff, old_diff1, old_diff2, count
    count += 1
    print("count: " + str(count))
    if count > 3:
        diff -= old_diff2
    old_diff2 = old_diff1
    old_diff1 = diff
    diff += old_diff1 + num2 - num1
    if num2 + diff != num1:
        diff = -diff

    print(diff)


def main():
    N = int(input("ENTER A NUMBER: "))
    for i in range(N):
        l1 = random.randint(0, 9)
        l2 = random.randint(0, 9)
        print("[" + str(l1) + ", " + str(l2) + "]")

        get_lists(l1, l2)

main()