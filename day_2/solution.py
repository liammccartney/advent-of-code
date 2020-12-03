"""
Day 2
=====
Passwords & Policies
"""
import re


def main(policy_and_passwords_list, validity_function):
    """
    Does the thing
    """
    valid = 0
    for policy_and_password in policy_and_passwords_list:
        (letter, digit1, digit2, password) = extract_policy_and_password(
            policy_and_password
        )
        if validity_function(digit1, digit2, letter, password):
            valid += 1

    return valid


def password_is_valid_part_1(min_count, max_count, letter, password):
    """
    Part 1
    Validity Determined by Letter Count
    """
    return int(min_count) <= len([x for x in password if x == letter]) <= int(max_count)


def password_is_valid_part_2(pos_1, pos_2, letter, password):
    """
    Part 2
    Validity Determined by Letter Position
    """
    idx_1 = int(pos_1) - 1
    idx_2 = int(pos_2) - 1
    letter_1 = password[idx_1]
    letter_2 = password[idx_2]

    return (letter_1 is letter or letter_2 is letter) and (letter_1 is not letter_2)


def extract_policy_and_password(policy_and_password):
    """
    Extracting letter, digits, and password from input data
    """
    pattern = re.compile(
        r"^(?P<digit1>\d+)-(?P<digit2>\d+) (?P<letter>[a-z]{1}): (?P<pw>[a-z]+)$"
    )

    match = re.match(pattern, policy_and_password)

    return (
        match.group("letter"),
        match.group("digit1"),
        match.group("digit2"),
        match.group("pw"),
    )


if __name__ == "__main__":
    with open("input.txt", "r") as input_data:
        input_data = input_data.readlines()
        print("Part 1:", main(input_data, password_is_valid_part_1))
        print("Part 2:", main(input_data, password_is_valid_part_2))
