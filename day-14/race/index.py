from race.index import race
from lola import lola
from lynne import lynne
with open('race-input.txt') as f:
    lines = [l.strip() for l in f.readlines()]
race(lola, lynne, lines, loop_count=1000)
