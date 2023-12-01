from typing import List
import sys
from pathlib import PurePath


def is_int(input: str):
    try:
        return True, int(input)
    except ValueError:
        return False, input


def process(instructions: List[str], input: List[int]) -> int:
    variables = {"w": 0, "x": 0, "y": 0, "z": 0}

    for instruction in instructions:
        print(instruction)
        if instruction[0] == "inp":
            variables[instruction[1]] = input.pop(0)
        elif is_int(instruction[2])[0]:
            value = is_int(instruction[2])[1]
            if instruction[0] == "add":
                variables[instruction[1]] = variables[instruction[1]] + value
            if instruction[0] == "mod":
                variables[instruction[1]] = variables[instruction[1]] % value
            if instruction[0] == "div":
                variables[instruction[1]] = variables[instruction[1]] // value
            if instruction[0] == "mul":
                variables[instruction[1]] = variables[instruction[1]] * value
            if instruction[0] == "eql":
                variables[instruction[1]] = (
                    1 if variables[instruction[1]] == value else 0
                )
        else:
            if instruction[0] == "add":
                variables[instruction[1]] = (
                    variables[instruction[1]] + variables[instruction[2]]
                )
            if instruction[0] == "mod":
                variables[instruction[1]] = (
                    variables[instruction[1]] % variables[instruction[2]]
                )
            if instruction[0] == "div":
                variables[instruction[1]] = (
                    variables[instruction[1]] // variables[instruction[2]]
                )
            if instruction[0] == "mul":
                variables[instruction[1]] = (
                    variables[instruction[1]] * variables[instruction[2]]
                )
            if instruction[0] == "eql":
                variables[instruction[1]] = (
                    1 if variables[instruction[1]] == variables[instruction[2]] else 0
                )

        print(variables)
    return variables["z"]


if __name__ == "__main__":
    # instructions = [ x.rstrip().split(" ") for x in open("./src/day24_input.txt", "r").readlines()]
    input = [open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readlines()]

    valid = process(input, list([int(x) for x in list("11111111111111")]))
    print(f"{'valid' if valid == 0 else 'invalid'}")
