"""
Return "Player n Wins!" where n is the winning player who has landed on square 100 
after taking all steps in their turn.

Return "Game over!" if a move is attempted after any player has won.

Otherwise, return "Player n is on square x", where n is the current player and x is 
the square they are currently on.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.square = 0


class SnakesAndLadders:
    snakes_and_ladders = {
         2: 38,
         7: 14,
         8: 31,
        15: 26,
        21: 42,
        28: 84,
        36: 44,
        51: 67,
        71: 91,
        78: 98,
        87: 94,

        16:  6,
        46: 25,
        49: 11,
        62: 19,
        64: 60,
        74: 53,
        89: 68,
        92: 88,
        95: 75,
        99: 80,
        }

    def __init__(self, players: tuple[Player]):
        self.players = players
        self.current_player = 0

    def roll_die(self):
        import random
        return random.randint(1, 6)
    
    def begin(self):
        while True:
            move = self.play(self.roll_die(), self.roll_die())
            move = move.split()

            match move:
                case ["Game", "over!"]:
                    # print(move)
                    break
                case ["Player", x, "Wins!"]:
                    print(f"Player {x} Wins!")
                    break
                case ["Player", x, *_, y]:
                    # print(f"Player {x} is on square {y}")
                    ...
                case _:
                    raise ValueError(f"Unexpected move: {move}")

    def play(self, die1, die2):
        if any(player.square == 100 for player in self.players):
            return "Game over!"
        
        player = self.players[self.current_player]
        new_square = player.square + die1 + die2
        print(f"Player {player.name} rolls {die1} and {die2} and moves to square {new_square}")
        
        if new_square > 100:
            new_square = 200 - new_square

        # new_square = self.snakes_and_ladders.get(new_square, new_square)
        player.square = new_square

        result = (f"Player {player.name} Wins!"
            if new_square == 100
            else f"Player {player.name} is on square {new_square}")
        
        player.square = new_square

        if die1 != die2:
            self.current_player = (self.current_player + 1) % len(self.players)

        return result
    
    def check_portal(self, square):
        if square in self.snakes_and_ladders:
            return self.snakes_and_ladders[square]
        return None

if __name__ == "__main__":
    players = (Player("1"), Player("2"), Player("3"))
    game = SnakesAndLadders(players)
    game.begin()
