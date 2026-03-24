import time
from sys import exit
import pygame

from core import Player, SnakesAndLadders
from tools import coordinate_converter


pygame.init()


BOARD_COLS, BOARD_ROWS = 10, 10  # 100 squares
SQUARE_SIZE = 60
BOARD_WIDTH = BOARD_COLS * SQUARE_SIZE
BOARD_HEIGHT = BOARD_ROWS * SQUARE_SIZE
INFO_WIDTH = 300
WIDTH, HEIGHT = BOARD_WIDTH + INFO_WIDTH, BOARD_HEIGHT
FPS = 30
DICE_SIZE = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (200, 200, 200)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")
clock = pygame.time.Clock()

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

board_image = pygame.image.load('S.jpg')
board_image = pygame.transform.scale(board_image, (BOARD_WIDTH, BOARD_HEIGHT))

haven = (0, HEIGHT)
square_centers = coordinate_converter(BOARD_WIDTH, BOARD_HEIGHT)
square_centers[0] = haven


def move_player(player, centers, speed=5):
    """
    Move a player along a sequence of moves.
    
    move_sequence: tuple of tuples, e.g.
        (('regular', 5), ('snake', 45))
        (('regular', 5),)
    
    Rules:
    - 'regular' moves step by step square by square
    - 'snake' or 'ladder' moves directly to the target
    """

    def move_to(square):
        global movement_flag  # ✅ make sure we modify the global flag

        target_x, target_y = centers[square]
        dx = target_x - player.x
        dy = target_y - player.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist < speed:
            # Arrived at this square
            player.x, player.y = target_x, target_y
            player.prev_square = square
            player.path.pop(0)

            # If path is empty, move to next move in player.move
            if not player.path:
                if player.move:
                    player.move.pop(0)  # finished current move

                # If all moves finished, reset movement_flag
                if not player.move:
                    movement_flag = False
        else:
            # Move toward target smoothly
            player.x += speed * dx / dist
            player.y += speed * dy / dist

    if player.move:
        move_type, target_square = player.move[0]

    # 1. Build path (ONLY ONCE)
    if not player.path and player.move:
        move_type, target_square = player.move[0]

        if move_type == "regular":
            player.path = list(range(player.prev_square + 1, target_square + 1))
        elif move_type == "bounce":
            up = list(range(player.prev_square + 1, 101))
            down = list(range(99, target_square - 1, -1))
            player.path = up + down
        elif move_type in ("snake", "ladder"):
            player.path = [target_square]

    # 2. ALWAYS move if path exists
    if player.path:
        next_square = player.path[0]
        move_to(next_square)

    if not player.path and not player.move:
        movement_flag = False

    pygame.draw.circle(screen, player.color, (int(player.x), int(player.y)), SQUARE_SIZE // 3)


def update_player(player, centers, speed=5):
    if player.move:
        # print(f"Updating player {player.name} with move: {move[player.name]}")
        move_player(player, centers, speed)
    else:
        # print(f"No move for player {player.name}, keeping position.")
        pygame.draw.circle(
            screen,
            player.color, 
            centers[player.square],
            SQUARE_SIZE // 3
            )


def display_player_info(player):
    font = pygame.font.Font(None, 30)
    color = RED if player == 1 else BLUE
    y_offset = 10 
    
    pygame.draw.rect(screen, GRAY, (BOARD_WIDTH, y_offset, INFO_WIDTH, HEIGHT // 2 - 10))
    
    text = font.render(f"Player {player}", True, color)
    screen.blit(text, (BOARD_WIDTH + 10, y_offset + 10))   


def draw_die(value, x, y):
    pygame.draw.rect(screen, WHITE, (x, y, DICE_SIZE, DICE_SIZE))
    pygame.draw.rect(screen, BLACK, (x, y, DICE_SIZE, DICE_SIZE), 2)
    
    dot_radius = 5
    dot_positions = {
        1: [(0, 0)],
        2: [(-1, -1), (1, 1)],
        3: [(-1, -1), (0, 0), (1, 1)],
        4: [(-1, -1), (-1, 1), (1, -1), (1, 1)],
        5: [(-1, -1), (-1, 1), (0, 0), (1, -1), (1, 1)],
        6: [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1)]
    }
    
    for dx, dy in dot_positions[value]:
        cx = x + DICE_SIZE // 2 + dx * (DICE_SIZE // 4)
        cy = y + DICE_SIZE // 2 + dy * (DICE_SIZE // 4)
        pygame.draw.circle(screen, BLACK, (cx, cy), dot_radius)


def draw_dice(dice1, dice2):
    x_offset = BOARD_WIDTH + 10
    y_offset = 150
    
    draw_die(dice1, x_offset, y_offset)
    draw_die(dice2, x_offset + DICE_SIZE + 10, y_offset)


def exit_game():
        pygame.quit()
        exit()


def game_loop():
    players = (Player("1"), Player("2"))
    p1, p2 = players
    p1.color = RED
    p2.color = BLUE
    p1.move = []
    p2.move = []
    p1.path = []
    p2.path = []
    p1.x, p1.y = haven
    p2.x, p2.y = haven

    move = {}
    
    global movement_flag
    movement_flag = False

    game = SnakesAndLadders(players)
    die1, die2 = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not movement_flag:
                    die1, die2 = game.roll_dies()
                    raw_move = game.play(die1, die2)
                    raw_move = raw_move.split()

                    match raw_move:
                        case ["Game", "over!"]:
                            exit_game()

                        case ["Player", x, "Wins!"]:
                            # Game over
                            font = pygame.font.Font(None, 72)
                            winner = "__Winner__"
                            text = font.render(f"Player {winner} wins!", True, GREEN)
                            screen.blit(text, (BOARD_WIDTH // 2 - text.get_width() // 2,
                                                HEIGHT // 2 - text.get_height() // 2))
                            pygame.display.flip()
                            time.sleep(3)
                            exit_game()

                        case ["Player", x, "to", "square", y, *extra]:
                            extra_tuples = [
                                (extra[i], int(extra[i+1]))
                                for i in range(0, len(extra) - 1, 2)
                            ] if extra else []

                            for player in players:
                                if player.name == x:
                                    player.move = [("regular", int(y)), *extra_tuples]

                        case _:
                            raise ValueError(f"Unexpected move: {raw_move}")

                    # for player in players:
                    #     player.path = []

                    for player in players:
                        print(player)

                    movement_flag = True
        
        screen.fill(WHITE)
        screen.blit(board_image, (0, 0))

        for player in players:
            update_player(player, square_centers)

        display_player_info(game.current_player)

        if die1 and die2:
            draw_dice(die1, die2)
        
        pygame.display.flip()
        clock.tick(FPS)
        

# Run the game
game_loop()
