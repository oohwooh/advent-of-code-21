def main():
    grid = {}
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            x1y1, x2y2 = line.split('->')
            x1, y1 = x1y1.split(',')
            x2, y2 = x2y2.split(',')
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y2 = int(y2)
            if x1 == x2:
                if x1 not in grid:
                    grid[x1] = {}
                start = min(y1, y2)
                end = max(y1, y2)
                idx = start
                while idx <= end:
                    if idx not in grid[x1]:
                        grid[x1][idx] = 0
                    grid[x1][idx] += 1
                    idx += 1
            elif y1 == y2:
                start = min(x1, x2)
                end = max(x1, x2)
                idx = start
                while idx <= end:
                    if idx not in grid:
                        grid[idx] = {}
                    if y1 not in grid[idx]:
                        grid[idx][y1] = 0
                    grid[idx][y1] += 1
                    idx += 1
        count = 0
        for row in grid:
            for col in grid[row]:
                if grid[row][col] > 1:
                    count += 1
        print(count)



if __name__ == '__main__':
    main()
