from tqdm import tqdm
from time import perf_counter
import asyncio

async def main():
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
        return basin

    tasks = []
    for point in low_points:
        tasks.append(asyncio.create_task(check_basin(point)))
    await asyncio.wait(tasks)
    basins = [task.result() for task in tasks]
    largest_basins = sorted([len(basin) for basin in basins], reverse=True)
    print(largest_basins[0] * largest_basins[1] * largest_basins[2])
    print(largest_basins)


if __name__ == '__main__':
    start = perf_counter()
    asyncio.run(main())
    print(perf_counter() - start)
