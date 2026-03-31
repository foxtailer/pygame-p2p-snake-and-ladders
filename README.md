# pygame-p2p-snake-and-ladders

## Game rules

1. Players start off the board on square 0.
2. Players take turns rolling two six-sided dice.
3. Move forward according to the sum of the dice, following squares 1 to 100.
4. If the dice show the same value (a double), the player will have another turn after completing the current move.
5. If a player lands exactly on the bottom of a ladder, they must move immediately to the top of the ladder, even if the roll was a double.
6. If a player lands exactly on the head of a snake, they must slide immediately to the bottom of the snake, even if the roll was a double.
7. A player must land exactly on square 100 to win. If the roll exceeds the last square, the piece “bounces” backward the extra number of steps. *For example, if you are on square 98 and roll a five, move your piece to 100 (two steps), then "bounce" back to 99, 98, and 97 (three, four, then five steps).*
8. If a player rolls a double and reaches square 100 exactly, the player wins and does not take an extra turn.

## TODO: Online mod

Use hole punching to create a UDP connection. It should work in ~82% of cases.

## Run
- pip install pygame
- navigate to project directory
- python main.py 

## Based on
- https://github.com/ImFizzyyy/Snakes-and-ladders.git
- ...