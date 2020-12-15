"""
Day 12
======
Rain Risk
"""

import re
from collections import namedtuple
from math import pi, ceil, cos, sin


def part_1(action_list):
    """
    Does the thing
    """
    x = 0
    y = 0

    facing = 90
    for action in action_list:
        direction, distance = parse_action(action)
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


def parse_action(action):
    """
    Extract direction and numerica value out of a navigational action
    """
    parsed = re.match(r"\A(?P<direction>[A-Z]{1})(?P<distance>\d+)\Z", action)
    return (parsed.group("direction"), int(parsed.group("distance")))


class Point:
    """
    X, Y Coordinates
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


def part_2(action_list):
    """
    Part 1
    """
    ship = Point(0, 0)
    waypoint = Point(10, 1)

    for action in action_list:
        direction, action_value = parse_action(action)

        if direction == "F":
            move_ship(ship, waypoint, action_value)

        if direction == "L":
            rotate_waypoint(waypoint, action_value * -1)

        if direction == "R":
            rotate_waypoint(waypoint, action_value)

        if direction == "N":
            waypoint.y += action_value

        if direction == "E":
            waypoint.x += action_value

        if direction == "S":
            waypoint.y -= action_value

        if direction == "W":
            waypoint.x -= action_value

    return abs(ship.x) + abs(ship.y)


def move_ship(ship, waypoint, action_value):
    """
    Move ship towards waypoint
    """
    ship.x += waypoint.x * action_value
    ship.y += waypoint.y * action_value


def rotate_waypoint(waypoint, degrees):
    """
    Rotate waypoint around ship
    """
    radians = degrees * (pi / 180)

    x = waypoint.x
    y = waypoint.y

    new_x = x * cos(radians) + y * sin(radians)

    if new_x < 0:
        new_x *= -1
        new_x = round(new_x)
        new_x *= -1
    else:
        new_x = round(new_x)

    new_y = -1 * (x * sin(radians)) + y * cos(radians)

    if new_y < 0:
        new_y *= -1
        new_y = round(new_y)
        new_y *= -1
    else:
        new_y = round(new_y)

    waypoint.x = new_x
    waypoint.y = new_y


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()
        print("Part 1:", part_1(dataset))
        print("Part 2:", part_2(dataset))
