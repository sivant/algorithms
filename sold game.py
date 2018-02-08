

def sold_game(N):
    if N % 11 == 0:
        while N > 0:
            num = int(input("Enter a Number: "))
            N -= num
            print("The current number: " + str(N))
            num = N % 11
            N -= num
            if N == 0:
                N = 1
                print("The current number: " + str(N))
                print("THE COMPUTER WON!")
                break
            else:
                print("The current number: " + str(N))
            num = int(input("Enter a Number: "))
            N -= num
    else:
        while N > 0:
            num = N % 11
            N -= num
            if N == 0:
                N = 1
                print("The current number: " + str(N))
                print("THE COMPUTER WON!")
                break

            else:
                print("The current number: " + str(N))
            num = int(input("Enter a Number: "))
            N -= num






def main():
    N = int(input("Enter a Number: "))
    sold_game(N)

main()