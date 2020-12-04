"""
Day 4
=====
Passports
"""
import re


def main(passports, is_valid):
    """
    Find Valid Passports
    """
    valid = 0
    for passport in passports.split("\n\n"):
        if is_valid(passport):
            valid += 1
    return valid


def is_valid_part_1(passport):
    """
    Valid if byr, iyr, eyr, hgt, hcl, ecl, pid, cid? are present
    """
    necessary_tokens = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
    return all([x in passport for x in necessary_tokens])


def is_valid_part_2(passport):
    """
    Valid if byr, iyr, eyr, hgt, hcl, ecl, pid, cid? are present
    """
    if not is_valid_part_1(passport):
        return False

    return all(
        [
            is_field_valid(k, v)
            for k, v in [pair.split(":") for pair in re.split(r"\s+", passport.strip())]
        ]
    )


def is_field_valid(field, value):
    """
    Is field data acceptable?
    """
    if field == "byr":
        return 1920 <= int(value) <= 2002

    if field == "iyr":
        return 2010 <= int(value) <= 2020

    if field == "eyr":
        return 2020 <= int(value) <= 2030

    if field == "hgt":
        match = re.match(r"(?P<digits>\d{2,3})(?P<units>(cm|in))", value)
        if match is None:
            return False
        digits, units = match.group("digits"), match.group("units")
        if units == "in":
            return 59 <= int(digits) <= 76
        if units == "cm":
            return 150 <= int(digits) <= 193

    if field == "hcl":
        return re.match(r"^#[a-f0-9]{6}$", value) is not None

    if field == "ecl":
        return value in [
            "amb",
            "blu",
            "brn",
            "gry",
            "grn",
            "hzl",
            "oth",
        ]
    if field == "pid":
        return re.match(r"^[0-9]{9}$", value.strip()) is not None

    if field == "cid":
        return True

    return False


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        data = data.read()
        print("Part 1:", main(data, is_valid_part_1))
        print("Part 2:", main(data, is_valid_part_2))
