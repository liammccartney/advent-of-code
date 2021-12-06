def part_1(numbers, boards):
    nums_called = []
    for n in numbers:
        nums_called.append(n)

        for b in boards:
            b.play(nums_called)

            if b.is_won:
                return b.score()


def part_2(numbers, boards):
    boards_won = []
    nums_called = []

    for n in numbers:
        nums_called.append(n)
        for board in boards:
            if board.is_won:
                continue

            board.play(nums_called)

            if board.is_won:
                boards_won.append(board)

    board = boards_won[-1]
    return board.score()


class Board:
    def __init__(self, rows):
        self.is_won = False
        self.rows = rows
        self.winning_numbers = []

    def play(self, numbers):
        self.is_won = self.has_won(numbers)
        if self.is_won:
            self.winning_numbers = [n for n in numbers]
        return self

    def has_won(self, numbers):
        for i, row in enumerate(self.rows):
            col = [r[i] for r in self.rows]
            if all([r in numbers for r in row]) or all([r in numbers for r in col]):
                return True
        return False

    def unmarked(self):
        if not self.is_won:
            return []

        return [r for row in self.rows for r in row if r not in self.winning_numbers]

    def score(self):
        return sum(self.unmarked()) * self.winning_numbers[-1]

    def reset(self):
        self.winning_numbers = []
        self.is_won = False


if __name__ == "__main__":
    with open("../input/day04.txt", "r") as depths:
        data = [d.strip() for d in depths.readlines() if d != "\n"]
        numbers = [int(d) for d in data[0].split(",")]
        boards = []
        board = []

        for row in data[1:]:
            board.append([int(d) for d in row.split()])

            if len(board) == 5:
                boards.append(board)
                board = []

        boards = [Board(b) for b in boards]
        print("Part 1:", part_1(numbers, boards))

        [b.reset() for b in boards]
        print("Part 2:", part_2(numbers, boards))
