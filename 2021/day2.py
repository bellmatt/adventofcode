from dataclasses import dataclass
from pathlib import PurePath
import sys
from typing import Optional


@dataclass
class Position:
    """Class that represents a Position"""

    horizontal: int = 0
    depth: int = 0
    # Aim is used in part 2 and changes how depth gets updated
    aim: int = None
    use_aim: bool = False

    def __init__(self, horizontal: int, depth: int, aim: Optional[int] = None):
        self.horizontal = horizontal
        self.depth = depth
        if aim is not None:
            self.use_aim = True
            self.aim = aim

    def forward(self, distance: int):
        self.horizontal += distance
        if self.use_aim:
            self.depth += self.aim * distance

    def down(self, distance: int):
        if self.use_aim:
            self.aim += distance
        else:
            self.depth += distance

    def up(self, distance: int):
        if self.use_aim:
            self.aim -= distance
        else:
            self.depth -= distance


def recalculate_position(position: Position, instruction_input: str) -> Position:
    """Returns an updated position after executing an instruction"""
    direction, distance = instruction_input.split(" ")
    # Call the relevant function on the dataclass with the provided distance
    getattr(position, direction)(int(distance))


if __name__ == "__main__":
    lines = open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readlines()
    current_position = Position(0, 0)
    current_position_with_aim = Position(0, 0, 0)
    for input in lines:
        # Part 1:
        recalculate_position(current_position, input)
        # Part 2:
        recalculate_position(current_position_with_aim, input)
    print("part 1:")
    print(current_position.horizontal * current_position.depth)
    print("part 2:")
    print(current_position_with_aim.horizontal * current_position_with_aim.depth)
