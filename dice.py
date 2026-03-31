import pygame

from settings import *


def draw_die(value, x, y, screen):
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


def draw_dice(dice1, dice2, screen):
    x_offset = DICE_SIZE + 10
    y_offset = 25
    padding = 10
    draw_die(dice1, BOARD_X+BOARD_WIDTH+padding, BOARD_Y+y_offset, screen)
    draw_die(dice2, BOARD_X+BOARD_WIDTH+padding+x_offset, BOARD_Y+y_offset, screen)
