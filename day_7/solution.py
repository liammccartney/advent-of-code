"""
Day 7
=====
Luggage
"""
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)


def parse(luggage_spec):
    """
    Does the thing
    """
    contains = {}
    for spec in luggage_spec:
        lead_bag = re.match(r"^(?P<lead_bag>[a-z]+ [a-z]+) bags", spec).group(
            "lead_bag"
        )
        contains[lead_bag] = []
        inner_bags = [bag for bag in spec.split("contain")[1].split(", ")]
        for bag in inner_bags:
            match = re.search(r"((?P<count>\d+) (?P<color>[a-z]+ [a-z]+))", bag)
            if match is None:
                continue
            contains[lead_bag].append(
                {"color": match.group("color"), "count": int(match.group("count"))}
            )

    return contains


def find_bags(bag_nesting, target, acc):
    """
    find which bags contain shiny gold
    """
    for bag, inner_bags in bag_nesting.items():
        if target in [inner["color"] for inner in inner_bags]:
            acc.add(bag)
            find_bags(bag_nesting, bag, acc)
    return acc


def count_bags(bag_nesting, target):
    """
    Count Bag Nesting
    """
    return sum(
        [
            ib["count"] * (count_bags(bag_nesting, ib["color"]) + 1)
            for ib in bag_nesting[target]
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        contains = parse(data)
        print("Part 1:", len(find_bags(contains, "shiny gold", set())))
        print("Part 2:", count_bags(contains, "shiny gold"))
