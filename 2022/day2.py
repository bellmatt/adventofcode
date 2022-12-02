from typing import List
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """A Y
B X
C Z""".splitlines(
        keepends=True
    )


@pytest.fixture
def example2() -> List[str]:
    return """A X
B X
C X
A Y
B Y
C Y
A Z
B Z
C Z
""".splitlines(
        keepends=True
    )


def lookup_score(moves: str) -> int:
    # A/X = Rock
    # B/Y = Paper
    # C/Z = Scissors

    if moves == "A X":
        return 4
    if moves == "A Y":
        return 8
    if moves == "A Z":
        return 3
    if moves == "B X":
        return 1
    if moves == "B Y":
        return 5
    if moves == "B Z":
        return 9
    if moves == "C X":
        return 7
    if moves == "C Y":
        return 2
    if moves == "C Z":
        return 6
    raise Exception(f"unknown move: {moves}")


def part1(input: List[str]) -> int:
    total_score = 0
    for line in input:
        score = lookup_score(line.strip())
        total_score += score
    return total_score


def lookup_required_move_score(moves: str) -> int:
    # A/X = Rock, need to lose
    # B/Y = Paper, need to draw
    # C/Z = Scissors, need to win

    if moves == "A X":
        # scissors
        return 3
    if moves == "A Y":
        # rock
        return 4
    if moves == "A Z":
        # paper
        return 8
    if moves == "B X":
        # rock
        return 1
    if moves == "B Y":
        # paper
        return 5
    if moves == "B Z":
        # scissors
        return 9
    if moves == "C X":
        # paper
        return 2
    if moves == "C Y":
        # scissors
        return 6
    if moves == "C Z":
        # rock
        return 7
    raise Exception(f"unknown move: {moves}")


def part2(input: List[str]) -> int:
    total_score = 0
    for line in input:
        score = lookup_required_move_score(line.strip())
        total_score += score
    return total_score


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 15


def test_example2(example2: List[str]) -> None:
    assert part1(example2) == 45


def test_part1() -> None:
    assert part1(get_input()) == 9651


def test_part2() -> None:
    assert part2(get_input()) == 10560


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
