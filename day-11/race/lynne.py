neighbors = lambda x, y: (
    (x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
    (x - 1, y), (x + 1, y),
    (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)
)


def ripple(grid, x, y):
    if grid[x, y][0] > 9 and not grid[x, y][1]:
        grid[x, y][1] = True

        for neighbor in neighbors(x, y):
            if neighbor in grid:
                grid[neighbor][0] += 1
                ripple(grid, *neighbor)


def lynne(lines):
    output_tuple = [0, None]
    rows = len(lines)
    cols = len(lines[0])
    grid = {(x, y): [int(lines[y][x]), False] for x in range(cols) for y in range(rows)}

    flashes = 0

    for i in range(1000):
        for (x, y) in grid:
            grid[x, y][1] = False
            grid[x, y][0] += 1
        for (x, y) in grid:
            ripple(grid, x, y)
        for (x, y) in grid:
            if grid[x, y][0] > 9:
                grid[x, y][0] = 0
        num_flashes = len([1 for key in grid if grid[key][0] == 0])
        flashes += num_flashes
        if i == 99:
            output_tuple[0] = flashes
        if num_flashes == rows * cols:
            output_tuple[1] = i + 1
            break

    return tuple(output_tuple)