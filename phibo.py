
check = 0
loc = 1

def fibo(num):
    global check, loc
    num1 = 0
    num2 = 1
    while num1 <= num or num2 <= num:
        if num == num1:
            check = 1
            return loc
        loc += 1
        num2 = num1+num2
        if num == num2:
            check = 1
            return loc
        loc += 1
        num1 = num1+num2
    return False

fibo(34)

if check == 0:
    print("The number doesn't exist..")
else:
    print("The location of the number you're looking for is " + str(loc) + "..")












