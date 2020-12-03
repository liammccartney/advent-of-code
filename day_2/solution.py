import re


def part_1(policy_and_passwords_list):
    valid = 0
    for policy_and_password in policy_and_passwords_list:
        pattern = re.compile(
            r"^(?P<min>\d+)-(?P<max>\d+) (?P<letter>[a-z]{1}): (?P<pw>[a-z]+)$"
        )
        match = re.match(pattern, policy_and_password)

        (letter, min_count, max_count, password) = (
            match.group("letter"),
            match.group("min"),
            match.group("max"),
            match.group("pw"),
        )

        if is_password_valid(min_count, max_count, letter, password):
            valid += 1

    return valid


def is_password_valid(min_count, max_count, letter, password):
    return int(min_count) <= len([x for x in password if x == letter]) <= int(max_count)


if __name__ == "__main__":
    with open("input.txt", "r") as passwords:
        policy_and_passwords_list = passwords.readlines()
        print(part_1(policy_and_passwords_list))
