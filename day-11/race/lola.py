

def lola(lines):
    grid = {}
    flashed = []

    def flash(coord):
        if coord not in flashed:
            x, y = coord
            flashed.append(coord)
            for xmod in [-1, 0, 1]:
                for ymod in [-1, 0, 1]:
                    c2 = (x + xmod, y + ymod)
                    if not c2 == coord:
                        if c2 in grid:
                            grid[c2] += 1
                            if grid[c2] > 9:
                                flash(c2)

    flash_count = 0
    p1 = None
    p2 = None
    for y, line in enumerate(lines):
        line = line.strip()
        for x, val in enumerate(line):
            grid[x, y] = int(val)
    for _ in range(1000):
        for coord in grid:
            grid[coord] += 1
        for coord in grid:
            if grid[coord] > 9:
                flash(coord)
        for coord in flashed:
            grid[coord] = 0
        flash_count += len(flashed)
        if len(flashed) == len(grid):
            p2 = _ + 1
            if p1 is not None:
                break
        if _ == 99:
            p1 = flash_count
            if p2 is not None:
                break
        flashed = []
    return p1, p2