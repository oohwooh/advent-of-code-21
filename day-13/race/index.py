from race.index import race
from lola import lola
from lynne import lynne
with open('race-input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
print()
race(lola, lynne, lines, 1000)
