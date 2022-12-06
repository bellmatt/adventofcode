import pytest
import os


@pytest.fixture
def example() -> str:
    return "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


@pytest.fixture
def example2() -> str:
    return "bvwbjplbgvbhsrlpgdmjqwftvncz"


@pytest.fixture
def example3() -> str:
    return "nppdvjthqldpwncqszvftbrmjlhg"


@pytest.fixture
def example4() -> str:
    return "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"


@pytest.fixture
def example5() -> str:
    return "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"


def part1(input: str) -> int:
    for i in range(3, len(input)):
        chars = input[i - 3 : i + 1]
        if len(set(chars)) == len(chars):
            return i + 1
    raise Exception("No sequence found")


def part2(input: str) -> int:
    for i in range(13, len(input)):
        chars = input[i - 13 : i + 1]
        if len(set(chars)) == len(chars):
            return i + 1
    raise Exception("No sequence found")


def get_input() -> str:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readline().strip()


def test_examples(
    example: str, example2: str, example3: str, example4: str, example5: str
) -> None:
    assert part1(example) == 7
    assert part1(example2) == 5
    assert part1(example3) == 6
    assert part1(example4) == 10
    assert part1(example5) == 11

    assert part2(example) == 19
    assert part2(example2) == 23
    assert part2(example3) == 23
    assert part2(example4) == 29
    assert part2(example5) == 26


def test_part1() -> None:
    assert part1(get_input()) == 1920


def test_part2() -> None:
    assert part2(get_input()) == 2334


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
