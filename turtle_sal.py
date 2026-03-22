import time
from turtle import *

from tmp import Player, SnakesAndLadders


hideturtle()
penup()
speed(50)
screensize(600,600)
goto(0,275)

"""----------------------Co-ordinate Converter-------------------------------"""
def coordinate_converter():
    """
    giving each square x, y position.
    d = {
        1:  [-225, -275],
        2:  [-175, -275],
        ...}
    """
    d = {}
    for row in range(10):
        y = -275 + row * 50
        squares = range(row * 10 + 1, row * 10 + 11)
        xs = range(-225, 226, 50)
        if row % 2 != 0:          # even rows go right→left
            xs = reversed(xs)
        for square, x in zip(squares, xs):
            d[square] = [x, y]
    return d

d = coordinate_converter()
"""--------------------------------------------------------------------------"""

"""----------------Filling the Boards(Numbering & Colouring)-----------------"""

def board(a, b, color="", text="", size=50):
    width(3)
    penup()
    
    # shift from center → top-left
    goto(a - size/2, b + size/2)
    
    pendown()
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(size)
        rt(90)
    end_fill()
    
    penup()
    goto(a, b + 10)
    write(text, align="center", font=("Arial", 8, "bold"))

colors = [
    "dark slate gray",
    "yellow",
    "Lime Green",
    "pink",
    "orange",
    "lightsalmon",
    "firebrick",
    "purple",
    "dark khaki",

    "red",
    "blue",
    "green",
    "cyan",
    "magenta",
    "gold",
    "navy",
    "brown",
    "teal",
    "coral",
    "orchid",
    "plum"
]

for square in range(1, 101):
    if square in SnakesAndLadders.snakes_and_ladders:
        head = square
        tail = SnakesAndLadders.snakes_and_ladders[head]
        color = colors.pop(0)
    else:
        head = tail = '_'

    if head > tail:
        board(*d[head], color=color, text="Snake")
        board(*d[tail], color=color, text="|:(|")
    elif head < tail:
        board(*d[head], color=color, text="Ladder")
        board(*d[tail], color=color, text="|:)|")
    else:
        board(*d[square])

for square in d:
    penup()
    x, y = d[square]
    goto(x, y)
    write(square)    
"""--------------------------------------------------------------------------"""

#-------------------------------------------------------------------------------
def dice_roll_display(posx, posy):
    board(posx, posy, color="white", size=120)
    penup()
    goto(posx+5, posy-20)
    write("Player 1:",   font=("arial",12))
    goto(posx+5, posy-60)
    write("Computer 1:", font=("arial",12))
    goto(posx+5, posy-100)
    write("Computer 2:", font=("arial",12))

def snakeladder_display(posx, posy):
    board(posx, posy, color="white", size=155)

def information(posx, posy, word, size):
    goto(posx, posy)
    write(word, font=("Times New Roman", size, "bold"))

#Defining Pawns-----------------------------------------------------------------
pencolor("black")
speed(0)
initial = Turtle()

pc0 = initial.clone()
pc0.penup()
pc0.fillcolor("red")
pc0.shape("circle")
pc0.goto(-260, -257)
pc0.speed(1)

pc1 = initial.clone()
pc1.penup()
pc1.fillcolor("blue")
pc1.shape("circle")
pc1.goto(-260, -275)
pc1.speed(1)

pc2 = initial.clone()
pc2.penup()
pc2.fillcolor("green")
pc2.shape("circle")
pc2.goto(-260, -293)
pc2.speed(1)

initial.ht()
#-------------------------------------------------------------------------------


#The Game-----------------------------------------------------------------------
player1, player2, player3 = Player("1"), Player("2"), Player("3")
player1.pawn, player2.pawn, player3.pawn = pc0, pc1, pc2
players = (player1, player2, player3)
game = SnakesAndLadders(players)


while True:
    command = input("Enter 'r' to roll the dice: ")

    if command.lower() != 'r':
        print("Invalid command. Please enter 'r' to roll the dice.")
        continue

    move = game.play(game.roll_die(), game.roll_die())
    move = move.split()

    match move:
        case ["Game", "over!"]:
            print(move)
            time.sleep(10)
            break
        case ["Player", x, "Wins!"]:
            print(f"Player {x} Wins!")
            break
        case ["Player", x, *_, y]:
            players[int(x)-1].pawn.goto(*d[int(y)])
            portal = game.check_portal(int(y))

            if portal is not None:
                players[int(x)-1].pawn.goto(*d[portal])
        case _:
            raise ValueError(f"Unexpected move: {move}")
