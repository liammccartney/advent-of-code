from collections import defaultdict
from pprint import pprint
import re


def part_1(paths):
    frequencies = defaultdict(int)

    for start, end in paths:
        start_x, start_y = start
        end_x, end_y = end

        if start_x == end_x:
            begin, finish = sorted((start_y, end_y))
            for y in range(begin, finish + 1):
                frequencies[(start_x, y)] += 1

        if start_y == end_y:
            begin, finish = sorted((start_x, end_x))
            for x in range(begin, finish + 1):
                frequencies[(x, start_y)] += 1

    return len([f for _, f in frequencies.items() if f >= 2])


def diagonal_path(start, end):
    path = []
    start_x, start_y = start
    end_x, end_y = end
    if start_x > end_x and start_y > end_y:
        while (start_x, start_y) != end:
            path.append((start_x, start_y))
            start_x -= 1
            start_y -= 1
        path.append(end)
        return path

    if start_x < end_x and start_y < end_y:
        while (start_x, start_y) != end:
            path.append((start_x, start_y))
            start_x += 1
            start_y += 1
        path.append(end)
        return path

    if start_x < end_x and start_y > end_y:
        while (start_x, start_y) != end:
            path.append((start_x, start_y))
            start_x += 1
            start_y -= 1
        path.append(end)
        return path

    if start_x > end_x and start_y < end_y:
        while (start_x, start_y) != end:
            path.append((start_x, start_y))
            start_x -= 1
            start_y += 1
        path.append(end)
        return path

    return path


def part_2(paths):
    frequencies = defaultdict(int)

    for start, end in paths:
        start_x, start_y = start
        end_x, end_y = end

        if start_x == end_x:
            begin, finish = sorted((start_y, end_y))
            for y in range(begin, finish + 1):
                frequencies[(start_x, y)] += 1
            continue

        if start_y == end_y:
            begin, finish = sorted((start_x, end_x))
            for x in range(begin, finish + 1):
                frequencies[(x, start_y)] += 1
            continue

        for p in diagonal_path(start, end):
            frequencies[p] += 1

    return len([f for _, f in frequencies.items() if f >= 2])


if __name__ == "__main__":
    with open("../input/day05.txt", "r") as raw_paths:
        paths = []
        pattern = re.compile(r"(?P<start>\d+,\d+) -> (?P<end>\d+,\d+)")
        for raw_path in raw_paths.readlines():
            match = re.match(pattern, raw_path)
            if match is None:
                continue
            start_x, start_y = match.group("start").split(",")
            end_x, end_y = match.group("end").split(",")

            paths.append(((int(start_x), int(start_y)), (int(end_x), int(end_y))))

        print("Part 1:", part_1(paths))
        print("Part 2:", part_2(paths))
