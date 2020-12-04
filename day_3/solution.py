"""
Day 3
Tobogganing
"""


def main(field):
    """
    Fin
    """
    trees = 0
    x = 0
    for row in field:
        if row[x] == "#":
            trees += 1

        if x + 3 > len(row) - 1:
            x = (x + 3) - len(row)
        else:
            x += 3

    return trees


if __name__ == "__main__":
    with open("input.txt", "r") as field_data:
        print(main(field_data.read().splitlines()))
