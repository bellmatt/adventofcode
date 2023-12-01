from typing import List
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw""".splitlines(
        keepends=True
    )


def calculate_priority(char: str) -> int:
    """Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    Uses `ord` to get the ascii ordinal for the character
    """
    ordinal = ord(char)
    # Handle upper case
    if ord("A") <= ordinal <= ord("Z"):
        priority = ordinal - ord("A")
        return priority + 26 + 1
    elif ord("a") <= ordinal <= ord("z"):
        return ordinal - ord("a") + 1
    raise Exception(f"char: {char}")


def part1(input: List[str]) -> int:
    sum_priorities = 0
    for line in input:
        compartment1 = line[: len(line) // 2]
        compartment2 = line[len(line) // 2 :]
        for item in compartment2:
            if item in compartment1:
                sum_priorities += calculate_priority(item)
                # make sure not to count the same item if it appears multiple times
                break
    return sum_priorities


def part2(input: List[str]) -> int:
    """Take every 3rd line, check every char to see if it appears in both the next 2 lines,
    then break if one is found and calculate its priority
    """
    sum_priorities = 0
    for i in range(0, len(input), 3):
        for char in input[i]:
            if char in input[i + 1] and char in input[i + 2]:
                sum_priorities += calculate_priority(char)
                break
    return sum_priorities


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 157


def test_example2(example: List[str]) -> None:
    assert part2(example) == 70


def test_part1() -> None:
    assert part1(get_input()) == 7917


def test_part2() -> None:
    assert part2(get_input()) == 2585


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
