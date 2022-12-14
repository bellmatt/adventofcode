from typing import List, Tuple
import pytest
import os

SAND_START = (500, 0)


@pytest.fixture
def example() -> List[str]:
    return """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9""".splitlines(
        keepends=True
    )


class Position:
    material: str
    x: int
    y: int

    def __init__(self, x: int, y: int, material: str) -> None:
        self.x = x
        self.y = y
        self.material = material

    def __repr__(self) -> str:
        if self.material == "rock":
            return "#"
        if self.material == "air":
            return "."
        if self.material == "sand":
            return "o"
        return "?"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return other.x == self.x and other.y == self.y


def print_map(input: List[List[Position]]) -> None:
    print("map:")
    for y in range(len(input[0])):
        print(y, end="")
        for x in range(len(input)):
            print(input[x][y], end="")
        print("")
    print("---")


def part1(input: List[str], add_floor: bool = False) -> int:
    grid: List[List[Position]] = []
    x_offset = 0
    max_x = 700
    max_y = 175
    highest_y = 0
    # Fill the grid with air
    for i in range(x_offset, max_x):
        grid.append([])
        for j in range(0, max_y):
            grid[i - x_offset].append(Position(i, j, "air"))

    for line in input:
        points = line.strip().split(" -> ")
        for index, point in enumerate(points):
            if index < len(points) - 1:
                # If x is the same, plot the y points
                this_point: Tuple[int, int] = eval(point)
                next_point = eval(points[index + 1])
                if point[0] == next_point[0]:
                    if point[1] < next_point[1]:
                        for i in range(this_point[1], next_point[1] + 1):
                            grid[this_point[0] - x_offset][i].material = "rock"
                            if i > highest_y:
                                highest_y = i
                    else:
                        for i in range(next_point[1], this_point[1] + 1):
                            grid[this_point[0] - x_offset][i].material = "rock"
                            if i > highest_y:
                                highest_y = i
                if point[1] == next_point[1]:
                    if point[0] < next_point[0]:
                        for i in range(this_point[0], next_point[0] + 1):
                            grid[i - x_offset][this_point[1]].material = "rock"
                    else:
                        for i in range(next_point[0], this_point[0] + 1):
                            grid[i - x_offset][this_point[1]].material = "rock"
                    if this_point[1] > highest_y:
                        highest_y = this_point[1]
    # Add floor:
    if add_floor:
        for i in range(x_offset, max_x):
            grid[i - x_offset][highest_y + 2].material = "rock"

    # Pour the sand
    sand = 0
    while True:
        sand_pos = SAND_START
        sand_falling = True
        while sand_falling:
            # detect when the sand falls into the abyss
            if (
                sand_pos[1] + 1 >= len(grid[0])
                or grid[SAND_START[0] - x_offset][SAND_START[1]].material == "sand"
            ):
                print_map(grid)
                print(f"Final position: {sand_pos}")
                return sand
            try:
                if grid[sand_pos[0] - x_offset][sand_pos[1] + 1].material in [
                    "rock",
                    "sand",
                ]:
                    # Check down and left
                    if grid[sand_pos[0] - x_offset - 1][sand_pos[1] + 1].material in [
                        "rock",
                        "sand",
                    ]:
                        # check down and right
                        if grid[sand_pos[0] - x_offset + 1][
                            sand_pos[1] + 1
                        ].material in ["rock", "sand"]:
                            # rest - set this pos to be sand
                            grid[sand_pos[0] - x_offset][sand_pos[1]].material = "sand"
                            sand_falling = False
                        else:
                            # Move down and right and repeat
                            sand_pos = (sand_pos[0] + 1, sand_pos[1] + 1)
                            continue
                    else:
                        # Move down and left and repeat
                        sand_pos = (sand_pos[0] - 1, sand_pos[1] + 1)
                        continue
                else:
                    # Move down and repeat
                    sand_pos = (sand_pos[0], sand_pos[1] + 1)
                    continue
            except:
                print_map(grid)
                print(f"IndexError: last sand pos: {sand_pos}")
                return -1
        sand += 1


def part2(input: List[str]) -> int:
    return part1(input, add_floor=True)


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example(example: List[str]) -> None:
    assert part1(example) == 24
    assert part2(example) == 93


def test_part1() -> None:
    assert part1(get_input()) == 885


def test_part2() -> None:
    assert part2(get_input()) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
