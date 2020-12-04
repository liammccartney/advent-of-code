"""
Day 4
=====
Passports
"""
import re


def main(passports):
    """
    Find Valid Passports
    """
    valid = 0
    for passport in passports.split("\n\n"):
        if is_valid(passport):
            print("\n")
            print(passport)
            print("\n")
            valid += 1
    return valid


def is_valid(passport):
    """
    Valid if byr, iyr, eyr, hgt, hcl, ecl, pid, cid? are present
    """
    necessary_tokens = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    return all([x in passport for x in necessary_tokens])


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        print(main(data.read()))
