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

def main():
    with open('input.txt') as f:
        flash_count = 0
        lines = f.readlines()
        for y, line in enumerate(lines):
            line = line.strip()
            for x, val in enumerate(line):
                grid[x, y] = int(val)
        for _ in range(100):
            for coord in grid:
                grid[coord] += 1
            for coord in grid:
                if grid[coord] > 9:
                    flash(coord)
            global flashed
            for coord in flashed:
                grid[coord] = 0
            flash_count += len(flashed)
            flashed = []
        for y in range(10):
            print(''.join([str(grid[x, y]) for x in range(10)]))
        print(flash_count)
if __name__ == '__main__':
    main()
