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


def test(input, expected):
    hex = HexGrid(input)
    title = 'Test: HexGrid({})'.format(input) # Easier than deep copy of list
    actual = hex.get_shortest_path()

    try:
        assert(actual == expected)
    except AssertionError:
        print(title)
        print('    Expected: {} {}'.format(*expected))
        print('    Actual  : {} {}'.format(*actual))


if __name__ == '__main__':

    test([NE,NE,NE], (3, [NE,NE,NE]))
    test([NE,NE,SW,SW], (0, []))
    test([NE,NE,S,S], (2, [SE,SE]))
    test([SE,SW,SE,SW,SW], (3, [S,S,SW]))


    with open(INPUT_FILE, 'r') as input:
        hex = HexGrid(input.read().strip().split(','))
        print('Day 11: Part 1:', hex.get_shortest_path()[0])
