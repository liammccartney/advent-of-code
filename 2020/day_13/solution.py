"""
Day 13
======
Shuttle Search
"""
from time import time


def part_1(earliest_departure, schedule):
    """
    Does the thing
    """
    departure = None
    bus_id = None
    working_departure = earliest_departure

    while departure is None:
        for t in schedule:
            if working_departure % t == 0:
                departure = working_departure
                bus_id = t
        working_departure += 1

    return bus_id * (departure - earliest_departure)


def part_2(schedule):
    t = 0
    first_bus, bus_tail = int(schedule[0]), schedule[1:]
    span_found = False

    while span_found is False:
        if all(
            future_bus == "x" or (t + i + 1) % int(future_bus) == 0
            for i, future_bus in enumerate(bus_tail)
        ):
            span_found = True
        else:
            t += first_bus

    return t


if __name__ == "__main__":
    # with open("example.txt", "r") as dataset:
    #     dataset = dataset.read().splitlines()
    #     print("Part 2:", part_2(dataset[1].split(",")))

    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()
        # filtered_schedule = [int(t) for t in dataset[1].split(",") if t != "x"]
        # print("Part 1:", part_1(int(dataset[0]), filtered_schedule))

        start = time()
        print("Part 2:", part_2(dataset[1].split(",")))
        print("Elapsed:", time() - start)
