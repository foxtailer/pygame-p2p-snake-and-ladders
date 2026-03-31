import time

import pygame

from core import SnakesAndLadders
from dice import draw_dice
from settings import *
from board import draw_board, display_player_info, update_player
from menu import show_ingame_menu


clock = pygame.time.Clock()


def game_loop(players, screen):
    move = {}  # Fake move before first roll.
    die1, die2 = 0, 0
    game = SnakesAndLadders(players)

    bg = pygame.image.load("assets/game_background.jpg")
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = show_ingame_menu(screen)

                if event.key == pygame.K_SPACE and not any(player.move for player in players):
                    die1, die2 = game.roll_dies()
                    raw_move = game.play(die1, die2)
                    raw_move = raw_move.split()

                    match raw_move:
                        case ["Player", x, "Wins!"]:
                            # Game over
                            font = pygame.font.Font(None, 72)
                            winner = next(p for p in players if p.name == x)
                            text = font.render(f"Player {winner.name} wins!", True, GREEN)
                            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2,
                                                SCREEN_HEIGHT // 2 - text.get_height() // 2))
                            pygame.display.flip()
                            time.sleep(5)
                            break

                        case ["Player", x, "to", "square", y, *extra]:
                            extra_tuples = [
                                (extra[i], int(extra[i+1]))
                                for i in range(0, len(extra) - 1, 2)
                            ] if extra else []

                            for player in players:
                                if player.name == x:
                                    player.move = [("regular", int(y)), *extra_tuples]
                                    # print(player.move, player)

                        case _:
                            raise ValueError(f"Unexpected move: {raw_move}")

        screen.blit(bg, (0, 0))
        draw_board(screen)

        for player in players:
            update_player(player, PLAYER_SPEED, screen)

            if player.move:
                draw_dice(die1, die2, screen)

        if not any(player.move for player in players):
            display_player_info(players[game.current_player], screen)

        pygame.display.flip()
        clock.tick(FPS)
