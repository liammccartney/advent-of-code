from collections import defaultdict


def part_1(fish, day, goal):
    if day > goal:
        return len(fish)

    old_fish = []
    new_fish = []
    for f in fish:
        if f == 0:
            new_fish.append(8)
            old_fish.append(6)
            continue

        old_fish.append(f - 1)

    return part_1(old_fish + new_fish, day + 1, goal)


def part_2(fish, day, goal):
    fish_freq = defaultdict(int)

    for f in fish:
        fish_freq[f] += 1

    return part_2_helper(fish_freq, day, goal)


def part_2_helper(fish_freq: dict, day: int, goal: int) -> int:
    if day > goal:
        return sum([c for _, c in fish_freq.items()])

    fish_about_to_give_birth = fish_freq[0]

    for i in range(1, 9):
        fish_freq[i - 1] = fish_freq[i]
        fish_freq[i] = 0

    fish_freq[6] += fish_about_to_give_birth
    fish_freq[8] += fish_about_to_give_birth

    return part_2_helper(fish_freq, day + 1, goal)


if __name__ == "__main__":
    with open("../input/day06.txt", "r") as fish:
        fish = [int(f) for f in fish.read().split(",")]
        print("Part 1:", part_1(fish, 1, 80))
        print("Part 2:", part_2(fish, 1, 256))
