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

    @property
    def height(self) -> int:
        if self.char == "S":
            return ord("a") - ord("a")
        if self.char == "E":
            return ord("z") - ord("a")
        return ord(self.char) - ord("a")

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __lt__(self, other: Position) -> bool:
        return self.f < other.f

    def __gt__(self, other: Position) -> bool:
        return self.f > other.f

    def __repr__(self) -> str:
        return f"{self.char}({self.y},{self.x})"

    @property
    def f(self) -> int:
        return self.h + self.g


def print_map(input: List[Position]) -> None:
    print("map:")
    for x in range(0, 50):
        for y in range(0, 140):
            visited = False
            for p in input:
                if p.x == x and p.y == y:
                    print(p.char, end="")
                    visited = True
            if not visited:
                print(".", end="")
        print("")
    print("---")


def astar_algo(heightmap: List[List[str]], start: Position) -> int:
    # Find the end point
    end: Optional[Position] = None
    for i, x in enumerate(heightmap):
        for j, y in enumerate(x):
            if y == "E":
                end = Position(y, i, j, None)
    # Use a heap to keep the "smallest" i.e. lowest cost route at the start of the list
    priority_queue: List[Position] = []
    heapq.heappush(priority_queue, start)
    # Positions already seen
    closed_list: List[Position] = []
    while True:
        curr_pos = heapq.heappop(priority_queue)
        closed_list.append(curr_pos)
        if curr_pos.is_end:
            path: List[Position] = []
            current = curr_pos.parent
            while current is not None:
                path.append(current)
                current = current.parent
            # print(path[::-1])
            # print_map(path)  # for debugging
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
            option.g = (
                curr_pos.g
                + (
                    ((option.x - option.parent.x) ** 2)
                    + ((option.y - option.parent.y) ** 2)
                )
                ** 0.5
            )
            option.h = (((option.x - end.x) ** 2) + ((option.y - end.y) ** 2)) ** 0.5
            # check if it's already on the queue and isn't a better route
            if option in priority_queue:
                index = priority_queue.index(option)
                if option.g > priority_queue[index].g:
                    continue
                else:
                    priority_queue.remove(option)

            # Add option for inspection next
            heapq.heappush(priority_queue, option)


def part1(input: List[str]) -> int:
    heightmap: List[List[str]] = [[char for char in line.strip()] for line in input]
    start: Optional[Position] = None
    for i, x in enumerate(heightmap):
        for j, y in enumerate(x):
            if y == "S":
                start = Position(y, i, j, None)
    if start is None:
        raise Exception("Can't find start or end point")
    return astar_algo(heightmap, start)


def part2(input: List[str]) -> int:
    heightmap: List[List[str]] = [[char for char in line.strip()] for line in input]
    start: Optional[Position] = None
    results = []
    for i, x in enumerate(heightmap):
        for j, y in enumerate(x):
            # can only start in the first row
            if j == 0 and y == "S":
                heightmap[i][j] = "a"
                y = "a"
            if j == 0 and y == "a":
                start = Position(y, i, j, None)
                try:
                    result = astar_algo(heightmap, start)
                # Protect against a's that are dead ends
                except IndexError:
                    continue
                results.append(result)
                print(f"{start}: steps = {result}")
    return min(results)


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 31
    assert part2(example) == 29


def test_part1() -> None:
    assert part1(get_input()) == 449


def test_part2() -> None:
    assert part2(get_input()) == 443


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
