
check = 0
loc = 1

def fibo(num):
    i = num
    global check, loc
    num1 = 0
    num2 = 1
    if num == 1:
        return 0
    elif num == 2:
        return 1
    for index in range(i):
        num1 = num1 + num2
        num2 = num1 + num2
    return i

f = fibo(3)

print(f)







