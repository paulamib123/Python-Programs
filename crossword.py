BLACK, WHITE = "#", "_"
TO_NUMBER = BLACK + WHITE + WHITE


def add_sentinels(grid: [str]) -> [str]:
    size = len(grid[0])
    sentinel_grid = [BLACK + row + BLACK for row in grid]
    sentinel_grid.append((size + 2) * BLACK)
    sentinel_grid.insert(0, (size + 2) * BLACK)
    return sentinel_grid


def clue_positions(grid: [str]) -> [(int, int)]:
    def is_clue(row, col):
        return grid[col:col+3] == TO_NUMBER or \
               grid[row-1][col] + grid[row][col] + grid[row+1][col] == TO_NUMBER

    numbered = set()
    width = len(grid[0])
    for row in range(0, width-1):
        for col in range(0, width):
            if is_clue(row, col):
                numbered.add((row, col))
    return sorted(numbered)

    # for row, line in enumerate(grid[1:]):
    #     for col, cell in enumerate(line):
    #         if line[col:col+3] == TO_NUMBER:
    #             numbered.add((row, col))
    #         elif grid[row-1][col] + grid[row][col] + grid[row+1][col] == TO_NUMBER:
    #             numbered.add((row, col))
    # return sorted(numbered)


input_grid = [line.strip() for line in open('grid.txt')]
new_grid = add_sentinels(input_grid)
clues = clue_positions(new_grid)
print(clues)
print(len(clues))
