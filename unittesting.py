#!/usr/bin/env python 3

# conway.py unit testing


from conway import *


game = Conway()
game.create_random_cells(100, -100, 200, -100, 200)
cells = game.get_cells()

assert len(cells) > 0
assert game.count_cells() == len(cells)

for coordinates, cell in cells.items():
    assert type(coordinates) is tuple
    assert cell == True
    print("{0}\t{1}".format(coordinates, cell))
