class TicTacToe:
    # creates empty field
    def __init__(self):
        self.field = list("_________")

    #  output type
    def __str__(self):
        msg = "---------\n"
        for i in range(3):
            msg += f"| {' '.join(list(self.field[i * 3:3 * (i + 1)]))} |\n"
        msg += "---------\n"
        return msg

    # checks input and makes a move
    def make_move(self, move):
        while True:
            try:
                x, y = [int(num) for num in input().split()]
                if not (0 < x < 4 and 0 < y < 4):
                    print("Coordinates should be from 1 to 3!")
                elif self.field[y - 1 + 3 * (x - 1)] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    self.field[y - 1 + 3 * (x - 1)] = move
                    break
            except ValueError:
                print("You should enter numbers!")

    # checks if the game is over
    def is_end(self):
        win_positions = list()
        win_positions.append(self.field[0] + self.field[1] + self.field[2])  # first line
        win_positions.append(self.field[3] + self.field[4] + self.field[5])  # second line
        win_positions.append(self.field[6] + self.field[7] + self.field[8])  # third line

        win_positions.append(self.field[0] + self.field[3] + self.field[6])  # first column
        win_positions.append(self.field[1] + self.field[4] + self.field[7])  # second column
        win_positions.append(self.field[2] + self.field[5] + self.field[8])  # third column

        win_positions.append(self.field[0] + self.field[4] + self.field[8])  # diagonal from left top to right bottom
        win_positions.append(self.field[2] + self.field[4] + self.field[6])  # diagonal from right top to left bottom

        winner = ""
        winner += 'X' * win_positions.count('XXX')
        winner += 'O' * win_positions.count('OOO')

        if len(winner) == 1:
            print(f"{winner} wins")
        elif self.field.count('_') == 0:
            print("Draw")
        else:
            return False  # returns False if game is not over
        return True

    # starts a game
    def game(self):
        print(self)
        move = 'X'
        while not self.is_end():
            self.make_move(move)
            print(self)
            move = 'O' if move == 'X' else 'X'


if __name__ == "__main__":
    TicTacToe.game(TicTacToe())
