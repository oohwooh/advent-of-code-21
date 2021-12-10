from race import race
from lola import lola
from lynne import lynne
with open('race-input.txt') as f:
    lines = f.readlines()
race(lola, lynne, lines)
