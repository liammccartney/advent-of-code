"""
Day 13
======
Shuttle Search
"""


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


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()
        filtered_schedule = [int(t) for t in dataset[1].split(",") if t != "x"]
        print("Part 1:", part_1(int(dataset[0]), filtered_schedule))
