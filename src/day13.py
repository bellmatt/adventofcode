from typing import List, Tuple


def fold_over_y(input: List[List[str]], instruction: Tuple[str, int]) -> List[str]:
    input[instruction[1]] = ["-"] * len(input[instruction[1]])
    top_half = input[: instruction[1]]
    bottom_half = input[instruction[1] + 1 :]
    bottom_half.reverse()
    input = top_half
    for i, bottom in enumerate(bottom_half):
        input[i] = [
            "#" if x[0] == "#" or x[1] == "#" else "." for x in zip(input[i], bottom)
        ]
    return input


def fold_over_x(input: List[List[str]], instruction: Tuple[str, int]) -> List[str]:
    for i, line in enumerate(input):
        second_half = line[instruction[1] + 1 :]
        second_half.reverse()
        input[i] = [
            "#" if x[0] == "#" or x[1] == "#" else "."
            for x in zip(line[: instruction[1]], second_half)
        ]
    return input


def get_map_dimensions(input: List[Tuple[int, int]]) -> Tuple[int, int]:
    size_x = 0
    size_y = 0
    for coordinate in input:
        if coordinate[0] > size_x:
            size_x = coordinate[0]
        if coordinate[1] > size_y:
            size_y = coordinate[1]
    return (size_x + 1, size_y + 1)


def plot_map(
    input: List[Tuple[int, int]], dimensions: Tuple[int, int]
) -> List[List[int]]:
    transparent_paper_map = []
    for y in range(dimensions[1]):
        transparent_paper_map.append([""] * dimensions[0])
    for y in range(len(transparent_paper_map)):
        for x in range(len(transparent_paper_map[y])):
            if (x, y) in input:
                transparent_paper_map[y][x] = "#"
            else:
                transparent_paper_map[y][x] = "."
    return transparent_paper_map


def print_map(input: List[List[str]]) -> None:
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end="")
        print("")


def count_dots(input: List[List[str]]) -> int:
    count_of_dots = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "#":
                count_of_dots += 1
    return count_of_dots


if __name__ == "__main__":
    input = open("./src/day13_input.txt", "r").readlines()
    dots = []
    fold_instructions = []
    for line in input:
        line = line.rstrip()
        if "," in line:
            dots.append((int(line.split(",")[0]), int(line.split(",")[1])))
        elif "fold" in line:
            fold_instructions.append(
                (line.split("=")[0].split()[2], int(line.split("=")[1]))
            )
    paper = plot_map(dots, get_map_dimensions(dots))
    for instruction in fold_instructions:
        if instruction[0] == "x":
            print("folding over x")
            paper = fold_over_x(paper, instruction)
        else:
            print("folding over y")
            paper = fold_over_y(paper, instruction)
    print_map(paper)

    print(count_dots(paper))
