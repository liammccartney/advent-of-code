def part_1(commands):
    x = 0
    y = 0
    for direction, distance in commands:
        distance = int(distance)
        if direction == "forward":
            x += distance

        elif direction == "up":
            y -= distance

        elif direction == "down":
            y += distance
    return x * y


def part_2(commands):
    x = 0
    y = 0
    aim = 0
    for direction, distance in commands:
        distance = int(distance)
        if direction == "forward":
            x += distance
            y += aim * distance

        elif direction == "up":
            aim -= distance

        elif direction == "down":
            aim += distance
    return x * y


if __name__ == "__main__":
    with open("../input/day02.txt", "r") as commands:
        commands = [tuple(d.strip().split(" ")) for d in commands.readlines()]
        print("Part 1:", part_1(commands))
        print("Part 2:", part_2(commands))
