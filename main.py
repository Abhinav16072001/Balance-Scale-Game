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
            name = input(f"Player {player}:")
            self.players.append(Player(name))

    def calulate_score(self, numbers):
        score = (sum(numbers)/len(numbers))*0.8
        return score
    
        
    def start_rounds(self):
        numbers = []
        min_score_player = self.players[0]
        while len(self.players) != 1:

            for player in self.players:
                num = int(input(f"Player {player.name} choose a number (0 - 100): "))
                player.number = num
                numbers.append(num)


            score =  self.calulate_score(numbers)
            print("Score: ", score)
            min_diff = 100
            for player in self.players:
                diff  = abs(player.number - score)
                if min_diff > diff:
                    min_score_player = player
                    min_diff = diff
            
            for player in self.players:
                player.number = None
                if player is min_score_player:
                    continue
                player.points -= 1
                if player.points <= self.limit:
                    self.players.remove(player)
                    print(f'Player {player.name} has been eliminated')
            
            print([f'{i.name}: {i.points}' for i in self.players])

        print(f'Player {self.players[0].name} won')
        return self.players[0]


    
game = Game(3, -2)
game.start()
game.start_rounds()