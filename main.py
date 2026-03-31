import os
import sys

import pygame

from menu import show_menu
from settings import SCREEN_HEIGHT, SCREEN_WIDTH
from game import game_loop


os.chdir(os.path.dirname(os.path.abspath(__file__)))


running = True
screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT), 
    pygame.FULLSCREEN
)


while running:
    menu_choice = show_menu(screen)

    if menu_choice["command"]  == "quit":
        running = False
        pygame.quit()
        sys.exit()
    elif menu_choice["command"] == "play":
        game_loop(menu_choice["players"], screen)
