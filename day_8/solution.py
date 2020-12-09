"""
Day 8
=====
Handheld Halting
"""


def main(data):
    """
    Does the thing
    """
    accumulator = 0
    visited = set()

    i = 0

    while i < len(data):
        if i in visited:
            return accumulator

        visited.add(i)

        instruction = data[i]
        op, arg = instruction.split(" ")

        if op == "acc":
            accumulator += int(arg)

        if op == "jmp":
            i += int(arg)
            continue

        i += 1


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        print(main(data.readlines()))
