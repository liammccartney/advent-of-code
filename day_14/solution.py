"""
Day 14
======
Docking Data
"""
import re


def part_1(program):
    """
    Does the thing
    """
    mask = None
    memory = {}
    for line in program:
        if line.startswith("mask = "):
            mask = parse_mask(line)
            continue

        address, value = parse_assignment(line)
        address = int(address)
        value = int(value)

        masked_value = apply_mask(mask, value)
        memory[address] = int(masked_value, 2)

    return sum(memory.values())


def part_2(program):
    """
    Does the thing, part 2
    """
    mask = None
    memory = {}
    for line in program:
        if line.startswith("mask = "):
            mask = parse_mask(line)
            continue

        address, value = parse_assignment(line)
        address = int(address)
        value = int(value)

        masked_address = apply_address_mask(mask, address)

        assign_masked_address(list(masked_address), value, memory)

    return sum(memory.values())


def assign_masked_address(address, value, memory):
    """
    Recursively assign to all resolved addresses
    """

    def helper(address, new_address, value, memory):
        for i, n in enumerate(address):
            if n == "X":
                helper(address[i + 1 :], new_address + ["0"], value, memory)
                helper(address[i + 1 :], new_address + ["1"], value, memory)
            else:
                new_address.append(n)

        if len(new_address) == 36 and any(x != "X" for x in new_address):
            memory[int("".join(new_address), 2)] = value

    helper(address, [], value, memory)


def apply_mask(mask, n):
    """
    Mask number
    """
    n_bin = bin(n)[2:]
    n_bin_padded = list(left_pad(n_bin, 36))

    for i, p in enumerate(mask):
        if p == "X":
            continue
        n_bin_padded[i] = p

    return "".join(n_bin_padded)


def apply_address_mask(mask, n):
    """
    Mask number, with floating values
    """
    n_bin = bin(n)[2:]
    n_bin_padded = [digit for digit in left_pad(n_bin, 36)]

    for i, p in enumerate(mask):
        if p != "0":
            n_bin_padded[i] = p

    return "".join(n_bin_padded)


def left_pad(n, length, c="0"):
    """
    I hope I don't break NPM
    """
    while len(n) < length:
        n = c + n
    return n


def parse_mask(line):
    """
    Parse out the mask
    """
    match = re.match(r"^mask = (?P<mask>[X01]{36})$", line)
    return match.group("mask")


def parse_assignment(line):
    """
    Parse out memory address and value to write
    """
    match = re.match(r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)$", line)
    return match.groups()


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()
        print("Part 1:", part_1(dataset))

    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()
        print("Part 2:", part_2(dataset))
