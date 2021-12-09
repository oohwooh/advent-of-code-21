def main():
    total = 0
    map = {}
    low_points = []
    with open('input.txt') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            line = line.strip()
            for x, val in enumerate(line):
                map.setdefault(x, {})
                map[x][y] = val
    for x in map:
        for y in map[x]:
            left = map.get(x-1, {}).get(y, None)
            right = map.get(x + 1, {}).get(y, None)
            down = map[x].get(y + 1, None)
            up = map[x].get(y - 1, None)
            if all(map[x][y] < test for test in [left, right, down, up] if test != None):
                low_points.append((x, y))
                total += int(map[x][y]) + 1
    basins = []
    for point in low_points:
        basin = {(point[0], point[1])}
        for i in range(400):
            basin_copy = basin.copy()
            for x, y in basin_copy:
                left = map.get(x - 1, {}).get(y, None)
                if left is not None and int(left) < 9:
                    basin.add((x - 1, y))
                right = map.get(x + 1, {}).get(y, None)
                if right is not None and int(right) < 9:
                    basin.add((x + 1, y))
                down = map[x].get(y + 1, None)
                if down is not None and int(down) < 9:
                    basin.add((x, y + 1))
                up = map[x].get(y - 1, None)
                if up is not None and int(up) < 9:
                    basin.add((x, y - 1))
        basins.append(basin)
    largest_basins = sorted([len(basin) for basin in basins], reverse=True)
    print(largest_basins[0] * largest_basins[1] * largest_basins[2])
    print(largest_basins)


if __name__ == '__main__':
    main()
