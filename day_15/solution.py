"""
Day 15
======
Rambunctious Recitation
"""
from collections import defaultdict


def part_1(numbers):
    """
    Does the thing
    """
    turn = 1
    number = None
    number_ages = defaultdict(list)

    for n in numbers:
        number_ages[n].append(turn)
        number = n
        turn += 1

    for p in range(2020 - len(numbers)):
        number_count = len(number_ages[number])

        if number_count > 1:
            ages = number_ages[number]
            number = ages[-1] - ages[-2]
        else:
            number = 0

        number_ages[number].append(turn)

        turn += 1

    return number


if __name__ == "__main__":
    assert (part_1([0, 3, 6])) == 436
    assert (part_1([1, 3, 2])) == 1
    assert (part_1([2, 1, 3])) == 10
    assert (part_1([1, 2, 3])) == 27
    assert (part_1([2, 3, 1])) == 78
    assert (part_1([3, 2, 1])) == 438
    assert (part_1([3, 1, 2])) == 1836

    with open("input.txt", "r") as dataset:
        dataset = [int(x) for x in dataset.read().split(",")]
        print("Part 1:", part_1(dataset))
