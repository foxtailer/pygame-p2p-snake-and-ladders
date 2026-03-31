#settings.py
import pygame

from tools import coordinate_converter


pygame.init()
info = pygame.display.Info()

SCREEN_WIDTH =  info.current_w
SCREEN_HEIGHT = info.current_h

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (180, 180, 180)
BLUE = (100, 149, 237)
LIGHT_BLUE = (173, 216, 230)
GREEN = (50, 205, 50)
RED = (220, 20, 60)
BROWN = (139, 69, 19)

PLAYER_COLORS = [
    (255, 0, 0),     # red
    (0, 200, 0),     # green
    (0, 0, 255),     # blue
    (255, 255, 0),   # yellow
    (255, 165, 0),   # orange
    (128, 0, 128),   # purple
    (0, 255, 255),   # cyan
    (255, 0, 255),   # magenta
    (255, 105, 180), # pink
    (50, 205, 50),   # lime
    (0, 128, 128),   # teal
    (255, 215, 0),   # gold
]


BOARD_COLS, BOARD_ROWS = 10, 10  # 100 squares
SQUARE_SIZE = 60
BOARD_WIDTH = BOARD_COLS * SQUARE_SIZE
BOARD_HEIGHT = BOARD_ROWS * SQUARE_SIZE
BOARD_X = (SCREEN_WIDTH - BOARD_WIDTH)/2
BOARD_Y = (SCREEN_HEIGHT - BOARD_HEIGHT)/2
FPS = 30
DICE_SIZE = 60
PLAYER_SPEED = 5
HAVEN = BOARD_X - 30, BOARD_Y + BOARD_HEIGHT - 30

square_centers = coordinate_converter(
            BOARD_WIDTH,
            BOARD_HEIGHT,
            BOARD_X,
            BOARD_Y
)
square_centers[0] = HAVEN