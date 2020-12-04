"""
Day 3
Tobogganing
"""

from collections import namedtuple
from functools import reduce


def main(field, slope):
    """
    How many trees are you gonna smack into?
    """
    trees = 0
    x = 0
    y = 0
    width = len(field[0])
    while y < len(field):
        if field[y][x] == "#":
            trees += 1

        x += slope.x
        if x > width - 1:
            x -= width

        y += slope.y

    return trees


if __name__ == "__main__":
    Slope = namedtuple("Slope", ("x", "y"))
    slopes = [Slope(1, 1), Slope(3, 1), Slope(5, 1), Slope(7, 1), Slope(1, 2)]

    with open("input.txt", "r") as field_data:
        field = field_data.read().splitlines()
        print(reduce(lambda x, y: x * y, [main(field, slope) for slope in slopes]))
