import re


def part_1(answers):
    return sum(
        [
            len(set(list(re.findall(r"[a-z]", answer_group))))
            for answer_group in answers.split("\n\n")
        ]
    )


def part_2(answers):
    total = 0
    for answer_group in answers.split("\n\n"):
        person_answers = answer_group.split("\n")
        person_1 = set(person_answers[0])
        total += len(count_all_answered(person_answers[1:], person_1))

    return total


def count_all_answered(answer_group, answer_set):
    if len(answer_group) == 0:
        return answer_set

    return count_all_answered(
        answer_group[1:], answer_set.intersection(set(answer_group[0]))
    )


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        data = data.read()
        print("Part 1:", part_1(data))
        print("Part 2:", part_2(data))
