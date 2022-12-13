from __future__ import annotations
from typing import List, Optional, Tuple, Dict
import pytest
import os
import heapq


@pytest.fixture
def example() -> List[str]:
    return """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines(
        keepends=True
    )


class Position:
    char: str
    x: int
    y: int
    parent: Optional[Position]
    is_start: bool = False
    is_end: bool = False
    g: int = 0
    h: int = 0

    def __init__(
        self, char: str, x: int, y: int, parent: Optional[Position] = None
    ) -> None:
        self.char = char
        self.x = x
        self.y = y
        self.is_start = char == "S"
        self.is_end = char == "E"
        self.parent = parent
        if self.is_end:
            print(f"Found end: {self.x},{self.y}")

    @property
    def height(self) -> int:
        if self.char == "S":
            return ord("a") - ord("a")
        if self.char == "E":
            return ord("z") - ord("a")
        return ord(self.char) - ord("a")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other,Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: Position) -> bool:
        return self.f < other.f

    def __gt__(self, other: Position) -> bool:
        return self.f > other.f

    def __repr__(self) -> str:
        return f"{self.char}:({self.x},{self.y})[g: {self.g}, h: {self.h}, f: {self.f}]"

    @property
    def f(self) -> int:
        return self.h + self.g


def part1(input: List[str]) -> int:
    heightmap: List[List[str]] = [[char for char in line.strip()] for line in input]
    start: Optional[Position] = None
    end: Optional[Position] = None
    for i, x in enumerate(heightmap):
        for j, y in enumerate(x):
            if y == "S":
                start = Position(y, i, j, None)
            if y == "E":
                end = Position(y, i, j, None)

    if start is None or end is None:
        raise Exception("Can't find start or end point")
    priority_queue: List[Position] = []
    # Use a heap to keep the "smallest" i.e. lowest cost route at the start of the list
    heapq.heappush(priority_queue, start)
    closed_list: List[Position] = []
    while True:
        curr_pos = heapq.heappop(priority_queue)
        closed_list.append(curr_pos)
        if curr_pos.is_end:
            path = []
            current = curr_pos.parent
            while current is not None:
                path.append(current)
                current = current.parent
            print(path[::-1])
            return len(path[::-1])  # Return reversed path
        # Populate options: Up down left right
        options: List[Position] = []
        if curr_pos.x - 1 >= 0:
            options.append(
                Position(
                    heightmap[curr_pos.x - 1][curr_pos.y],
                    curr_pos.x - 1,
                    curr_pos.y,
                    curr_pos,
                )
            )
        if curr_pos.x + 1 < len(heightmap):
            options.append(
                Position(
                    heightmap[curr_pos.x + 1][curr_pos.y],
                    curr_pos.x + 1,
                    curr_pos.y,
                    curr_pos,
                )
            )
        if curr_pos.y - 1 >= 0:
            options.append(
                Position(
                    heightmap[curr_pos.x][curr_pos.y - 1],
                    curr_pos.x,
                    curr_pos.y - 1,
                    curr_pos,
                )
            )
        if curr_pos.y + 1 < len(heightmap[curr_pos.x]):
            options.append(
                Position(
                    heightmap[curr_pos.x][curr_pos.y + 1],
                    curr_pos.x,
                    curr_pos.y + 1,
                    curr_pos,
                )
            )
        for option in options:
            # Rule out options that have been visited before, or that are too high
            if option in closed_list:
                continue
            if option.height > curr_pos.height + 1:
                continue
            # Create the f,g,h values for A* algorithm
            option.g = curr_pos.g + 1
            option.h = ((option.x - end.x) ** 2) + ((option.y - end.y) ** 2)
            # check if it's already on the queue and isn't a better route
            if (
                len(
                    [
                        node
                        for node in priority_queue
                        if option == node and option.g > node.g
                    ]
                )
                > 0
            ):
                continue
            # Add option for inspection next
            heapq.heappush(priority_queue, option)


def part2(input: List[str]) -> int:
    return 0


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 31


def test_part1() -> None:
    assert part1(get_input()) == 0  # 467 and 477 too high


def test_part2() -> None:
    assert part2(get_input()) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
