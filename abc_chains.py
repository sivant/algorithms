import random

# check_a = False
# check_b = False
# check_c = False
# SUM = 0
#
# def get_lett(lett):
#     global check_a, check_b, check_c, SUM
#     if lett == 'A':
#         check_a = True
#     elif lett == 'B' and check_a:
#         check_b = True
#     elif check_a and check_b:
#         check_c = True
#
#     if check_c:
#         SUM += 1
#         check_a = False
#         check_b = False
#         check_c = False
#
#     return SUM

check_a = 0
check_b = 0
check_c = 0
SUM = 0

def get_lett(lett):
    global check_a, check_b, check_c, SUM
    if lett == 'A':
        check_a += 1
    elif lett == 'B' and check_a > 0:
        check_b += 1
        check_a -= 1
    elif check_b > 0:
        SUM += 1
        check_b -= 1




def main():
    # N = int(input("ENTER A NUMBER: "))
    # for i in range(N):
    #     lett = random.randint(1, 3)
    #     if lett == 1:
    #         lett = 'A'
    #     elif lett == 2:
    #         lett = 'B'
    #     else:
    #         lett = 'C'
    #     print(lett, end='')
    #
    #     get_lett(lett)

    for c in 'CABBACABAC':
        get_lett(c)
    print(" ")
    print(SUM)


main()























