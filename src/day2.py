from dataclasses import dataclass


@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    def __init__(self, horizontal: int = 0, depth: int = 0, aim: int = 0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim


@dataclass
class Instruction:
    direction: str
    distance: int

    def __init__(self, input: str):
        self.direction, dist = input.split(" ")
        self.distance = int(dist)


def recalculate_position(position: Position, instruction_input: str) -> Position:
    """Returns an updated position after executing an instruction"""
    instruction = Instruction(instruction_input)
    if instruction.direction == "forward":
        position.horizontal = position.horizontal + instruction.distance
    if instruction.direction == "up":
        position.depth = position.depth - instruction.distance
    if instruction.direction == "down":
        position.depth = position.depth + instruction.distance
    return position


def recalculate_position_with_aim(
    position: Position, instruction_input: str
) -> Position:
    """Returns an updated position after executing an instruction"""
    instruction = Instruction(instruction_input)
    if instruction.direction == "forward":
        position.horizontal = position.horizontal + instruction.distance
        position.depth = position.depth + (position.aim * instruction.distance)
    if instruction.direction == "up":
        position.aim = position.aim - instruction.distance
    if instruction.direction == "down":
        position.aim = position.aim + instruction.distance
    return position


if __name__ == "__main__":
    lines = open("./src/day2_input.txt", "r").readlines()
    current_position = Position()
    current_position_with_aim = Position()
    for input in lines:
        current_position = recalculate_position(current_position, input)
        current_position_with_aim = recalculate_position_with_aim(
            current_position_with_aim, input
        )
    print("part 1:")
    print(f"h: {current_position.horizontal} d: {current_position.depth} ")
    print(current_position.horizontal * current_position.depth)
    print("part 2:")
    print(
        f"h: {current_position_with_aim.horizontal} d: {current_position_with_aim.depth} a: {current_position_with_aim.aim}"
    )
    print(current_position_with_aim.horizontal * current_position_with_aim.depth)
