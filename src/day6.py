#!/usr/bin/env python3


# Input reformatted for language simplicity
INPUT = [4, 1, 15, 12, 0, 9, 9, 5, 5, 8, 7, 3, 14, 5, 12, 3]

TEST_INPUT = [0, 2, 7, 0]
TEST_OUTPUT = 5


def loop_detector(input):
    distributions = []

    distribution = input
    while str(distribution) not in distributions:
        # Save current distribution
        distributions.append(str(distribution))
        print('    ', distribution)

        highest_index = 0
        highest_value = 0
        # Find index and value of largest bank
        for index, value in enumerate(distribution):
            if highest_value < value:
                highest_index = index
                highest_value = value

        # Zero out bank, save value, set index to bank + 1
        distribution[highest_index] = 0

        # Looping through the banks redistribute one block at a time
        blocks_remaining = highest_value # Change variable for readability
        index = highest_index + 1
        while blocks_remaining > 0:
            distribution[index % len(distribution)] += 1
            blocks_remaining -= 1
            index += 1

    print('    ', distribution)

    return len(distributions)


if __name__ == '__main__':
    redistributions = loop_detector(TEST_INPUT)
    print("loop_detector() = {} == {}".format(redistributions, TEST_OUTPUT))
    assert redistributions == TEST_OUTPUT

    print("Part One Solution:", loop_detector(INPUT))
