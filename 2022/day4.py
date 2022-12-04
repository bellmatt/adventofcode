from typing import List, Sequence
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".splitlines(
        keepends=True
    )


def assignment_range(assigment: str) -> Sequence[int]:
    range_start, range_end = assigment.split("-")
    return range(int(range_start), int(range_end) + 1)


def part1(input: List[str]) -> int:
    count = 0
    for line in input:
        assignment1, assignment2 = line.strip().split(",")
        assignment1_set = set(assignment_range(assignment1))
        assignment2_set = set(assignment_range(assignment2))
        if assignment1_set.issubset(assignment2_set):
            count += 1
        elif assignment2_set.issubset(assignment1_set):
            count += 1
    return count


def part2(input: List[str]) -> int:
    count = 0
    for line in input:
        assignment1, assignment2 = line.strip().split(",")
        assignment1_set = set(assignment_range(assignment1))
        assignment2_set = set(assignment_range(assignment2))
        if not assignment1_set.isdisjoint(assignment2_set):
            count += 1
    return count


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 2


def test_part1() -> None:
    assert part1(get_input()) == 464


def test_part2() -> None:
    assert part2(get_input()) == 770


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
