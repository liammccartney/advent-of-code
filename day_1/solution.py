def part_1(expenses):
    for i in expenses:
        diff = 2020 - i
        if diff in expenses:
            return diff * i


def part_2(expenses):
    with open("input.txt", "r") as expenses:
        expenses = [int(exp) for exp in expenses.readlines()]
        for iidx, i in enumerate(expenses):
            for jdx, j in enumerate(expenses[iidx:]):
                for k in expenses[jdx:]:
                    if i + j + k == 2020:
                        return i * j * k


if __name__ == "__main__":
    with open("input.txt", "r") as expenses:
        expenses = [int(exp) for exp in expenses.readlines()]
        print("Part 1:", part_1(expenses))
        print("Part 2:", part_2(expenses))
