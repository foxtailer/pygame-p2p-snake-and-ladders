def coordinate_converter(board_width, board_height, rows=10, cols=10):
    d = {}
    cell_w = board_width / cols
    cell_h = board_height / rows

    for row in range(rows):
        # row 0 is bottom row → y increases going up
        y = (rows - 1 - row) * cell_h + cell_h / 2

        squares = range(row * cols + 1, row * cols + cols + 1)
        xs = [col * cell_w + cell_w / 2 for col in range(cols)]

        # reverse every other row (snake pattern)
        if row % 2 == 1:
            xs.reverse()

        for square, x in zip(squares, xs):
            d[square] = (int(x), int(y))

    return d