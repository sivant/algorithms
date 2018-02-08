def r(n):
    sum = 0
    for i in range(n + 1):
        sum = sum + i
    return(sum)


def atzeret(n):
    if n == 1:
        return 1
    else:
        val = atzeret(n-1)
        return val * n

def sumatz(n):
    if n ==1:
        return 1
    else:
        val = sumatz(n - 1)
        return val + n

def calc_sum_d():
    num = int(input('Enter positive integer: '))
    result = resum(num)
    print('{} = {}'.format(num, result))


def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

def resum(num):
    if num == 0:
        return 0
    else:
        return num % 10 + resum(num // 10)



# print(r(10))
calc_sum_d()
