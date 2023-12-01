from pathlib import PurePath
import sys
from typing import Counter, List


def increase_neighbour_energy(octopus_map: List[List[str]], i, j) -> List[List[str]]:
    if i == 0:
        # Top row
        if j == 0:
            # Top left corner
            octopus_map[i + 1][j] += 1
            octopus_map[i][j + 1] += 1
            octopus_map[i + 1][j + 1] += 1
        elif j == len(octopus_map[i]) - 1:
            # top right corner
            octopus_map[i][j - 1] += 1
            octopus_map[i + 1][j] += 1
            octopus_map[i + 1][j - 1] += 1
        else:
            # Top row after first col and before last col
            octopus_map[i + 1][j] += 1
            octopus_map[i + 1][j + 1] += 1
            octopus_map[i + 1][j - 1] += 1
            octopus_map[i][j - 1] += 1
            octopus_map[i][j + 1] += 1
    elif j == 0:
        if i == len(octopus_map) - 1:
            # Left col
            octopus_map[i - 1][j] += 1
            octopus_map[i - 1][j + 1] += 1
            octopus_map[i][j + 1] += 1
        else:
            # left col after first row and before last row
            octopus_map[i - 1][j] += 1
            octopus_map[i - 1][j + 1] += 1
            octopus_map[i + 1][j] += 1
            octopus_map[i][j + 1] += 1
            octopus_map[i + 1][j + 1] += 1
    elif i == len(octopus_map) - 1:
        if j == len(octopus_map[i]) - 1:
            # bottom right corner
            octopus_map[i - 1][j] += 1
            octopus_map[i][j - 1] += 1
            octopus_map[i - 1][j - 1] += 1
        else:
            # bottom row
            octopus_map[i - 1][j] += 1
            octopus_map[i - 1][j + 1] += 1
            octopus_map[i][j + 1] += 1
            octopus_map[i][j - 1] += 1
            octopus_map[i - 1][j - 1] += 1
    elif j == len(octopus_map[i]) - 1:
        # right col
        octopus_map[i - 1][j] += 1
        octopus_map[i + 1][j] += 1
        octopus_map[i + 1][j - 1] += 1
        octopus_map[i - 1][j - 1] += 1
        octopus_map[i][j - 1] += 1
    else:
        # any other points
        octopus_map[i - 1][j - 1] += 1
        octopus_map[i - 1][j] += 1
        octopus_map[i - 1][j + 1] += 1
        octopus_map[i + 1][j - 1] += 1
        octopus_map[i + 1][j] += 1
        octopus_map[i + 1][j + 1] += 1
        octopus_map[i][j - 1] += 1
        octopus_map[i][j + 1] += 1
    return octopus_map


def print_map(input: List[List[str]]) -> None:
    print("")
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end=" ")
        print("")
    print("---")


if __name__ == "__main__":
    octopus_map = [
        list(int(x) for x in list(line.strip()))
        for line in open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readlines()
    ]
    flashes = []
    # Part 1: set to 100
    for step in range(500):
        for i in range(len(octopus_map)):
            for j in range(len(octopus_map[i])):
                octopus_map[i][j] += 1
        i = 0
        j = 0
        while i < len(octopus_map):
            j = 0
            while j < len(octopus_map[i]):
                flash = False
                if octopus_map[i][j] > 9 and (step, i, j) not in flashes:
                    flashes.append((step, i, j))
                    # increase energy of neighbours
                    octopus_map = increase_neighbour_energy(octopus_map, i, j)
                    i = 0
                    j = 0
                    flash = True
                    continue
                j += 1
            if flash:
                i = 0
            else:
                i += 1

        for i in range(len(octopus_map)):
            for j in range(len(octopus_map[i])):
                if octopus_map[i][j] > 9:
                    octopus_map[i][j] = 0
        if step == 100:
            print_map(octopus_map)
            print(f"Part 1 {len(flashes)}")
    c = Counter(list(x[0] for x in flashes))
    print(c.most_common(1))
