import random


class PeopleSet:
    def __init__(self,  size, force_danidin=False):
        self.size = size
        self.familiarity_matrix = [[False for i in range(size)] for i in range(size)]
        break_point = random.random()
        for i in range(size):
            for j in range(size):
                if random.random() > break_point:
                    self.familiarity_matrix[i][j] = True
        if force_danidin:
            danidin = random.randrange(size)
            for i in range(size):
                self.familiarity_matrix[danidin][i] = True
                self.familiarity_matrix[i][danidin] = False
            print('Danidin is {}'.format(danidin+1))
        self.call_count = 0

    def find_danidin(self):
        for i in range(self.size):
            burned = False
            for j in range(self.size):
                if (j != i) and ((not self.familiarity_matrix[i][j]) or self.familiarity_matrix[j][i]):
                    burned = True
                    break
            if not burned:
                return i + 1
        return None

    def familiarity(self, i, j):
        self.call_count += 1
        return self.familiarity_matrix[i-1][j-1]

    def number_of_familiarity_calls(self):
        return self.call_count


def main():
    # Create the list of people, choose the size, and choose if you want to have a "danidin" in the list.
    # If 'force_danidin=True' - there will be a "danidin" person.
    # If 'force_danidin=False' - all values are random, so there may or may not be a "danidin" person.
    people = PeopleSet(size=1000, force_danidin=True)

    candidate = 1
    next = 2

    while next <= 1000:
        check = people.familiarity(candidate, next)
        if not check:
            candidate = next
        next += 1
    check_dan = True
    for i in range(1, 1001):
        if not people.familiarity(candidate, i) and candidate != i:
            check_dan = False
            break
        if people.familiarity(i, candidate) and candidate != i:
            check_dan = False
            break
    num = people.number_of_familiarity_calls()
    if not check_dan:
        print("There is no Danidin!")
    else:
        print("The number of the Danidin: " + str(candidate))

    print("Number of calls: " + str(num))



    # Note that you need to use the method people.familiarity() to check if i knows j. (Remember that for 1000 people, i and j should be between 1-1000, not 0-999)
    # After you're done, you can call people.number_of_familiarity_calls() to see how many times people.familiarity() was called.
    # You can also call people.find_danidin() to see the right answer. That function returns the number of "danidin" person, or None if no "danidin" exists.


main()
