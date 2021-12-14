from race.index import race
from lola import lola
from lynne import lynne
# with open('race-input.txt') as f:
    # lines = f.readlines()
# race(lola, lynne, lines, 5)
lines = (['1', '2', '3', '4', '5', '5'], '123455')
def listcount(lines):
    return lines[0].count('5')
def strcount(lines):
    return lines[1].count('5')
race(listcount, strcount, lines, 10000000)