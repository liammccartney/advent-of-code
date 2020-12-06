import re


def main(answers):
    return sum(
        [
            len(set(list(re.findall(r"[a-z]", answer_group))))
            for answer_group in answers.split("\n\n")
        ]
    )


if __name__ == "__main__":
    with open("input.txt", "r") as data:
        data = data.read()
        print(main(data))
