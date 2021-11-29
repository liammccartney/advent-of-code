"""
Day 16
======
Ticket Translation
"""

import re

from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def part_1(data):
    """
    Find invalid ticket data
    """
    ruleset, tickets = parse(data)
    invalid = []

    for ticket in tickets:
        for digit in ticket:
            if all(digit not in rule for rule in ruleset):
                invalid.append(digit)

    return sum(invalid)


def parse(data):
    """
    Parse out rules, your ticket, all other tickets
    """
    ruleset = []

    for rule in dataset[0].splitlines():
        digits = [int(d) for d in re.findall(r"\d+", rule)]
        for valid_range in grouper(digits, 2):
            ruleset.append(range(valid_range[0], valid_range[1] + 1))

    ticket = [int(x) for x in dataset[1].splitlines()[1].split(",")]
    other_tickets = [
        [int(x) for x in y.split(",")] for y in dataset[2].splitlines()[2:]
    ]

    return ruleset, [ticket] + other_tickets


if __name__ == "__main__":
    print("Checking example data set:")
    with open("example.txt", "r") as dataset:
        dataset = dataset.read().split("\n\n")
        solution = part_1(dataset)
        assert solution == 71, "%d does not equal 71" % solution

    print()
    print("Prime time, now:")
    with open("input.txt", "r") as dataset:
        dataset = dataset.read().split("\n\n")
        print(part_1(dataset))
