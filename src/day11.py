#!/usr/bin/env python3

from os.path import abspath

N  = 'n'
NE = 'ne'
SE = 'se'
S  = 's'
SW = 'sw'
NW = 'nw'

DIRECTIONS = {
    N:  {S:  None, SE: NE, SW: NW},
    NE: {SW: None, NW: N,  S:SE},
    SE: {NW: None, N:  NE, SW: S},
    S:  {N:  None, NE: SE, NW: SW},
    SW: {NE: None, N:  NW, SE: S},
    NW: {SE: None, NE: N,  S: SW}
}

INPUT_FILE = abspath('../input/day11.txt')


class HexGrid:

    def __init__(self, path):
        self.path = path
        self.index = 0


    def get_shortest_path(self):
        while self.index < len(self.path):
            if not self._handle_step():
                self.index += 1
        return(len(self.path), self.path)


    def _handle_step(self):
        """Using a list of instructions from a given location, look ahead for
        a given step.  If found remove the step and replace the step at the
        current index.
        return True if the path has changed else False
        """
        for step, replacement in DIRECTIONS[self.path[self.index]].items():
            preview = self.index + 1
            while preview < len(self.path):
                if (self.path[preview] == step):
                    del self.path[preview]
                    if replacement:
                        self.path[self.index] = replacement
                    else:
                        del self.path[self.index]
                    return True
                preview += 1
        return False


    def find_furthest_point(self):
        furthest = 0
        route = []
        for step in self.path:
            # Append the new step to a planned route
            route.append(step)
            route = self._handle_step_in_reverse(route)

            if len(route) > furthest:
                furthest = len(route)

        return (furthest, route)


    def _handle_step_in_reverse(self, route):
        ''' Similar to _handle_step, but searches in reverse '''
        # Use a dictionary lookup to find direction replacements to
        # keep the route as short as possible
        for lookup, replacement in DIRECTIONS[route[-1]].items():
            # Loop backwards looking for direction replacements
            for rearview in range(len(route) - 1, -1, -1):
                if (route[rearview] == lookup):
                    del route[-1] # Remove the item just added
                    if replacement:
                        route[rearview] = replacement
                    else:
                        del route[rearview]
                    return route
        return route


def test_shortest(input, expected):
    hex = HexGrid(input)
    title = 'Test Shortest: HexGrid({})'.format(input)
    actual = hex.get_shortest_path()

    try:
        assert(actual == expected)
    except AssertionError:
        print(title)
        print('    Expected: {} {}'.format(*expected))
        print('    Actual  : {} {}'.format(*actual))

def test_furthest(input, expected):
    hex = HexGrid(input)
    actual = hex.find_furthest_point()

    try:
        assert(actual == expected)
    except AssertionError:
        print('Test Furthest: HexGrid({})'.format(input))
        print('    Expected: {} {}'.format(*expected))
        print('    Actual  : {} {}'.format(*actual))


if __name__ == '__main__':

    test_shortest([NE,NE,NE], (3, [NE,NE,NE]))
    test_shortest([NE,NE,SW,SW], (0, []))
    test_shortest([NE,NE,S,S], (2, [SE,SE]))
    test_shortest([SE,SW,SE,SW,SW], (3, [S,S,SW]))

    test_furthest([NE,NE,NE], (3, [NE,NE,NE]))
    test_furthest([NE,NE,SW,SW], (2, []))
    test_furthest([NE,NE,S,S], (2, [SE,SE]))
    test_furthest([SE,SW,SE,SW,SW], (3, [S,S,SW]))

    input = open(INPUT_FILE, 'r').read().strip().split(',')
    hex = HexGrid(input)
    furthest, path = hex.find_furthest_point()

    print('Day 11: Part 1:', len(path))
    print('Day 11: Part 2:', furthest)
