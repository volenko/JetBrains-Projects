import random


# creates a new set of dominos
def create_set():
    set_ = list()
    for i in range(7):
        for j in range(i, 7):
            set_.append([i, j])
    return set_


# shuffles pieces and split them between player, computer and deck
def shuffle():
    domino_set = create_set()
    random.shuffle(domino_set)
    return domino_set[0:7], domino_set[7:14], domino_set[14:]


# chooses first piece to play from player or computer
def beginning(computer_pieces, player_pieces):
    for double in range(6, -1, -1):
        if [double, double] in computer_pieces or [double, double] in player_pieces:
            return [double, double]


# updates all data on the screen
def refresh_screen(stock_pieces, player_pieces, computer_pieces, domino_snake):
    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()
    if len(domino_snake) > 6:  # doesn't show more than 6 pieces on the screen
        print(str(domino_snake[0]) + str(domino_snake[1]) + str(domino_snake[2]) + "..." + str(domino_snake[-3]) + str(domino_snake[-2]) + str(domino_snake[-1]))
    else:
        msg = ""
        for domino in domino_snake:
            msg += str(domino)
        print(msg)
    print()
    print("Your pieces:")
    for i, domino in enumerate(player_pieces):
        print(f"{i + 1}:{domino}")
    print()


# moves dominos between deck, hands and table
def move_domino(from_set, to_set, pos=0):
    if not from_set:
        return from_set, to_set
    if pos == 0:  # if pos == 0 it grabs one domino from the deck
        domino = random.choice(from_set)
    else:
        domino = from_set[abs(pos) - 1]
    from_set.remove(domino)
    if not to_set:
        to_set.insert(1, domino)
        return from_set, to_set
    if pos > 0:
        if to_set[len(to_set) - 1][1] == domino[0]:
            to_set.append(domino)
        else:
            to_set.append(domino[::-1])
    else:
        if to_set[0][0] == domino[1]:
            to_set.insert(0, domino)
        else:
            to_set.insert(0, domino[::-1])
    return from_set, to_set


# checks whether move is valid
def check_move(move, status, player_pieces, computer_pieces, domino_snake):
    if move == 0:
        return True
    if status == "player":
        set_ = player_pieces
    else:
        set_ = computer_pieces
    domino = set_[abs(move) - 1]
    start = domino_snake[0][0]
    end = domino_snake[-1][1]
    if move < 0 and (start == domino[0] or start == domino[1]):
        return True
    if move > 0 and (end == domino[0] or end == domino[1]):
        return True
    return False


# gets move from user input and its validity
def get_move(player_pieces, computer_pieces, domino_snake, status):
    while True:
        move = input()
        try:
            move = int(move)
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if not -len(player_pieces) <= move <= len(player_pieces):
            print("Invalid input. Please try again.")
            continue
        if check_move(move, status, player_pieces, computer_pieces, domino_snake):
            return move
        else:
            print("Illegal move. Please try again.")
            print("Positive number to put at the end and negative to put at the beginning of the snake.")
            print("Zero to draw one from the deck or skip your move.")


# checks whether it is the end of the game (by victory or by draw)
def is_end(player_pieces, computer_pieces, domino_snake, status):
    if not computer_pieces or not player_pieces:
        print(f"Status: The game is over. {'You' if status == 'player' else 'The computer'} won!")
        return True
    start = domino_snake[0][0]
    start_c = 0
    end = domino_snake[-1][1]
    end_c = 0
    for domino in domino_snake:
        start_c += domino.count(start)
        end_c += domino.count(end)
    if start_c == 8 and end_c == 8:  # means there are no possible moves
        print("Status: The game is over. It's a draw!")
        return True


# calculates computers move by getting the biggest score
# each domino receives a score equal to the sum of appearances of each of its numbers on the table and computer's hands
# then tries to pull piece with the highest score, if it is not possible then pulls one from the deck or skips move
def calculate_move(player_pieces, computer_pieces, domino_snake, status):
    set_ = computer_pieces + domino_snake
    counter = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0}
    moves = dict()
    for domino in set_:
        counter[str(domino[0])] += 1
        counter[str(domino[1])] += 1
    for i, domino in enumerate(computer_pieces):
        moves[str(i + 1)] = domino[0] + domino[1]
    for _ in range(len(moves)):
        move = int(max(moves, key=moves.get))
        if check_move(move, status, player_pieces, computer_pieces, domino_snake):
            return move
        else:
            moves.pop(str(move))
    return 0


# main part for changing moves and connecting all together
def start_game():
    domino_snake = list()
    while True:
        computer_pieces, player_pieces, stock_pieces = shuffle()
        highest_domino = beginning(computer_pieces, player_pieces)
        if highest_domino in player_pieces:
            status = "player"
            player_pieces, domino_snake = move_domino(player_pieces, domino_snake, player_pieces.index(highest_domino) + 1)
            break
        else:
            status = "computer"
            computer_pieces, domino_snake = move_domino(computer_pieces, domino_snake, computer_pieces.index(highest_domino) + 1)
            break
    while True:
        refresh_screen(stock_pieces, player_pieces, computer_pieces, domino_snake)
        if is_end(player_pieces, computer_pieces, domino_snake, status):
            break
        status = "computer" if status == "player" else "player"
        print("Status: {0}".format("It's your turn to make a move. Enter your command." if status == "player" else "Computer is about to make a move. Press Enter to continue..."))
        if status == "computer":
            input()
            move = calculate_move(player_pieces, computer_pieces, domino_snake, status)
            if move == 0:
                stock_pieces, computer_pieces = move_domino(stock_pieces, computer_pieces, move)
            else:
                computer_pieces, domino_snake = move_domino(computer_pieces, domino_snake, move)
        else:
            move = get_move(player_pieces, computer_pieces, domino_snake, status)
            if move == 0:
                stock_pieces, player_pieces = move_domino(stock_pieces, player_pieces, move)
            else:
                player_pieces, domino_snake = move_domino(player_pieces, domino_snake, move)


if __name__ == "__main__":
    start_game()
