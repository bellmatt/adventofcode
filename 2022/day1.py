from typing import List
import pytest
import os
from collections import Counter


@pytest.fixture
def example() -> List[str]:
    return """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".splitlines(
        keepends=True
    )


def elf_calories(input: List[str]) -> List[int]:
    elves = []
    current_elf_sum = 0
    for line in input:
        current_elf_sum += int(line) if line != "\n" else 0
        if line == "\n":
            # New elf
            elves.append(current_elf_sum)
            current_elf_sum = 0
    elves.append(current_elf_sum)
    return elves


def part1(input: List[str]) -> int:
    return max(elf_calories(input))


def part2(input: List[str]) -> int:
    elves = elf_calories(input)
    return sum(sorted(elves, reverse=True)[0:3])


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 24000


def test_example2(example: List[str]) -> None:
    assert part2(example) == 45000


def test_part1() -> None:
    assert part1(get_input()) == 70116


def test_part2() -> None:
    assert part2(get_input()) == 206582


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
