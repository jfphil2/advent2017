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

if __name__ == '__main__':
    test(1, 0)
    test(12, 3)
    test(23, 2)
    test(1024, 31)
    print("Part One Solution:", manhattan_path(INPUT))
