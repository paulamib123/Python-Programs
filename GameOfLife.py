def neighbors(cell):
    x, y = cell
    yield x - 1, y - 1
    yield x, y - 1
    yield x + 1, y - 1
    yield x - 1, y
    yield x + 1, y
    yield x - 1, y + 1
    yield x, y + 1
    yield x + 1, y + 1


def game(live_cells):
    new_board = set()
    candidates = set(n for cell in live_cells for n in neighbors(cell)) | set(live_cells)

    for cell in candidates:
        count = sum([int(n in live_cells) for n in neighbors(cell)])
        if count == 3 or ((count == 2 or count == 3) and cell in live_cells):
            new_board.add(cell)
    return new_board


if __name__ == "__main__":
    live_cells = {(4, 6), (5, 6), (6, 6)}
    #live_cells = {(5, 6), (6, 6), (5, 7), (6, 7)}
    #live_cells = {(5, 6), (5, 7), (5, 8), (5, 9)}
    generations = 10
    for _ in range(generations):
        live_cells = game(live_cells)
        print(live_cells)
