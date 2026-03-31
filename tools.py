from core import Player


def coordinate_converter(board_width, board_height, offset_x=0, offset_y=0, rows=10, cols=10):
    d = {}
    cell_w = board_width / cols
    cell_h = board_height / rows

    for row in range(rows):
        y = offset_y + (rows - 1 - row) * cell_h + cell_h / 2

        squares = range(row * cols + 1, row * cols + cols + 1)
        xs = [offset_x + col * cell_w + cell_w / 2 for col in range(cols)]

        if row % 2 == 1:
            xs.reverse()

        for square, x in zip(squares, xs):
            d[square] = (int(x), int(y))

    return d


def create_players(n:int, colors, haven):
    players = []

    for i in range(1, n + 1):
        player = Player(f"{i}")
        player_color = colors.pop()
        player.color = player_color
        player.move = []
        player.path = []
        player.x, player.y = haven
        players.append(player)

    return players
