import os
import sys

day = sys.argv[1]
day_folder = f'day-{day}'
empty_files = [f'{day_folder}/part-1.py',
               f'{day_folder}/part-2.py',
               f'{day_folder}/example.txt',
               f'{day_folder}/input.txt',
               f'{day_folder}/race/lola.py',
               f'{day_folder}/race/lynne.py',
               f'{day_folder}/race/race-input.txt',
               ]
try:
    os.mkdir(day_folder)
except:
    pass
try:
    os.mkdir(f'{day_folder}/race')
except:
    pass

for f in empty_files:
    with open(f, "wb+") as fl:
        fl.write(bytes())

with open(f'day-{day}/race/index.py', "w+") as racefile:
    racefile.writelines([
        "from race import race\n",
        "from lola import lola\n",
        "from lynne import lynne\n",
        "with open('race-input.txt') as f:\n",
        "    lines = f.readlines()\n",
        "race(lola, lynne, lines)\n"
    ])