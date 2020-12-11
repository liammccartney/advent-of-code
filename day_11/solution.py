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

            adjacent = adjacent_coords(coord, len(row), len(seat_chart))

            surrounding = []

            for d, line_of_sight in adjacent.items():
                for point in line_of_sight:
                    sseat = get_seat(seat_chart, point)
                    if sseat in ("L", "#"):
                        surrounding.append(sseat)
                        break

            if seat == "L" and all([z in ("L", ".") for z in surrounding]):
                to_be_seated.append(coord)
                continue

            if seat == "#" and len([v for v in surrounding if v == "#"]) >= 5:
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


def adjacent_coords(coord, width, height):
    """
    A list of all points surrounding a given coordinate set
    """
    adjacent = {
        "S": [],
        "SE": [],
        "E": [],
        "NE": [],
        "N": [],
        "NW": [],
        "W": [],
        "SW": [],
    }
    x = coord.x
    y = coord.y

    # S
    delta_y = 1
    while delta_y + y < height:
        adjacent["S"].append(Coord(x, y + delta_y))
        delta_y += 1

    # SE?
    delta_x = x + 1
    delta_y = y + 1
    while delta_x < width and delta_y < height:
        adjacent["SE"].append(Coord(delta_x, delta_y))
        delta_x += 1
        delta_y += 1

    # E
    delta_x = 1
    while x + delta_x < width:
        adjacent["E"].append(Coord(x + delta_x, y))
        delta_x += 1

    # NE?
    delta_x = 1
    delta_y = y - 1
    while delta_x < width - x and delta_y >= 0:
        adjacent["NE"].append(Coord(x + delta_x, delta_y))
        delta_x += 1
        delta_y -= 1

    # N
    delta_y = y - 1
    while delta_y >= 0:
        adjacent["N"].append(Coord(x, delta_y))
        delta_y -= 1

    # NW?
    delta_x = x - 1
    delta_y = y - 1
    while delta_x >= 0 and delta_y >= 0:
        adjacent["NW"].append(Coord(delta_x, delta_y))
        delta_x -= 1
        delta_y -= 1
    # W
    delta_x = x - 1
    while delta_x >= 0:
        adjacent["W"].append(Coord(delta_x, y))
        delta_x -= 1

    # SW?
    delta_x = x - 1
    delta_y = 1
    while delta_x >= 0 and y + delta_y < height:
        adjacent["SW"].append(Coord(delta_x, y + delta_y))
        delta_x -= 1
        delta_y += 1

    return adjacent


if __name__ == "__main__":
    with open("input.txt", "r") as rawdata:
        dataset = [[char for char in line] for line in rawdata.read().splitlines()]
        finalized = serialize(main(dataset))
        print("Part 1:", len([x for x in finalized if x == "#"]))
