"""
Day 10
======
Adapter Array
"""
from collections import defaultdict


def main(data):
    """
    Does the thing
    """
    differences = defaultdict(int)
    data = [0] + data
    for i, adapter in enumerate(data):
        if i >= len(data) - 1:
            differences[3] += 1
            continue

        next_adapter = data[i + 1]
        differences[next_adapter - adapter] += 1

    return differences


def part_2(adapters):
    path_counts = defaultdict(int)
    path_counts[0] = 1
    for i, a in enumerate(adapters):
        path_counts[a] = 0
        for diff in range(1, 4):
            if path_counts.get(a - diff):
                path_counts[a] += path_counts[a - diff]
    return path_counts[max(dataset)]


# def find_arrangements(data):
#     """
#     Count valid arrangements of adapters
#     """

#     def helper(current, options):
#         if len(options) == 0:
#             return 1
#         next_adapters = find_next_valid_options(current, options)

#         return sum([helper(adapter, options[i + 1 :]) for i, adapter in next_adapters])

#     return helper(0, data)


# def find_next_valid_options(adapter, next_adapters):
#     """
#     for a given adapter and all subsequent adapters, find the next n adapters
#     that satisfy the constraint
#     """
#     options = tuple()

#     for i, next_adapter in enumerate(next_adapters):
#         if next_adapter - adapter > 3:
#             return options
#         options = options + (next_adapter,)
#     return options


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = sorted([int(d) for d in dataset.read().splitlines()])
        result = main(dataset)
        print("Part 1:", main(dataset))
        print("Part 2:", part_2(dataset))
