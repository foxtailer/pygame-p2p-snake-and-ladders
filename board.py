import pygame

from settings import *


def move_player(player, speed, screen):

    def move_to(square):
        target_x, target_y = square_centers[square]
        dx = target_x - player.x
        dy = target_y - player.y
        dist = (dx**2 + dy**2) ** 0.5

        if dist < speed:
            # Arrived at this square
            player.x, player.y = target_x, target_y
            player.prev_square = square
            player.path.pop(0)
            # print(player.path)

            # If path is empty, move to next move in player.move
            if not player.path:
                if player.move:
                    player.move.pop(0)  # finished current move
                    # print(player.move)
        else:
            # Move toward target smoothly
            player.x += speed * dx / dist
            player.y += speed * dy / dist

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

    pygame.draw.circle(
        screen,
        player.color,
        (int(player.x), 
        int(player.y)),
        SQUARE_SIZE // 3
    )


def update_player(player, speed, screen):
    if player.move:
        # print(f"Updating player {player.name} with move: {move[player.name]}")
        move_player(player, speed, screen)
    else:
        # print(f"No move for player {player.name}, keeping position.")
        pygame.draw.circle(
            screen,
            player.color, 
            square_centers[player.square],
            SQUARE_SIZE // 3
            )


def display_player_info(player, screen):
    font = pygame.font.Font(None, 30)
    text = font.render(f"Player {player.name} turn:", True, player.color)
    screen.blit(
        text,
        (BOARD_X + BOARD_WIDTH + 10, BOARD_Y))   


def draw_board(screen):
        board_image = pygame.image.load('assets/S.jpg')
        board_image = pygame.transform.scale(
            board_image,
            (BOARD_WIDTH, BOARD_HEIGHT)
        )

        screen.blit(
            board_image, 
            (BOARD_X, BOARD_Y)
        )

        pygame.draw.rect(
            screen,
            GRAY,
            (BOARD_X+BOARD_WIDTH, BOARD_Y, 200, BOARD_HEIGHT)
        )