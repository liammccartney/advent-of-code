from pprint import pprint


def part_1(crabs):
    crabs = sorted(crabs)
    return min([calc_fuel(c, crabs) for c in range(max(crabs) + 1)])


def calc_fuel(position, crabs):
    return sum([abs(c - position) for c in crabs])


def part_2(crabs):
    crabs = sorted(crabs)
    return min([calc_fuel_2(c, crabs) for c in range(max(crabs) + 1)])


def calc_fuel_2(position, crabs):
    return sum([sum(range(abs(c - position) + 1)) for c in crabs])


if __name__ == "__main__":
    with open("../input/day07.txt", "r") as crabs:
        crabs = [int(f) for f in crabs.read().split(",")]
        print("Part 1:", part_1(crabs))
        print("Part 2:", part_2(crabs))
