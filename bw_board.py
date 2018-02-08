SPACE = ' '
NEW_LINE = '\n'

class WB_Board:
    def __init__(self, size):
        self.matrix = [[0 for i in range(size)] for j in range(size)]
        self.size = size

    def get_cell(self, row, col):
        return self.matrix[row][col]

    def __getitem__(self, item):
        return self.matrix[item]

    def toggle_row(self, row):
        for i in range(self.size):
            self.matrix[row][i] = 1 - self.matrix[row][i]

    def toggle_col(self, col):
        for i in range(self.size):
            self.matrix[i][col] = 1 - self.matrix[i][col]

    def toggle_cell(self, row, col):
        self.matrix[row][col] = 1 - self.matrix[row][col]

    @staticmethod
    def _color_(value):
        if value == 0:
            return 'W'
        else:
            return 'B'

    def __str__(self):
        s = NEW_LINE + SPACE * 2
        for i in range(self.size):
            s += str(i) + SPACE
        s += NEW_LINE
        for row in range(self.size):
            s += str(row) + SPACE
            for item in self.matrix[row]:
                s += self._color_(item) + SPACE
            s += NEW_LINE
        return s


def can_board_be_whitened(board):
    """
    :param board: WB_Board
    :return: True of False
    """
    # write your code here

    
    pass


def main():
    board = WB_Board(10)
    board.toggle_row(0)
    board.toggle_col(2)
    board.toggle_cell(5, 2)
    print(board)
    if can_board_be_whitened(board):
        print('The board can be made all-white')
    else:
        print('The board cannot be made all-white')

main()
