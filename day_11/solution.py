"""
Day 11
======
Seating System
"""
from collections import namedtuple

Coord = namedtuple("Coord", ["x", "y"])


def main(seat_chart):
    current = serialize(seat_chart)
    updated = change_seating(seat_chart)

    while current != serialize(updated):
        current = serialize(updated)
        updated = change_seating(updated)

    return updated


def serialize(seat_chart):
    return "\n".join(["".join(row) for row in seat_chart])


def change_seating(seat_chart):
    """
    Does the thing
    """
    to_be_seated = []
    to_be_unseated = []
    for y in range(len(seat_chart)):
        row = seat_chart[y]
        for x in range(len(row)):
            seat = row[x]
            coord = Coord(x, y)
            if seat == ".":
                continue

            adjacent = adjacent_coords(coord)
            surrounding = [get_seat(seat_chart, coord) for coord in adjacent]

            if seat == "L" and all([s != "#" for s in surrounding if s is not None]):
                to_be_seated.append(coord)
                continue

            if seat == "#" and len([s for s in surrounding if s == "#"]) >= 4:
                to_be_unseated.append(coord)
                continue

    for c in to_be_seated:
        seat_chart[c.y][c.x] = "#"

    for c in to_be_unseated:
        seat_chart[c.y][c.x] = "L"

    return seat_chart


def get_seat(seat_chart, coord):
    """
    return seat for valid coordinate set
    """
    height = len(seat_chart)
    width = len(seat_chart[0])

    if (0 <= coord.x < width) and (0 <= coord.y < height):
        return seat_chart[coord.y][coord.x]
    return None


def adjacent_coords(coord):
    """
    A list of all points surrounding a given coordinate set
    """
    return [
        # South
        Coord(coord.x, coord.y + 1),
        # South East
        Coord(coord.x + 1, coord.y + 1),
        # East
        Coord(coord.x + 1, coord.y),
        # North East
        Coord(coord.x + 1, coord.y - 1),
        # North
        Coord(coord.x, coord.y - 1),
        # North West
        Coord(coord.x - 1, coord.y - 1),
        # West
        Coord(coord.x - 1, coord.y),
        # North West
        Coord(coord.x - 1, coord.y + 1),
    ]


if __name__ == "__main__":
    with open("input.txt", "r") as rawdata:
        dataset = [[char for char in line] for line in rawdata.read().splitlines()]
        finalized = serialize(main(dataset))
        print("Part 1:", len([x for x in finalized if x == "#"]))
