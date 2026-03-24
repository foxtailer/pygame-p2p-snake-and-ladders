"""
Return "Player n Wins!" where n is the winning player who has landed on square 100 
after taking all steps in their turn.

Return "Game over!" if a move is attempted after any player has won.

Otherwise, return "Player n to regular x [snake x | ladder x]", where n is the current player and x is 
the square they are currently on.
"""

import random


class Player:
    def __init__(self, name):
        self.name = name
        self.square = 0
        self.prev_square = 0

    def __repr__(self):
        return (f"Player name: {self.name}\n"
                f"Current square: {self.square}\n")


class SnakesAndLadders:
    """snakes_and_ladders = {
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
        }"""
    
    snakes_and_ladders = {
         4: 25,
         21: 39,
         29: 74,
        43: 76,
        63: 80,
        71: 89,

        30:  7,
        47: 15,
        56: 19,
        82: 42,
        98: 55,
        92: 75,
        }

    def __init__(self, players: tuple[Player]):
        self.players = players
        self.current_player = 0

    @staticmethod
    def roll_dies():
        return (random.randint(1, 6), random.randint(1, 6))

    def play(self, die1, die2):
        if any(player.square == 100 for player in self.players):
            return "Game over!"
        
        player = self.players[self.current_player]
        start_square = player.square

        new_square = player.square + die1 + die2
        
        bounce_str = ""
        portal_str = ""

        if new_square > 100:
            bounce_target = 200 - new_square
            bounce_str = f"bounce {bounce_target}"
            new_square = bounce_target

        # FIRST move normally
        player.prev_square = start_square
        player.square = new_square

        # THEN check snake/ladder
        if new_square in self.snakes_and_ladders:
            portal = self.snakes_and_ladders[new_square]
            portal_str = f"{('ladder' if portal > new_square else 'snake')} {portal}"
            player.square = portal  # final position

        result = (
            f"Player {player.name} Wins!"
            if player.square == 100
            else f"Player {player.name} to square {new_square} {bounce_str} {portal_str}"
        )

        if die1 != die2:
            self.current_player = (self.current_player + 1) % len(self.players)

        return result
    
    def begin(self):
        """
        Mock game loop.
        """
        while True:
            move = self.play(*self.roll_dies())
            move = move.split()

            match move:
                case ["Game", "over!"]:
                    # print(move)
                    break
                case ["Player", x, "Wins!"]:
                    print(f"Player {x} Wins!")
                    break
                case ["Player", x, "to", "square", y, *extra]:
                    print(move)
                case _:
                    raise ValueError(f"Unexpected move: {move}")


if __name__ == "__main__":
    players = (Player("1"), Player("2"), Player("3"))
    game = SnakesAndLadders(players)
    game.begin()
