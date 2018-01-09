#!/usr/bin/env python3


INPUT = '197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63'

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


    def _sparse_hash(self, lengths, rounds=64):
        ascii_lengths = []
        for char in lengths:
            ascii_lengths.append(ord(char))
        ascii_lengths += [17, 31, 73, 47, 23]

        for _ in range(rounds):
            for length in ascii_lengths:
                self._single_hash(length)


    def _dense_hash(self):
        hash = ''
        for index in range(0, self.size, 16):
            value = self.list[index]
            for offset in range(1, 16):
                value ^= self.list[index + offset]
            hash += '{:02x}'.format(value)
        return hash


    def full_hash(self, lengths):
        self._sparse_hash(lengths)
        return self._dense_hash()

def test_part2(input, expected):
    actual = KnotHash().full_hash(input)
    print('test KnotHash().full_hash({})\n    {} == {}'.format(
            input, actual, expected))
    assert actual == expected

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

    numeric_input_lengths = [int(i) for i in INPUT.split(',')]
    print('Day 10: Part 1:', KnotHash().hash(numeric_input_lengths))

    test_part2('', 'a2582a3a0e66e6e86e3812dcb672a272')
    test_part2('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd')
    test_part2('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d')
    test_part2('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e')

    print('Day 10: Part 2:', KnotHash().full_hash(INPUT))
