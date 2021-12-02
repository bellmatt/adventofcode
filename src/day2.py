from typing import Tuple


def recalculate_position(current: Tuple[int, int], instruction: str) -> Tuple[int, int]:
    direction, distance = instruction.split(" ")
    if direction == "forward":
        return (current[0] + int(distance), current[1])
    if direction == "up":
        return (current[0], current[1] - int(distance))
    if direction == "down":
        return (current[0], current[1] + int(distance))


if __name__ == "__main__":
    lines = open("./src/day2_input.txt", "r").readlines()
    current_position = (0, 0)
    for input in lines:
        current_position = recalculate_position(current_position, input)
    print(current_position)
    print(current_position[0] * current_position[1])
