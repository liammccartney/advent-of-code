"""
Day 9
=====
Encoding Error
"""


def main(data, preamble_size):
    """
    Find number in data set that is not the sum of any of the
    preceding number within bounds of a given preamble
    """
    for i, number in enumerate(data[preamble_size:]):
        preamble = data[i : preamble_size + i]
        if all([number - p not in preamble for p in preamble]):
            return number

    return None


def break_encryption(data, target_sum):
    """
    Finds a contiguous string of numbers in the data set that sum up
    to the invalid number
    """

    def find_sums(data, total):
        contiguous = []
        for number in data:
            contiguous.append(number)
            if sum(contiguous) == total:
                return contiguous

        return find_sums(data[1:], total)

    contiguous = find_sums(data, target_sum)
    return min(contiguous) + max(contiguous)


if __name__ == "__main__":
    with open("input.txt", "r") as dataset:
        dataset = [int(n) for n in dataset.read().splitlines()]

        invalid = main(dataset, 25)

        print("Part 1:", invalid)
        print("Part 2:", break_encryption(dataset, invalid))
