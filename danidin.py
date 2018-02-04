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
        for i in range(1, self.size + 1):
            burned = False
            for j in range(1, self.size + 1):
                if (j != i) and ((not self.familiarity(i, j)) or self.familiarity(j, i)):
                    burned = True
                    break
            if not burned:
                return i
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

    # Now write your code to find "danidin".
    # Note that you need to use the method people.familiarity() to check if i knows j. (Remember that for 1000 people, i and j should be between 1-1000, not 0-999)
    # After you're done, you can call people.number_of_familiarity_calls() to see how many times people.familiarity() was called.
    # You can also call people.find_danidin() to see the right answer. That function returns the number of "danidin" person, or None if no "danidin" exists.
    

main()
