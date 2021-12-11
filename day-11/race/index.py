# from race import race
from lola import lola
from lynne import lynne
from tqdm import tqdm
from time import perf_counter
from random import randint, choice
from typing import List
from matplotlib import pyplot as plt
import matplotx

fig, ax = plt.subplots()

def random_grid(n: int) -> List[str]:
    output = [""]*n
    for i in range(n):
        for j in range(n):
            output[i] += str(randint(1, 9))
    return output
input_grids = {}

lola_times = []
lynne_times = []
loop = range(5, 15)
print('Brute forcing valid grids...')
for i in loop:
    print('')
    lola_time = 0
    lynne_time = 0
    for j in range(100):
        grid = random_grid(i)
        s = perf_counter()
        lola_answer = lola(grid)
        lola_time += perf_counter() - s
        s = perf_counter()
        lynne_answer = lynne(grid)
        lynne_time += perf_counter() - s
        if lola_answer == lynne_answer:
            input_grids.setdefault(i, [])
            input_grids[i].append(grid)
    lola_times.append(lola_time)
    lynne_times.append(lynne_time)
    print(f'Generated {len(input_grids[i])} valid input grids with size {i}')
    print(f'Time spent computing:')
    print(f'Lola: {lola_time} ({lola_time/100}/it)')
    print(f'Lynne: {lynne_time} ({lynne_time/100}/it)')
    if lola_time > lynne_time:
        print('Winner: Lynne')
    else:
        print('Winner: Lola')
    print(f'Difference: {abs(lola_time - lynne_time)} ({abs(lola_time - lynne_time)/100}/it)')
diffs = [abs(lola_times[loop.index(i)] - lynne_times[loop.index(i)]) for i in loop]
ax.plot(loop, lola_times, label='Lola')
ax.plot(loop, lynne_times, label='Lynne')
ax.plot(loop, diffs, label='Diff')
ax.set_xlabel('Input size')
ax.set_ylabel('Execution time')
plt.title('Brute Forcing Valid Graphs')
matplotx.line_labels()
plt.show()

fig, ax = plt.subplots()

# input_grids = {10: [['8448854321', '4447645251', '6542573645', '4725275268', '6442514153', '4515734868', '5513676158', '3257376185', '2172424467', '6775163586']]}

lola_times = []
lynne_times = []
print('Racing on known grids')
for size in input_grids:
    print('')
    lola_time = 0
    lynne_time = 0
    for j in range(100):
        grid = choice(input_grids[size])
        s = perf_counter()
        lola_answer = lola(grid)
        lola_time += perf_counter() - s
        s = perf_counter()
        lynne_answer = lynne(grid)
        lynne_time += perf_counter() - s
        if lola_answer != lynne_answer:
            print('DISCREPANCY ALERT (cringe)')
            print('Input grid:')
            for line in grid:
                print(line)
            print(f'Lola Answer: {lola_answer}')
            print(f'Lynne Answer: {lynne_answer}')
            input_grids[size].remove(grid)
    print(f'On valid input grids with size {size}:')
    print(f'Time spent computing:')
    print(f'Lola: {lola_time} ({lola_time / 100}/it)')
    print(f'Lynne: {lynne_time} ({lynne_time / 100}/it)')
    if lola_time > lynne_time:
        print('Winner: Lynne')
    else:
        print('Winner: Lola')
    print(f'Difference: {abs(lola_time - lynne_time)} ({abs(lola_time - lynne_time) / 100}/it)')
    lola_times.append(lola_time)
    lynne_times.append(lynne_time)

loop = input_grids.keys()
diffs = [abs(lola_times[i] - lynne_times[i]) for i in range(len(loop))]
ax.plot(loop, lola_times, label='Lola')
ax.plot(loop, lynne_times, label='Lynne')
ax.plot(loop, diffs, label='Diff')
ax.set_xlabel('Input size')
ax.set_ylabel('Execution time')
plt.title('Brute forced graphs as input')
matplotx.line_labels()
plt.show()

# print(lola(random_grid(10)))
# race(lola, lynne, lines)
