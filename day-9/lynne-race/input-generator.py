import random

class Input:
    def __init__(self, size):
        self.grid = {(x, y):9 for x in range(size) for y in range(size)}
        print(self.grid)
Input(100)