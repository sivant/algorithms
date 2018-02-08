
def fibo(num):
    pos = 0
    i = 0
    num1 = 0
    pos = 1
    if pos == num:
        return num1
    num2 = 1
    pos = 2
    if pos == num:
        return num2
    while pos < num:
        num1 = num1 + num2
        pos += 1
        if pos == num:
            return num1
        num2 = num1 + num2
        pos += 1
        if pos == num:
            return num2


def fibo1(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    current = 1
    current_loc = 3
    prev = 1
    while current_loc < num:
        next = current + prev
        prev = current
        current = next
        current_loc += 1

    return current


def fibo_r(num):
    if num == 1:
        return 0
    if num == 2:
        return 1

    n_1 = fibo_r(num - 1)
    n_2 = fibo_r(num - 2)
    return n_1 + n_2


"""

fibo(4) --> fibo(3) + fibo(2) --> (fibo(2) + fibo(1)) + fibo(2) --> 1 + 0 + 1 --> 2

fibo(4)
{
    n_1 = fibo(3)
          {
             n_1 = fibo(2)
                   {
                        return 1
                   }
             n_2 = fibo(1)
                   {
                        return 0
                   }
             return n_1 + n_2 = 1 + 0 = 1
        }
    n_2 = fibo(2)
          {
             return 1
          }
    return n_1 + n_2 = 1 + 1 = 2
}

"""


def main():
    inp = int(input('Enter positive integer: '))
    result = fibo_r(inp)
    print('The {}th number in Fibonacci series is: {}'.format(inp, result))


main()
