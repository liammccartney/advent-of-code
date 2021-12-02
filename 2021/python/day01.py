def part_1(depths):
    increases = 0
    for i, d in enumerate(depths):
        if i == len(depths) - 1:
            return increases

        next_d = depths[i + 1]

        if next_d > d:
            increases += 1


def part_2(depths):
    window_sums = []
    for i, d in enumerate(depths):
        if i >= len(depths) - 2:
            continue

        next_d = depths[i + 1]
        next_next_d = depths[i + 2]

        window_sums.append(d + next_d + next_next_d)

    return part_1(window_sums)


if __name__ == "__main__":
    with open("../input/day01.txt", "r") as depths:
        depths = [int(d) for d in depths.readlines()]
        print("Part 1:", part_1(depths))
        print("Part 2:", part_2(depths))
