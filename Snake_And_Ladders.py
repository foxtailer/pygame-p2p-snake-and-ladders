import time
from sys import exit
import pygame

from core import Player, SnakesAndLadders


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


board_image = pygame.image.load('S.jpg')
board_image = pygame.transform.scale(board_image, (BOARD_WIDTH, BOARD_HEIGHT))


def draw_players(pos1, pos2):
    for pos, color in [(pos1, RED), (pos2, BLUE)]:
        x = (pos - 1) % BOARD_COLS
        y = BOARD_ROWS - 1 - (pos - 1) // BOARD_COLS
        pygame.draw.circle(screen, color, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 3)


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
    p1, p2 = Player("1"), Player("2")
    game = SnakesAndLadders((p1, p2))
    die1, die2 = 0, 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    die1, die2 = game.roll_dies()
                    move = game.play(die1, die2)
                    move = move.split()
        
        screen.fill(WHITE)
        screen.blit(board_image, (0, 0))

        draw_players(p1.square, p2.square)
        display_player_info(game.current_player)
        if die1 and die2:
            draw_dice(die1, die2)
        
        pygame.display.flip()
        clock.tick(FPS)
        

# Run the game
game_loop()
