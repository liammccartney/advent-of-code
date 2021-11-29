"""
Day 15
======
Rambunctious Recitation
"""
from collections import defaultdict


def main(numbers, limit):
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

    for p in range(limit - len(numbers)):
        number_count = len(number_ages[number])

        if number_count > 1:
            ages = number_ages[number]
            number = ages[-1] - ages[-2]
        else:
            number = 0

        number_ages[number].append(turn)
        number_ages[number] = number_ages[number][-2:]

        turn += 1

    return number


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = [int(x) for x in dataset.read().split(",")]
        print("Part 1:", main(dataset, 2020))
        print("Part 2:", main(dataset, 30000000))
