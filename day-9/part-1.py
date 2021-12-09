def main():
    total = 0
    map = {}
    with open('input.txt') as f:
        lines = f.readlines()
        for y, line in enumerate(lines):
            line = line.strip()
            for x, val in enumerate(line):
                map.setdefault(x, {})
                map[x][y] = val
    print(map)
    for x in map:
        for y in map[x]:
            left = map.get(x-1, {}).get(y, None)
            right = map.get(x + 1, {}).get(y, None)
            down = map[x].get(y + 1, None)
            up = map[x].get(y - 1, None)
            if all(map[x][y] < test for test in [left, right, down, up] if test != None):
                print('low point', map[x][y])
                total += int(map[x][y]) + 1
    print(total)

if __name__ == '__main__':
    main()
