"""
Day 12
======
Rain Risk
"""

import re
from collections import namedtuple


def main(action_list):
    """
    Does the thing
    """
    x = 0
    y = 0

    facing = 90
    for action in action_list:
        parsed = re.match(r"\A(?P<direction>[A-Z]{1})(?P<distance>\d+)\Z", action)
        direction, distance = (parsed.group("direction"), int(parsed.group("distance")))

        if direction == "L":
            facing -= distance

        if direction == "R":
            facing += distance

        if facing < 0:
            facing += 360

        if facing >= 360:
            facing -= 360

        if direction == "F":
            if facing == 0:
                y += distance
            elif facing == 90:
                x += distance
            elif facing == 180:
                y -= distance
            else:
                x -= distance

        if direction == "N":
            y += distance

        if direction == "E":
            x += distance

        if direction == "S":
            y -= distance

        if direction == "W":
            x -= distance

    return abs(x) + abs(y)


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()
        print("Part 1:", main(dataset))
