"""
Day 7
=====
Luggage
"""
import re


def parse_spec(luggage_spec):
    """
    Parse the Luggage Spec into a more reasonable data structure
    """
    nested_bags = {}
    for spec in luggage_spec:
        parent, children = spec.split("contain")
        outer_bag = re.match(r"^(?P<lead_bag>\w+ \w+) bags", parent).group("lead_bag")
        inner_bags = children.split(", ")

        nested_bags[outer_bag] = []
        for bag in inner_bags:
            match = re.search(r"((?P<count>\d+) (?P<color>\w+ \w+))", bag)
            if match is None:
                continue
            nested_bags[outer_bag].append(
                {"color": match.group("color"), "count": int(match.group("count"))}
            )

    return nested_bags


def find_bags(nested_bags, target, acc):
    """
    find all bags eventually contain the target
    """
    for bag, inner_bags in nested_bags.items():
        if target in [inner["color"] for inner in inner_bags]:
            acc.add(bag)
            find_bags(nested_bags, bag, acc)
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
        contains = parse_spec(data)
        print("Part 1:", len(find_bags(contains, "shiny gold", set())))
        print("Part 2:", count_bags(contains, "shiny gold"))
