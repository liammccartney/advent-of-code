from collections import defaultdict


def part_1(report):
    transposed = zip(*report)
    gamma = ""
    epsilon = ""

    for bit in transposed:
        most = most_common(bit)
        gamma += most
        if most == "1":
            epsilon += "0"
        else:
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def most_common(lst):
    freq = defaultdict(int)
    for l in lst:
        freq[l] += 1

    if freq["1"] >= freq["0"]:
        return "1"

    return "0"


def part_2(report):
    if len(report) == 1:
        return int(report[0], 2)

    oxygen_generator_search = report[0:]
    co2_scrubber_search = report[0:]

    for i in range(len(report[0])):
        transposed_oxy = list(zip(*oxygen_generator_search))
        transposed_co2 = list(zip(*co2_scrubber_search))

        most_oxy = most_common(transposed_oxy[i])

        if len(oxygen_generator_search) > 1:
            oxygen_generator_search = [
                b for b in oxygen_generator_search if b[i] == most_oxy
            ]

        most_co2 = most_common(transposed_co2[i])
        least_co2 = "0"
        if most_co2 == "1":
            least_co2 = "0"
        else:
            least_co2 = "1"

        if len(co2_scrubber_search) > 1:
            co2_scrubber_search = [b for b in co2_scrubber_search if b[i] == least_co2]

    co2_scrubber_rate = co2_scrubber_search[0]
    oxygen_generator = oxygen_generator_search[0]

    return int(co2_scrubber_rate, 2) * int(oxygen_generator, 2)


if __name__ == "__main__":
    with open("../input/day03.txt", "r") as commands:
        report = [d.strip() for d in commands.readlines()]
        print("Part 1:", part_1(report))
        print("Part 2:", part_2(report))
