import random
from enum import Enum


class RockPaperScissors:

    def __init__(self):
        self.rules = {
            "Rock": ["Scissors", "Lizard"],
            "Paper": ["Rock", "Spock"],
            "Scissors": ["Paper", "Lizard"],
            "Spock": ["Rock", "Scissors"],
            "Lizard": ["Paper", "Spock"],
        }
        self.win = 0
        self.draw = 0
        self.loss = 0

    def ask_to_continue(self):
        print("Press Q to quit and anything else for another round")
        wants_to_continue = input(">>>")
        wants_to_continue = wants_to_continue.upper()
        return wants_to_continue != 'Q'

    def print_headers(self):
        print("Welcome to the Rock, Paper, Scissors, Lizard, Spock!")

    def convert_to_move(self, move):
        if move == 1:
            return 'Rock'
        elif move == 2:
            return 'Paper'
        elif move == 3:
            return 'Scissors'
        elif move == 4:
            return 'Spock'
        elif move == 5:
            return 'Lizard'
        else:
            raise ValueError()

    def find_winner(self, move, opponent_move):
        print("You played " + move + ". Opponent played " + opponent_move)
        if move in self.rules.get(opponent_move):
            self.loss += 1
            print(opponent_move + " beats " + move + "! You lost.")
        elif opponent_move in self.rules.get(move):
            self.win += 1
            print(move + " beats " + opponent_move + "! You won.")
        else:
            self.draw += 1
            print("It is a draw.")

    def game_loop(self):
        print("1- Rock   2- Paper   3- Scissors   4- Spock   5- Lizard")
        player_move = input(">>>")
        player_move = int(player_move)
        player_move = self.convert_to_move(player_move)
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        self.find_winner(player_move, computer_choice)
        print(str(self.win) + " wins. " + str(self.loss) + " losses." + str(self.draw) + " draws.")


    def start_game(self):
        self.print_headers()
        game_is_active = True
        while game_is_active:
            try:
                self.game_loop()
                game_is_active = self.ask_to_continue()
            except ValueError as err:
                print("Incorrect input, please enter a number 1 - 5.")
        print("Good Bye")


if __name__ == "__main__":
    newGame = RockPaperScissors()
    newGame.start_game()
