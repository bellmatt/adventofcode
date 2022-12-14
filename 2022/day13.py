from typing import List, Tuple, Union, Any
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]""".splitlines(
        keepends=True
    )


def compare(left: Union[List[Any], int], right: Union[List[Any], int]) -> int:
    print(f"- Compare {left} vs {right}")
    correct = False
    if isinstance(left, int) and isinstance(right, int):
        if int(left) < int(right):
            return 1
        elif int(left) > int(right):
            return -1
        else:
            return 0
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    #   correct = compare(left,right)
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
    #    correct = compare(left,right)
    if isinstance(left, list) and isinstance(right, list):
        for x in range(max(len(left), len(right))):
            if x >= len(left):
                print("  - Left side ran out of items")
                return 1
            elif x >= len(right):
                print("  - Right side ran out of items")
                return -1

            result = compare(left[x], right[x])
            if result == 1:
                return 1
            if result == -1:
                return -1
    return correct


def part1(input: List[str]) -> int:
    input = [line.strip() for line in input if line.strip() != ""]
    pairs: List[Tuple[List[Any], List[Any]]] = []
    for i in range(0, len(input), 2):
        pairs.append((eval(input[i]), eval(input[i + 1])))
    total = 0
    for i, pair in enumerate(pairs):
        correct_order = compare(pair[0], pair[1])
        print(f"Inputs are {'not ' if correct_order == -1 else ''}in the right order")
        total += i + 1 if correct_order == 1 else 0
        print(f"Total: {total}")
    return total


def part2(input: List[str]) -> int:
    return 0


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example(example: List[str]) -> None:
    assert part1(example) == 13
    assert part2(example) == 140


def test_part1() -> None:
    assert part1(get_input()) == 4894


def test_part2() -> None:
    assert part2(get_input()) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
