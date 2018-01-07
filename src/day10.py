#!/usr/bin/env python3


INPUT = [197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]

TEST_INPUT = [3, 4, 1, 5]
TEST_OUTPUT_LIST = [3,4,2,1,0]
TEST_OUTPUT_POSITION = 4
TEST_OUTPUT_VALUE = 12
TEST_SIZE = 5


class KnotHash:


    def __init__(self, size=256):
        self.list = list(range(0, size))
        self.current_position = 0
        self.skip_size = 0
        self.size = len(self.list) # Don't calculate this every time


    def _single_hash(self, length):
        first = self.current_position
        last  = self.current_position + length

        # Extract a slice of the circular list of the given length
        slice = []
        if last > self.size:
            slice = self.list[first:] + self.list[:last % self.size]
        else:
            slice = self.list[first:last]

        # Reverse the values and insert them back into the list
        index = first
        for value in reversed(slice):
            self.list[index] = value
            index = (index + 1) % self.size

        # Increment the current position and wrap
        self.current_position += length + self.skip_size
        self.current_position %= self.size

        self.skip_size += 1


    def hash(self, lengths=[]):
        for length in lengths:
            self._single_hash(length)
        return self.list[0] * self.list[1]


if __name__ == '__main__':
    tkh = KnotHash(TEST_SIZE)
    tkh_actual = tkh.hash(TEST_INPUT)
    print('  test hash output {} == {}'.format(tkh_actual, TEST_OUTPUT_VALUE))
    assert tkh_actual == TEST_OUTPUT_VALUE

    print('  test hash list {} == {}'.format(tkh.list, TEST_OUTPUT_LIST))
    assert tkh.list == TEST_OUTPUT_LIST

    print('  test hash list {} == {}'.format(
            tkh.current_position, TEST_OUTPUT_POSITION))
    assert tkh.current_position == TEST_OUTPUT_POSITION

    print('Day 10: Part 1:', KnotHash().hash(INPUT))
