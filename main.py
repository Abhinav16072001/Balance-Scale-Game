import getpass


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
                        player.number = num
                        numbers.append(num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

            score = self.calulate_score(numbers)

            for player in self.players:
                print(f"{player.name}: {player.number}", end=' ')

            print()

            # Check for duplicate numbers
            if len(self.players) == 2:

                duplicate_numbers = [item for item in numbers if numbers.count(item) > 1]
                if duplicate_numbers:
                    for player in self.players:
                        if player.number in duplicate_numbers:
                            player.points -= 1
                            print(f"Player {player.name} had a duplicate number, points decremented.") 

            numbers.clear()
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
                player.number = None
                if player in min_score_player:
                    continue
                player.points -= 1

            # Remove players with points below the limit
            for player in self.players[:]:
                if player.points <= self.limit:
                    self.players.remove(player)
                    print(f"Player {player.name} has been eliminated")

            min_score_player.clear()
            
            if self.players:
                print([f'{i.name}: {i.points}' for i in self.players])
            else:
                break

        if self.players:
            print(f'Player {self.players[0].name} won')
            return self.players[0]
        else:
            print("Tie")
            return 


def run():
    n = int(input("Enter Number of players: "))
    l = int(input("Set Limit: "))
    game = Game(n, l)
    game.start()
    game.start_rounds()

run()
