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
        instruction = data[i].strip()
        op, arg = instruction.split(" ")

        if i in visited:
            raise ValueError("Looped")

        visited.add(i)

        if op == "acc":
            accumulator += int(arg)

        if op == "jmp":
            i += int(arg)
            continue

        i += 1
    return accumulator


def fix_program(data):
    for i in range(0, len(data)):
        head = data[0:i]
        tail = data[(i + 1) :]
        instruction = data[i]

        if "jmp" in instruction:
            new_instruction = instruction.replace("jmp", "nop")
        elif "nop" in instruction:
            new_instruction = instruction.replace("nop", "jmp")
        else:
            continue

        try:
            return main(head + [new_instruction] + tail)
        except ValueError:
            continue


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        data = data.read().splitlines()
        print(fix_program(data))
