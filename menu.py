import pygame

from settings import *
from button import Button
from tools import create_players


def show_menu(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)

    # --- STATE ---
    players_count = 2
    modes = ["Online", "1PC"]
    mode_index = 0

    # --- BACKGROUND ---
    bg = pygame.image.load("assets/game_background.jpg")
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2

    # --- BUTTONS ---
    # Players arrows
    p_left  = Button(cx + 30,  cy - 20, 40, 40, "<", font, text_color=WHITE)
    p_right = Button(cx + 190, cy - 20, 40, 40, ">", font, text_color=WHITE)

    # Mode arrows
    m_left  = Button(cx + 30,  cy + 60, 40, 40, "<", font, text_color=WHITE)
    m_right = Button(cx + 190, cy + 60, 40, 40, ">", font, text_color=WHITE)

    # Bottom buttons
    play_btn = Button(cx - 100, cy + 160, 200, 50, "Play", font,
                      bg_color=(0, 150, 0), text_color=WHITE)
    quit_btn = Button(cx - 100, cy + 230, 200, 50, "Quit", font,
                      bg_color=(220, 20, 60), text_color=WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if p_left.is_clicked(event):
                    players_count = max(2, players_count - 1)

                elif p_right.is_clicked(event):
                    players_count = min(6, players_count + 1)

                elif m_left.is_clicked(event):
                    mode_index = (mode_index - 1) % len(modes)

                elif m_right.is_clicked(event):
                    mode_index = (mode_index + 1) % len(modes)

                elif play_btn.is_clicked(event):
                    players = create_players(players_count, PLAYER_COLORS, HAVEN)
                    return {
                        "mode": modes[mode_index],
                        "players": players,
                        "command": "play"
                    }

                elif quit_btn.is_clicked(event):
                    return {"command": "quit"}

        # --- DRAW ---
        screen.blit(bg, (0, 0))

        # Title
        title = font.render("Game Menu", True, WHITE)
        screen.blit(title, title.get_rect(center=(cx, cy - 120)))

        # --- PLAYERS ROW ---
        label_players = font.render("Players", True, WHITE)
        screen.blit(label_players, (cx - 200, cy - 10))

        value_players = font.render(str(players_count), True, WHITE)
        screen.blit(value_players, value_players.get_rect(center=(cx + 120, cy)))

        # --- MODE ROW ---
        label_mode = font.render("Mode", True, WHITE)
        screen.blit(label_mode, (cx - 200, cy + 70))

        value_mode = font.render(modes[mode_index], True, WHITE)
        screen.blit(value_mode, value_mode.get_rect(center=(cx + 120, cy + 80)))

        # --- DRAW BUTTONS ---
        p_left.draw(screen)
        p_right.draw(screen)

        m_left.draw(screen)
        m_right.draw(screen)

        play_btn.draw(screen)
        quit_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)


def show_ingame_menu(screen):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 40)

    # --- BACKGROUND ---
    bg = pygame.image.load("assets/game_background.jpg")
    bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    cx = SCREEN_WIDTH // 2
    cy = SCREEN_HEIGHT // 2

    quit_btn = Button(cx - 100, cy, 200, 50, "Quit", font,
                      bg_color=(220, 20, 60), text_color=WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if quit_btn.is_clicked(event):
                    return False

        # --- DRAW ---
        screen.blit(bg, (0, 0))

        # --- DRAW BUTTONS ---
        quit_btn.draw(screen)

        pygame.display.flip()
        clock.tick(60)