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
        memory[address] = convert_to_dec(masked_value)

    return sum(memory.values())


def part_2(program):
    """
    Does the thing, part 2
    """
    mask = None
    memory = {}
    cache = {}
    for line in program:
        if line.startswith("mask = "):
            mask = parse_mask(line)
            continue

        address, value = parse_assignment(line)
        address = int(address)
        value = int(value)

        masked_address = apply_mask_2(mask, address)
        print("Masked Address", masked_address)

        min_address = convert_to_dec(masked_address.replace("X", "0"))
        print("Min Address", min_address)
        max_address = convert_to_dec(masked_address.replace("X", "1"))
        print("Max Address", max_address)
        all_addresses = []

        for address_to_set in range(min_address, max_address + 1):
            address_bin = cache.get(address_to_set)

            if address_bin is None:
                address_bin = left_pad(convert_to_bin(address_to_set), 36)
                cache[address_to_set] = address_bin

            if any(
                masked_address[i] != "X" and masked_address[i] != aaa
                for i, aaa in enumerate(address_bin)
            ):
                continue

            memory[address_to_set] = value

    return sum(memory.values())


def assign_masked_address(address, value, memory, seen):
    """
    Recursively assign to all resolved addresses
    """
    if any(n == "X" for n in address):
        for i, n in enumerate(address):
            if n == "X":
                new_address = address[0:i] + ["0"] + address[i + 1 :]

                if "".join(new_address) in seen:
                    continue
                assign_masked_address(new_address, value, memory, seen)

                new_address = address[0:i] + ["1"] + address[i + 1 :]
                if "".join(new_address) in seen:
                    continue
                assign_masked_address(new_address, value, memory, seen)

    else:
        seen.add("".join(address))
        memory[convert_to_dec("".join(address))] = value


def apply_mask(mask, n):
    """
    Mask number
    """
    n_bin = convert_to_bin(n)
    n_bin_padded = [digit for digit in left_pad(n_bin, 36)]

    for i, p in enumerate(mask):
        if p == "X":
            continue
        n_bin_padded[i] = p

    return "".join(n_bin_padded)


def apply_mask_2(mask, n):
    """
    Mask number, with floating values
    """
    n_bin = convert_to_bin(n)
    n_bin_padded = [digit for digit in left_pad(n_bin, 36)]

    for i, p in enumerate(mask):
        if p != "0":
            n_bin_padded[i] = p

    return "".join(n_bin_padded)


def left_pad(n, length):
    """
    I hope I don't break NPM
    """
    while len(n) < length:
        n = "0" + n
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


def convert_to_bin(n):
    """
    convert to binary
    """

    def helper(n, acc):
        q = n // 2
        r = n % 2
        acc = [r] + acc
        if q == 0:
            return "".join(str(x) for x in acc)

        return helper(q, acc)

    return helper(n, [])


def convert_to_dec(b):
    """
    convert to decimal
    """
    return sum(int(x) * pow(2, i) for i, x in enumerate(reversed(b)))


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = dataset.read().splitlines()

        # print("Part 1:", part_1(dataset))
        print("Part 2:", part_2(dataset))
