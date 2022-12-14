import random


class TicTacToe:
    def __init__(self):
        self.field = list("_________")
        self.current_sign = 'X'
        self.current_move = None
        self.player_1 = None
        self.player_2 = None

    def __str__(self):
        msg = "---------\n"
        for i in range(3):
            msg += f"| {' '.join(list(self.field[i * 3:3 * (i + 1)]))} |\n"
        msg += "---------"
        return msg

    # AI for an easy difficulty. Chooses random move on the field.
    def easy(self):
        while True:
            move = random.randrange(9)
            if self.field[move] == "_":
                self.field[move] = self.current_sign
                break

    # AI for medium difficulty. If in the next move there is a possible win or lose. It will make this move. Otherwise works as easy difficulty
    def medium(self):
        loses = list()
        for pos in range(9):
            if self.field[pos] == '_':
                self.field[pos] = self.current_sign
                if self.game_status() == self.current_sign:
                    return
                self.field[pos] = 'O' if self.current_sign == 'X' else 'X'
                if self.game_status() != '':
                    loses.append(pos)
                self.field[pos] = '_'
        if loses:
            self.field[loses[0]] = self.current_sign
        else:
            self.easy()

    # AI for hard difficulty. Uses minmax algorythm for finding the best move. Imposible to lose. Only draw with it is possible.
    def hard(self, sign, root=False):
        status = self.game_status()
        if status == self.current_sign:
            return 10
        if status == ('X' if self.current_sign == 'O' else 'O'):
            return -10
        if self.field.count('_') == 0:
            return 0

        moves = dict()
        for tile in range(9):
            if self.field[tile] == '_':
                self.field[tile] = sign
                moves[tile] = self.hard('X' if sign == 'O' else 'O')
                self.field[tile] = '_'
        if root:
            self.field[max(moves, key=moves.get)] = self.current_sign
            print(moves)
        return max(moves.values()) if self.current_sign == sign else min(moves.values())

    # Checks user's input of a move
    def user(self):
        while True:
            try:
                x, y = [int(num) for num in input('Enter the coordinates: ').split()]
                if not (0 < x < 4 and 0 < y < 4):
                    print("Coordinates should be from 1 to 3!")
                elif self.field[y - 1 + 3 * (x - 1)] != "_":
                    print("This cell is occupied! Choose another one!")
                else:
                    self.field[y - 1 + 3 * (x - 1)] = self.current_sign
                    break
            except ValueError:
                print("You should enter numbers!")

    # Makes a move depending on difficulty or user
    def make_move(self):
        if self.current_move == 'easy':
            print('Making move level "easy"')
            self.easy()
        elif self.current_move == 'medium':
            print('Making move level "medium"')
            self.medium()
        elif self.current_move == 'hard':
            print('Making move level "hard"')
            self.hard(self.current_sign, True)
        elif self.current_move == 'user':
            self.user()

    # Returns a str with a winner in it. If it is empty then no winners. If it is longer than 1 then there is an error on the field
    def game_status(self):
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
        return winner

    # Checks whether the game is over
    def is_end(self):
        winner = self.game_status()
        if len(winner) == 1:
            print(f"{winner} wins")
        elif self.field.count('_') == 0:
            print("Draw")
        else:
            return False
        return True

    # Takes input from user for game options
    def choose_game_mode(self):
        game_modes = ['easy', 'user', 'medium', 'hard']
        while True:
	    print('"exit", "start", "user", "easy", "medium", "hard"')
	    print('To start choose gamemode in format: "start [first_player] [second_player]"')
            answer = input('Input command: ')
            if answer == 'exit':
                return False

            try:
                option, player_1, player_2 = answer.split()
                if option != 'start' or player_1 not in game_modes or player_2 not in game_modes:
                    raise ValueError
                else:
                    self.player_1 = player_1
                    self.player_2 = player_2
                    self.current_move = self.player_1
                    return True
            except ValueError:
                print('Bad parameters!')

    # starts a game
    def game(self):
        if not self.choose_game_mode():
            return
        print(self)
        while not self.is_end():
            self.make_move()
            print(self)
            self.current_sign = 'O' if self.current_sign == 'X' else 'X'
            self.current_move = self.player_1 if self.current_move == self.player_2 else self.player_2


if __name__ == "__main__":
    TicTacToe.game(TicTacToe())
