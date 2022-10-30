from pathlib import PurePath
import sys
from typing import List
from copy import deepcopy


def print_map(input: List[List[str]]) -> None:
    lit = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end="")
            lit += 1 if input[i][j] == "#" else 0
        print()
    print(lit)


def enhance(input: List[List[str]], algo: List[str], repeat: int) -> List[List[str]]:

    neighbour_pixels = [
        [-1, -1],
        [-1, 0],
        [-1, 1],
        [0, -1],
        [0, 0],
        [0, 1],
        [1, -1],
        [1, 0],
        [1, 1],
    ]
    background = "0"
    while repeat > 0:
        output = [
            ["." for _ in range(len(input) + 2)] for _ in range(len(input[0]) + 2)
        ]
        print(f"{len(input)}x{len(input[0])} -> {len(output)}x{len(output[0])}")
        for i in range(-1, len(input) + 1):
            for j in range(-1, len(input[0]) + 1):
                binary = ""
                for pixel in neighbour_pixels:
                    if (
                        i + pixel[0] >= 0
                        and i + pixel[0] < len(input)
                        and j + pixel[1] >= 0
                        and j + pixel[1] < len(input[0])
                    ):
                        binary += (
                            "0" if input[i + pixel[0]][j + pixel[1]] == "." else "1"
                        )
                    else:
                        binary += background
                value = int(binary, 2)
                output_value = algo[value]
                output[i + 1][j + 1] = output_value

        background = "0" if algo[int(background * 9, 2)] == "." else "1"
        input = deepcopy(output)
        repeat -= 1
        # print_map(input)
        print(sum([line.count("#") for line in input]))


if __name__ == "__main__":
    algo = list(
        open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readline().rstrip()
    )
    image = [
        list(line.rstrip())
        for line in open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readlines()[2:]
    ]

    # Part 1
    enhance(image, algo, 2)
    # Part 2
    enhance(image, algo, 50)
