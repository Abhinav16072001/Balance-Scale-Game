import os
import random
import getpass
import cowsay
from tabulate import tabulate


class Player:
    def __init__(self, name):
        self.points = 0
        self.name = name
        self.number = None


class Game:
    def __init__(self, n, limit):
        self.MIN_NUM = 0
        self.MAX_NUM = 100
        self.num_of_players = n
        self.limit = limit
        self.players = []

    def start(self):
        for player in range(self.num_of_players):
            name = input(f"Player {player + 1}:")
            self.players.append(Player(name))

    def calulate_score(self, numbers):
        if not numbers:  # Check if the list is empty
            return 0  # or any default value you prefer if no numbers are entered
        else:
            return (sum(numbers) / len(numbers)) * 0.8

    def display_winners(self, min_score_players):
        if self.players and min_score_players:
            winner_data = [player.name for player in min_score_players]
            if len(winner_data) == 1:
                print("Winner: ", ", ".join(winner_data))
            else:
                print("Winners: ", ", ".join(winner_data))
        else:
            print("No winners to display.")

    def start_rounds(self):
        while len(self.players) != 1:
            numbers = []
            min_score_player = []
            duplicate_numbers = []

            for player in self.players:
                while True:
                    try:
                        num = int(getpass.getpass(
                            f"Player {player.name} choose a number (0 - 100): "))
                        if 0 <= num <= 100:
                            player.number = num
                            numbers.append(num)
                            break
                        else:
                            print("choose a number 0 - 100")
                    except ValueError:
                        print("Invalid input: Please enter a valid number.")

            score = random.randint(0, 100)

            # for player in self.players:
            #     print(f"{player.name}: {player.number}", end=' ')

            print()

            # Check for duplicate numbers
            # if len(self.players) == 2:

            duplicate_numbers = [
                item for item in numbers if numbers.count(item) > 1]
            if duplicate_numbers:
                for player in self.players:
                    if player.number in duplicate_numbers:
                        player.points -= 1
                        print(
                            f"Player {player.name} had a duplicate number, points decremented.")

            if len(self.players) == 0:
                return
            print("Score: ", score)
            min_diff = 100

            for player in self.players:
                diff = abs(player.number - score)
                if min_diff > diff:
                    min_score_player = [player]
                    min_diff = diff
                elif min_diff == diff:
                    min_score_player.append(player)

            for player in self.players:
                if player in min_score_player:
                    continue
                player.points -= 1

            # Remove players with points below the limit
            for player in self.players[:]:
                if player.points <= self.limit:
                    self.players.remove(player)
                    print(f"Player {player.name} has been eliminated")

            self.display_winners(min_score_player)

            min_score_player.clear()

            if self.players:
                data = [[player.name, player.points, player.number]
                        for player in self.players]
                print(tabulate(data, headers=[
                      "Player Name", "Points", "Number Choose"], tablefmt="grid"))
            else:
                break

            for player in self.players:
                player.number = None
            numbers.clear()

        if self.players:
            print(f'Player {self.players[0].name} won')
            return self.players[0]
        else:
            print("Tie")
            return


def run():
    messages = [
        "Hello, everyone!",
        "Are you ready to play a game?",
        "Before we start, let me explain the rules to you.",
        "Firstly, each player should choose a number between 0 and 100.",
        "After that, a random number will be generated.",
        "The player whose number is closest to the generated number wins!",
        "There can be multiple winners, losers, or ties.",
        "However, if two players choose the same number, they will both receive a penalty of -1 point regardless of the game's result.",
        "Let's begin the game!"
    ]

    for message in messages:
        os.system('cls' if os.name == 'nt' else 'clear')
        cowsay.cow(message)
        input("Press Enter to continue...")

    n = int(input("Enter Number of players: "))
    l = int(input("Set Limit: "))
    game = Game(n, l)
    game.start()
    game.start_rounds()


run()
