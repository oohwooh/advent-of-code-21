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
            else:
                rise = y2 - y1
                run = x2 - x1
                idx_x = x1
                idx_y = y1
                for i in range(abs(rise) + 1):
                    if idx_x not in grid:
                        grid[idx_x] = {}
                    if idx_y not in grid[idx_x]:
                        grid[idx_x][idx_y] = 0
                    grid[idx_x][idx_y] += 1
                    if rise >= 0:
                        idx_y += 1
                    else:
                        idx_y -= 1
                    if run >= 0:
                        idx_x += 1
                    else:
                        idx_x -= 1

        for y in range(10):
            row = ''
            for x in range(10):
                if x in grid:
                    if y in grid[x]:
                        row += str(grid[x][y])
                    else:
                        row += '.'
                else:
                    row += '.'
            print(row)

        count = 0
        for row in grid:
            for col in grid[row]:
                if grid[row][col] > 1:
                    count += 1
        print(count)



if __name__ == '__main__':
    main()
