#!/usr/bin/env python3

# Conway's game of life simulator.
# v20150504
#
# Author: Hadrien Wild
# E-mail: hadrien.wild@gmail.com


from random import randrange


class Conway(object):
    def __init__(self):
        """
        Creates a Conway's game simulator.

        Attributes:
            cells (dict): Cells contained in the world, which is represented as a 2D grid.
                          The keys of the dictionary are x, y (tuple) coordinates in the world.
                          Cells are represented as True (bool).

        Args:
            n (int): Number of cells to create.
        """
        self.cells = {}

    def create_random_cells(self, n, left, right, bottom, top):
        """
        Creates n cells at random coordinates in a limited square whose coordinates must be defined.
        The method doesn't check whether there is already a cell at a place or not.

        Args:
            n (int): Number of cells to create.
            left (int): Left-limit of the square delimiting the random creation.
            right (int): Right limit of the square delimiting the random creation.
            top (int): Top-limit of the square delimiting the random creation.
            bottom (int): Bottom-limit of the square delimiting the random creation.
        """
        for i in range(n):
            self.cells[(randrange(left, right), randrange(bottom, top))] = True

    def count_cells(self):
        """
        Counts the cells contained in the world.

        Returns:
            (int): Returns the number of cells contained in the world.
        """
        return len(self.cells)

    def update_world(self):
        """
        Updates the world to its next state, according to the Conway's game rules.
        """
        old_cells = self.cells.copy()

        for coordinates in old_cells.keys():

            # on cell
            neighbours_count = self.__count_neighbours(coordinates, old_cells)
            if neighbours_count < 2 or neighbours_count > 3:
                del(self.cells[coordinates])

            # around the cell:
            x, y = coordinates[0], coordinates[1]

            if (x-1, y+1) not in old_cells and self.__count_neighbours((x-1, y+1), old_cells) == 3:
                self.cells[(x-1, y+1)] = True # upper-left
            if (x-1, y) not in old_cells and self.__count_neighbours((x-1, y), old_cells) == 3:
                self.cells[(x-1, y)] = True   # left
            if (x-1, y-1) not in old_cells and self.__count_neighbours((x-1, y-1), old_cells) == 3:
                self.cells[(x-1, y-1)] = True #lower-left
            if (x+1, y+1) not in old_cells and self.__count_neighbours((x+1, y+1), old_cells) == 3:
                self.cells[(x+1, y+1)] = True # uper-right
            if (x+1, y) not in old_cells and self.__count_neighbours((x+1, y), old_cells) == 3:
                self.cells[(x+1, y)] = True   # right
            if (x+1, y-1) not in old_cells and self.__count_neighbours((x+1, y-1), old_cells) == 3:
                self.cells[(x+1, y-1)] = True # lower-right
            if (x, y+1) not in old_cells and self.__count_neighbours((x, y+1), old_cells) == 3:
                self.cells[(x, y+1)] = True   # top
            if (x, y-1) not in old_cells and self.__count_neighbours((x, y-1), old_cells) == 3:
                self.cells[(x, y-1)] = True   # bottom

    def __count_neighbours(self, coordinates, cells):
        """
        <Helper function for update_world()>
        Counts the cells around the coordinates in the old_cells world.

        Args:
            coordinates (tuple): Coordinates x, y (int).
            cells (dict): Cells in the old_cell world.

        Returns:
            neighbours_count (int): Number of cells around the coordinate.
        """
        x, y = coordinates[0], coordinates[1]

        neighbours_count = 0

        if (x-1, y+1) in cells: # upper-left
            neighbours_count += 1
        if (x-1, y) in cells:   # left
            neighbours_count += 1
        if (x-1, y-1) in cells: # lower-left
            neighbours_count += 1
        if (x+1, y+1) in cells: # upper-right
            neighbours_count += 1
        if (x+1, y) in cells:   # right
            neighbours_count += 1
        if (x+1, y-1) in cells: # lower-right
            neighbours_count += 1
        if (x, y+1) in cells:   # top
            neighbours_count += 1
        if (x, y-1) in cells:   # bottom
            neighbours_count += 1

        return neighbours_count

    def get_cells(self):
        """
        Returns cells contained in the world.

        Returns:
            (dict): Returns cells contained in the world, which is represented as a 2D grid.
                    The keys of the dictionnary are x, y (tuple) coordinates in the world.
                    Cells are represented as True (bool).
        """
        return self.cells
