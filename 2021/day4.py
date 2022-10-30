from dataclasses import dataclass
from pathlib import PurePath
import sys
from typing import List


@dataclass
class Position:
    number: int
    marked: bool = False

    def __init__(self, num: int):
        self.number = num


@dataclass
class Board:
    numbers: List[List[Position]]
    id: int

    def __init__(self, input: List[List[str]], id: int):
        self.numbers = input
        self.id = id
        i = 0
        while i < len(input):
            self.numbers[i] = input[i]
            j = 0
            while j < len(input[i]):
                self.numbers[i][j] = Position(int(input[i][j]))
                j += 1
            i += 1

    def mark(self, number: str):
        """Mark all occurrences of number on the board. return true if at least one number marked"""
        i = 0
        ret = False
        while i < len(self.numbers):
            j = 0
            while j < len(self.numbers[i]):
                if self.numbers[i][j].number == int(number):
                    self.numbers[i][j].marked = True
                    ret = True
                j += 1
            i += 1
        return ret

    def is_winner(self) -> bool:
        row_marked = 0
        col_marked = 0

        all_numbers_on_board = sum(self.numbers, [])
        max_row_marked = 0
        max_col_marked = 0
        # check rows
        for i in range(0, len(all_numbers_on_board), 5):
            for j in range(i, i + 5, 1):
                if all_numbers_on_board[j].marked:
                    row_marked += 1
            if row_marked > max_row_marked:
                max_row_marked = row_marked
                row_marked = 0
            else:
                row_marked = 0
        # check columns
        for i in range(0, len(all_numbers_on_board), 1):
            for j in range(i, 25, 5):
                if all_numbers_on_board[j].marked:
                    col_marked += 1
            if col_marked > max_col_marked:
                max_col_marked = col_marked
                col_marked = 0
            else:
                col_marked = 0

        return max_row_marked == 5 or max_col_marked == 5

    def print(self):
        i = 0
        while i < len(self.numbers):
            j = 0
            while j < len(self.numbers[i]):
                j += 1
            i += 1

    def calculate_unmarked_sum(self) -> int:
        i = 0
        sum = 0
        found = []
        while i < len(self.numbers):
            j = 0
            while j < len(self.numbers[i]):
                if not self.numbers[i][j].marked:
                    sum += self.numbers[i][j].number
                    found.append(self.numbers[i][j].number)
                j += 1
            i += 1
        return sum


def create_boards(row_list: List[List[str]], num_rows: int) -> List[Board]:
    boards = []
    i = 0
    while i < len(row_list):
        boards.append(Board(row_list[i : i + num_rows], int(i / 5) if i > 0 else 0))
        i += num_rows
    return boards


def play_bingo(boards: List[Board], random_numbers: List[int]):
    winners = []
    for i in random_numbers:
        j = 0
        while j < len(boards):
            boards[j].mark(i)
            if boards[j].is_winner():
                winners.append((boards[j], i, boards[j].calculate_unmarked_sum()))
                del boards[j]
            else:
                j += 1
    l = len(winners)
    if l > 0:
        print(
            f"First winner (part 1): Board {winners[0][0].id} on num {winners[0][1]} with unmarked sum {int(winners[0][2])} = {int(winners[0][1])*int(winners[0][2])}"
        )
        print(
            f"Last winner (part 2): Board {winners[l-1][0].id} on num {winners[l-1][1]} with unmarked sum {int(winners[l-1][2])} = {int(winners[l-1][1])*int(winners[l-1][2])}"
        )


if __name__ == "__main__":
    input = open(PurePath(sys.argv[0]).with_suffix(".txt"), "r")
    random_numbers = input.readline().rstrip().split(",")
    lines = input.readlines()[1:]

    rows = [s.rstrip().split() for s in lines if len(s) > 0]
    rows = [r for r in rows if len(r) > 0]
    boards = create_boards(rows, 5)
    play_bingo(boards, random_numbers)
