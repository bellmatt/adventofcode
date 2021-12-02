from typing import Tuple


def recalculate_position(current: Tuple[int, int], instruction: str) -> Tuple[int, int]:
    """Returns an updated position (horizontal position, depth) given an instruction"""
    direction, distance = instruction.split(" ")
    if direction == "forward":
        return (current[0] + int(distance), current[1])
    if direction == "up":
        return (current[0], current[1] - int(distance))
    if direction == "down":
        return (current[0], current[1] + int(distance))


def recalculate_position_with_aim(
    current: Tuple[int, int, int], instruction: str
) -> Tuple[int, int, int]:
    """Returns an updated position (horizontal position, aim, depth) given an instruction"""
    direction, distance = instruction.split(" ")
    new_position = current
    if direction == "forward":
        new_position = (
            current[0] + int(distance),
            current[1],
            current[2] + current[1] * int(distance),
        )
        return new_position
    if direction == "up":
        return (current[0], current[1] - int(distance), current[2])
    if direction == "down":
        return (current[0], current[1] + int(distance), current[2])


if __name__ == "__main__":
    lines = open("./src/day2_input.txt", "r").readlines()
    current_position = (0, 0)
    current_position_with_aim = (0, 0, 0)
    for input in lines:
        current_position = recalculate_position(current_position, input)
        current_position_with_aim = recalculate_position_with_aim(
            current_position_with_aim, input
        )
    print(current_position)
    print(current_position[0] * current_position[1])
    print(current_position_with_aim)
    print(current_position_with_aim[0] * current_position_with_aim[2])
