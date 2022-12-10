from typing import List, Tuple
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines(
        keepends=True
    )


@pytest.fixture
def example2() -> List[str]:
    return """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20""".splitlines(
        keepends=True
    )


def part1(input: List[str]) -> int:
    start: Tuple[int, int] = (0, 4)
    tail_visited: List[Tuple[int, int]] = [start]
    head_pos: Tuple[int, int] = start
    tail_pos: Tuple[int, int] = start
    for line in input:
        direction, amount = line.strip().split(" ")
        i = int(amount)
        while i > 0:
            # Move head
            if direction == "R":
                head_pos = (head_pos[0] + 1, head_pos[1])
            elif direction == "L":
                head_pos = (head_pos[0] - 1, head_pos[1])
            elif direction == "D":
                head_pos = (head_pos[0], head_pos[1] + 1)
            elif direction == "U":
                head_pos = (head_pos[0], head_pos[1] - 1)
            # Update tail
            if tail_pos[0] - head_pos[0] >= 2:
                tail_pos = (tail_pos[0] - 1, tail_pos[1])
                if tail_pos[1] != head_pos[1]:
                    tail_pos = (tail_pos[0], head_pos[1])
            if tail_pos[0] - head_pos[0] <= -2:
                tail_pos = (tail_pos[0] + 1, tail_pos[1])
                if tail_pos[1] != head_pos[1]:
                    tail_pos = (tail_pos[0], head_pos[1])
            if tail_pos[1] - head_pos[1] >= 2:
                tail_pos = (tail_pos[0], tail_pos[1] - 1)
                if tail_pos[0] != head_pos[0]:
                    tail_pos = (head_pos[0], tail_pos[1])
            if tail_pos[1] - head_pos[1] <= -2:
                tail_pos = (tail_pos[0], tail_pos[1] + 1)
                if tail_pos[1] != head_pos[1]:
                    tail_pos = (head_pos[0], tail_pos[1])
            tail_visited.append(tail_pos)
            i -= 1
    return len(set(tail_visited))


def part2(input: List[str]) -> int:
    start: Tuple[int, int] = (11, 15)
    knot_positions: List[Tuple[int, int]] = [start] * 10
    tail_visited: List[Tuple[int, int]] = [start]
    for line in input:
        direction, amount = line.strip().split(" ")
        i = int(amount)
        while i > 0:
            for pos, knot_pos in enumerate(knot_positions):
                # Move head first
                if pos == 0:
                    if direction == "R":
                        knot_positions[pos] = (knot_pos[0] + 1, knot_pos[1])
                    elif direction == "L":
                        knot_positions[pos] = (knot_pos[0] - 1, knot_pos[1])
                    elif direction == "D":
                        knot_positions[pos] = (knot_pos[0], knot_pos[1] + 1)
                    elif direction == "U":
                        knot_positions[pos] = (knot_pos[0], knot_pos[1] - 1)
                else:
                    # Update all other following knots
                    # tail is >2 right of head
                    if knot_positions[pos][0] - knot_positions[pos - 1][0] >= 2:
                        knot_positions[pos] = (
                            knot_positions[pos][0] - 1,
                            knot_positions[pos][1],
                        )
                        if knot_positions[pos][1] < knot_positions[pos - 1][1]:
                            knot_positions[pos] = (
                                knot_positions[pos][0],
                                knot_positions[pos][1] + 1,
                            )
                        elif knot_positions[pos][1] > knot_positions[pos - 1][1]:
                            knot_positions[pos] = (
                                knot_positions[pos][0],
                                knot_positions[pos][1] - 1,
                            )

                    # tail is >2 left of head
                    if knot_positions[pos][0] - knot_positions[pos - 1][0] <= -2:
                        knot_positions[pos] = (
                            knot_positions[pos][0] + 1,
                            knot_positions[pos][1],
                        )
                        if knot_positions[pos][1] > knot_positions[pos - 1][1]:
                            knot_positions[pos] = (
                                knot_positions[pos][0],
                                knot_positions[pos][1] - 1,
                            )
                        elif knot_positions[pos][1] < knot_positions[pos - 1][1]:
                            knot_positions[pos] = (
                                knot_positions[pos][0],
                                knot_positions[pos][1] + 1,
                            )

                    # tail is >2 down from head
                    if knot_positions[pos][1] - knot_positions[pos - 1][1] >= 2:
                        knot_positions[pos] = (
                            knot_positions[pos][0],
                            knot_positions[pos][1] - 1,
                        )
                        if knot_positions[pos][0] > knot_positions[pos - 1][0]:
                            knot_positions[pos] = (
                                knot_positions[pos][0] - 1,
                                knot_positions[pos][1],
                            )
                        elif knot_positions[pos][0] < knot_positions[pos - 1][0]:
                            knot_positions[pos] = (
                                knot_positions[pos][0] + 1,
                                knot_positions[pos][1],
                            )

                    # tail is >2 up from head
                    if knot_positions[pos][1] - knot_positions[pos - 1][1] <= -2:
                        knot_positions[pos] = (
                            knot_positions[pos][0],
                            knot_positions[pos][1] + 1,
                        )
                        if knot_positions[pos][0] > knot_positions[pos - 1][0]:
                            knot_positions[pos] = (
                                knot_positions[pos][0] - 1,
                                knot_positions[pos][1],
                            )
                        elif knot_positions[pos][0] < knot_positions[pos - 1][0]:
                            knot_positions[pos] = (
                                knot_positions[pos][0] + 1,
                                knot_positions[pos][1],
                            )
                    if pos == 9:
                        tail_visited.append(knot_positions[pos])
            i -= 1
    print_map(tail_visited, visited=True)
    return len(set(tail_visited))


def print_map(input: List[Tuple[int, int]], visited: bool = False) -> None:
    print("map:")
    for x in range(0, 27):
        for y in range(0, 20):
            if visited:
                if y == 11 and x == 15:
                    print("s", end=" ")
                if (y, x) in input:
                    print("#", end=" ")
                else:
                    print(".", end=" ")
                continue

            if (y, x) == input[0]:
                print("H", end=" ")
            elif (y, x) in input[: len(input) - 1]:
                index = input.index((y, x))
                print(f"{index}", end=" ")
            elif (y, x) == input[-1]:
                print("T", end=" ")
            elif y == 11 and x == 15:
                print("s", end=" ")
            else:
                print(".", end=" ")
        print("")
    print("---")


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 13
    assert part2(example) == 1


def test_example2(example2: List[str]) -> None:
    assert part2(example2) == 36


def test_part1() -> None:
    assert part1(get_input()) == 6357


def test_part2() -> None:
    assert part2(get_input()) == 2627


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
