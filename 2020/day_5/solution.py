"""
Day 5
=====
Seat Numbers
"""
import math


def find_seat_ids(seat_spec_list):
    """
    Does the thing
    """
    seat_ids = []
    for seat_spec in seat_spec_list:
        row_range = range(0, 128)
        col_range = range(0, 8)
        row = find_row(row_range, seat_spec[0:7])
        col = find_col(col_range, seat_spec[7:])
        seat_ids.append(int(row) * 8 + int(col))

    return seat_ids


def find_row(row_range, row_spec):
    """
    Recursively find the row
    """
    if len(row_range) == 1:
        return row_range[0]

    mid_idx = math.ceil((len(row_range) - 1) / 2)

    if row_spec[0] == "F":
        return find_row(row_range[0:mid_idx], row_spec[1:])

    if row_spec[0] == "B":
        return find_row(row_range[mid_idx:], row_spec[1:])


def find_col(col_range, col_spec):
    """
    Recursively find the col
    """
    if len(col_range) == 1:
        return col_range[0]

    mid_idx = math.ceil((len(col_range) - 1) / 2)

    if col_spec[0] == "L":
        return find_col(col_range[0:mid_idx], col_spec[1:])

    if col_spec[0] == "R":
        return find_col(col_range[mid_idx:], col_spec[1:])


def part_2(seat_ids):
    """
    Part 2
    """
    for i, seat_id in enumerate(seat_ids):
        print(seat_id, seat_ids[i + 1])
        if seat_ids[i + 1] != seat_id + 1:
            return seat_id + 1


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        seat_ids = find_seat_ids(data)
        print("Part 1:", max(seat_ids))
        # print(sorted(seat_ids))
        print("Part 2:", part_2(sorted(seat_ids)))
