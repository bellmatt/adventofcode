from typing import List
import pytest
import os


@pytest.fixture
def example() -> List[List[int]]:
    return [
        [int(char) for char in line.strip()]
        for line in """30373
25512
65332
33549
35390""".splitlines(
            keepends=True
        )
    ]


def part1(input: List[List[int]]) -> int:
    visible = []
    for x in range(0, len(input)):
        for y, height in enumerate(input[x]):
            is_visible = False
            # Edges
            if x == 0 or y == 0 or x == len(input) - 1 or y == len(input[x]) - 1:
                if (x, y) not in visible:
                    visible.append((x, y))
                continue
            # Inside
            # look left
            i = y
            checked = []
            while height > input[x][i - 1]:
                checked.append(input[x][i - 1])
                i -= 1
                if i == 0:
                    visible.append((x, y))
                    print(f"{height} is visible {x},{y} left. Checked {checked}")
                    is_visible = True
                    break
            if is_visible:
                continue
            # look right
            i = y
            checked = []
            while height > input[x][i + 1]:
                checked.append(input[x][i + 1])
                i += 1
                if i == len(input[0]) - 1:
                    print(f"{height} is visible {x},{y} right. Checked {checked}")
                    visible.append((x, y))
                    is_visible = True
                    break
            if is_visible:
                continue
            # look up
            i = x
            checked = []
            while height > input[i - 1][y]:
                checked.append(input[i - 1][y])
                i -= 1
                if i == 0:
                    print(f"{height} is visible {x},{y} up. Checked {checked}")
                    visible.append((x, y))
                    is_visible = True
                    break
            if is_visible:
                continue
            # look down
            i = x
            checked = []
            while height > input[i + 1][y]:
                checked.append(input[i + 1][y])
                i += 1
                if i == len(input) - 1:
                    print(f"{height} is visible {x},{y} down. Checked {checked}")
                    visible.append((x, y))
                    is_visible = True
                    break

    return len(visible)


def part2(input: List[List[int]]) -> int:
    highest_scenic_score = 0
    for x in range(0, len(input)):
        for y, height in enumerate(input[x]):
            up_visible = 1 if x > 0 else 0
            down_visible = 1 if x < len(input) - 1 else 0
            right_visible = 1 if y < len(input) - 1 else 0
            left_visible = 1 if y > 0 else 0
            # look left
            i = y
            while i > 1 and height > input[x][i - 1]:
                left_visible += 1
                i -= 1
            # look right
            i = y
            while i < len(input[0]) - 2 and height > input[x][i + 1]:
                i += 1
                right_visible += 1
            # look up
            i = x
            while i > 1 and height > input[i - 1][y]:
                i -= 1
                up_visible += 1
            # look down
            i = x
            while i < len(input) - 2 and height > input[i + 1][y]:
                i += 1
                down_visible += 1
            scenic_score = up_visible * down_visible * right_visible * left_visible
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score

    return highest_scenic_score


def get_input() -> List[List[int]]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return [
        [int(char) for char in line.strip()]
        for line in open(base + ".txt", "r").readlines()
    ]


def test_example1(example: List[List[int]]) -> None:
    assert part1(example) == 21
    assert part2(example) == 8


def test_part1() -> None:
    assert part1(get_input()) == 1538


def test_part2() -> None:
    assert part2(get_input()) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
