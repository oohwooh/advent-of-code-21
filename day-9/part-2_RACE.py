from timeit import timeit
import asyncio


async def lola():
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
                # total += int(map[x][y]) + 1
    async def check_basin(point):
        basin = {(point[0], point[1])}
        for i in range(9):
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
            if basin_copy == basin:
                return basin
        return basin

    tasks = []
    for point in low_points:
        tasks.append(asyncio.create_task(check_basin(point)))
    await asyncio.wait(tasks)
    basins = [task.result() for task in tasks]
    largest_basins = sorted([len(basin) for basin in basins], reverse=True)
    # print(largest_basins[0] * largest_basins[1] * largest_basins[2])

    # print(largest_basins)

from time import perf_counter

async def lynne():
    def increasing_neighbors(grid, rows, columns, x, y, existing):
        neighbors = []
        if x > 0 and (x - 1, y) not in existing and grid[x - 1, y] != 9:
            neighbors.append((x - 1, y))
        if y > 0 and (x, y - 1) not in existing and grid[x, y - 1] != 9:
            neighbors.append((x, y - 1))
        if x < columns - 1 and (x + 1, y) not in existing and grid[x + 1, y] != 9:
            neighbors.append((x + 1, y))
        if y < rows - 1 and (x, y + 1) not in existing and grid[x, y + 1] != 9:
            neighbors.append((x, y + 1))

        return neighbors


    with open("input.txt") as inp:
        lines = list(map(lambda x: x.strip(), inp.readlines()))
        rows = len(lines)
        columns = len(lines[0])
        grid = {(x, y): int(lines[y][x]) for x in range(columns) for y in range(rows)}
        low_points = set()
        for (x, y) in grid:
            if all([
                x == 0 or grid[x, y] < grid[x - 1, y],
                y == 0 or grid[x, y] < grid[x, y - 1],
                x == columns - 1 or grid[x, y] < grid[x + 1, y],
                y == rows - 1 or grid[x, y] < grid[x, y + 1]
            ]):
                low_points.add((x, y))
        # print("Part 1:", sum(grid[point] + 1 for point in low_points))

        basins = {point: {point} for point in low_points}
        async def check_basin(basin, basins):
            x, y = basin
            neighbors = increasing_neighbors(grid, rows, columns, x, y, basins[x, y])
            while len(neighbors) > 0:
                new_neighbors = []
                [new_neighbors.extend(increasing_neighbors(grid, rows, columns, j, k, basins[x, y])) for (j, k) in
                 neighbors]
                neighbors = new_neighbors
                [basins[x, y].add(n) for n in neighbors]
        for basin in basins:
            await check_basin(basin, basins)

        ttb = sorted([len(basins[point]) for point in basins], reverse=True)
        # print("Part 2:", ttb[0] * ttb[1] * ttb[2])


import matplotlib.pyplot as plt
import matplotx

if __name__ == '__main__':
    fig, ax = plt.subplots()
    loop_count = 500
    lynne_times = [0]
    lola_times = [0]
    loops = range(loop_count)
    for _ in loops:
        lynne_start = perf_counter()
        asyncio.run(lynne())
        lynne_time = perf_counter() - lynne_start
        lynne_times.append(lynne_time + lynne_times[-1])

    # print(f'Lynne: {lynne_time} ({lynne_time/loops}/it)')
    for _ in loops:
        lola_start = perf_counter()
        asyncio.run(lola())
        lola_time = perf_counter() - lola_start
        lola_times.append(lola_time + lola_times[-1])
    lola_times.pop(0)
    lynne_times.pop(0)

    diffs = [abs(lola_times[i] - lynne_times[i]) for i in loops]

    ax.plot(loops, lola_times, label='Lola')
    ax.plot(loops, lynne_times, label='Lynne')
    ax.plot(loops, diffs, label='Diff')
    ax.set_xlabel('Iterations')
    ax.set_ylabel('Cumulative execution time')
    matplotx.line_labels()
    plt.show()
    # print(f'Lola: {lola_time} ({lola_time/loops}/it)')

    # if lola_time > lynne_time:
    #     print('Winner: Lynne')
    # else:
    #     print('Winner: Lola')
    # print(f'Diff: {abs(lola_time - lynne_time)} ({abs(lola_time - lynne_time)/loops}/it)')