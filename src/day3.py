#!/usr/bin/env python3

from math import pow, floor

INPUT = 368078


def manhattan_path(input):

    # First task it to calculate the grid dimensions
    edge = 1
    last_value = 1
    while input > last_value:
        edge += 2
        last_value = int(pow(edge, 2))
    print("    Grid Dimensions: {}x{}".format(edge, edge))

    # I can make the assumption that the block will be on the outer most edge
    # of the square since I'm working out from the center.
    max_path = edge - 1
    min_path = int(max_path / 2)
    print("    Maximum Path: {}, Minimum Path: {}".format(max_path, min_path))

    # Now to locate the closest corner
    corner = last_value
    while corner - input > edge:
        corner -= edge + 1 # Corners are shared by edges so add 1

    # Calculate how far it is from the middle of the edge
    middle_value = corner - floor(edge / 2)
    distance_from_middle = abs(input - middle_value)
    print("    Corner:", corner)
    print("    Middle Value:", middle_value)
    print("    Distance from Middle:", distance_from_middle)

    steps = distance_from_middle + min_path
    return steps


def test(input, expected):
    actual = manhattan_path(input)
    print("manhattan_path({}) = {} == {}".format(input, actual, expected))
    assert actual == expected


class Grid:


    def __init__(self):
        self.grid = {0: {0: 1}}


    def add_new_value(self, x, y):
        sum = self.get_value(x, y)
        sum += self.get_value(x + 1, y)
        sum += self.get_value(x + 1, y + 1)
        sum += self.get_value(x, y + 1)
        sum += self.get_value(x - 1, y + 1)
        sum += self.get_value(x - 1, y)
        sum += self.get_value(x - 1, y - 1)
        sum += self.get_value(x, y - 1)
        sum += self.get_value(x + 1, y - 1)

        # print("  add_new_value({},{}) = {}".format(x, y, sum))

        if x not in self.grid.keys():
            self.grid[x] = {}
        self.grid[x][y] = sum
        self.print_value(x, y)


    def get_value(self, x, y):
        if x not in self.grid.keys():
            return 0
        if y not in self.grid[x].keys():
            return 0
        return self.grid[x][y]


    def print_value(self, x, y):
        print("    grid[{}][{}] = {}".format(x, y, self.get_value(x,y)))


def grid_stress_test(input):
    x = 0
    y = 0
    grow_factor = 0

    grid = Grid()
    while True:
        grow_factor += 1
        for xv in range(x + 1, x + grow_factor + 1, 1):
            grid.add_new_value(xv, y)
            if grid.get_value(xv, y) > input:
                return grid.get_value(xv, y)
        x = xv

        for yv in range(y + 1, y + grow_factor + 1, 1):
            grid.add_new_value(x, yv)
            if grid.get_value(x, yv) > input:
                return grid.get_value(x, yv)
        y = yv

        grow_factor += 1
        for xv in range(x - 1, x - grow_factor - 1, -1):
            grid.add_new_value(xv, y)
            if grid.get_value(xv, y) > input:
                return grid.get_value(xv, y)
        x = xv

        for yv in range(y - 1, y - grow_factor - 1, -1):
            grid.add_new_value(x, yv)
            if grid.get_value(x, yv) > input:
                return grid.get_value(x, yv)
        y = yv


def test_grid(input, expected):
    actual = grid_stress_test(input)
    print("grid_stress_test({}) = {} == {}".format(input, actual, expected))
    assert actual == expected


if __name__ == '__main__':
    # test(1, 0)
    # test(12, 3)
    # test(23, 2)
    # test(1024, 31)
    # print("Part One Solution:", manhattan_path(INPUT))

    test_grid(2, 4)
    test_grid(12, 23)
    test_grid(748, 806)
    print("Part Two Solution:", grid_stress_test(INPUT))

