from typing import List
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """input""".splitlines(keepends=True)


def part1(input: List[str]) -> int:
    return 0


def part2(input: List[str]) -> int:
    return 0


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 0


def test_part1() -> None:
    assert part1(get_input()) == 0


def test_part2() -> None:
    assert part2(get_input()) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
