import random
import os


class Game:
    options = ["scissors", "rock", "paper"]  # default options for a game

    def __init__(self):
        self.name = input("Enter your name: ")
        self.score = 0
        self.load_score()

    def load_score(self):
        if not os.path.exists("rating.txt"):
            return
        with open("rating.txt", 'r') as f:
            scores = f.readlines()
            for line in scores:
                name, score = line.rstrip("\n").split(" ")
                if name == self.name:
                    self.score = int(score)

    def save_score(self):
        if not os.path.exists("rating.txt"):
            scores = f"{self.name} {self.score}\n"
        else:
            with open("rating.txt", 'r') as f:
                scores = f.readlines()
                for i, line in enumerate(scores):
                    if self.name in line:
                        scores[i] = f"{self.name} {self.score}\n"
                else:
                    scores.append(f"{self.name} {self.score}\n")
        with open('rating.txt', 'w') as f:
            f.writelines(scores)

    # checks whether computer or player has won by dividing all options in 2 halves
    # (first can beat player and second can be beaten by player)
    def is_victory(self, player_move, computer_move):
        index = self.options.index(player_move)
        if index != len(self.options) - 1:  # creates new temporary list with other options to choose from
            other_options = self.options[index + 1:] + self.options[:index]
        else:
            other_options = self.options[:index]
        return other_options.index(computer_move) > (len(other_options) - 1) / 2

    # starts a fight and gives score points if win or draw
    def fight(self, players_move):
        computers_move = random.choice(self.options)
        if players_move == computers_move:
            self.score += 50
            print(f"There is a draw ({players_move})")
        elif self.is_victory(players_move, computers_move):
            self.score += 100
            print(f"Well done. The computer chose {computers_move} and failed")
        else:
            print(f"Sorry, but the computer chose {computers_move}")

    # reads from input new options for a game (ex. rock, paper, scissors, lizard, spock) or chooses default ones
    def define_rules(self):
        print("Enter game options divided by comma or nothing for default (default is: rock, paper, scissors)")
        rules = input().replace(' ', '')
        if rules != "":
            self.options = rules.split(',')

    # menu options to choose
    def start(self):
        print(f"Hello, {self.name}")
        self.define_rules()
        print("Okay, let's start. Write action (!exit, !rating or your option to play with:")
        while True:
            players_move = input()
            if players_move == "!exit":
                print("Bye!")
                break
            elif players_move == "!rating":
                print(f"Your rating: {self.score}")
            elif players_move in self.options:
                self.fight(players_move)
            else:
                print("Invalid input")
        self.save_score()


if __name__ == "__main__":
    Game().start()
