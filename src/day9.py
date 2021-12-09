from typing import List


def find_low_points(heightmap: List[List[str]]) -> int:
    low_points = []
    for i, heightlist in enumerate(heightmap):
        for j, point in enumerate(heightlist):
            if i == 0:
                # Left column
                if j == 0:
                    # top left corner
                    # 2 neighbours right and down
                    if int(point) < int(heightlist[j + 1]) and int(point) < int(
                        heightmap[i + 1][j]
                    ):
                        low_points.append(int(point))
                elif j == len(heightlist) - 1:
                    # bottom left corner
                    # 2 neighbours up and right
                    if int(point) < int(heightlist[j - 1]) and int(point) < int(
                        heightmap[i + 1][j]
                    ):
                        low_points.append(int(point))
                else:
                    # left column after first row and before last row
                    # 3 neighbours up right and down
                    if (
                        int(point) < int(heightlist[j + 1])
                        and int(point) < int(heightlist[j - 1])
                        and int(point) < int(heightmap[i + 1][j])
                    ):
                        low_points.append(int(point))
            elif j == 0:
                if i == len(heightmap) - 1:
                    # top right corner
                    # 2 neighbours down and left
                    if int(point) < int(heightlist[j + 1]) and int(point) < int(
                        heightmap[i - 1][j]
                    ):
                        low_points.append(int(point))
                else:
                    # top row after first column and before last column
                    # 3 neighbours left down right
                    if (
                        int(point) < int(heightlist[j + 1])
                        and int(point) < int(heightmap[i - 1][j])
                        and int(point) < int(heightmap[i + 1][j])
                    ):
                        low_points.append(int(point))
            elif i == len(heightmap) - 1:
                if j == len(heightlist) - 1:
                    # bottom right corner
                    # 2 neighbours up and left
                    if int(point) < int(heightlist[j - 1]) and int(point) < int(
                        heightmap[i - 1][j]
                    ):
                        low_points.append(int(point))
                else:
                    # right column after first row and before last row
                    # 3 neighbours left up and down
                    if (
                        int(point) < int(heightlist[j + 1])
                        and int(point) < int(heightlist[j - 1])
                        and int(point) < int(heightmap[i - 1][j])
                    ):
                        low_points.append(int(point))
            elif j == len(heightlist) - 1:
                # bottom row
                # 3 neighbours up left and right
                if (
                    int(point) < int(heightlist[j - 1])
                    and int(point) < int(heightmap[i - 1][j])
                    and int(point) < int(heightmap[i + 1][j])
                ):
                    low_points.append(int(point))
            else:
                # any other points, all with 4 neighbours
                if (
                    int(point) < int(heightlist[j - 1])
                    and int(point) < int(heightlist[j + 1])
                    and int(point) < int(heightmap[i - 1][j])
                    and int(point) < int(heightmap[i + 1][j])
                ):
                    low_points.append(int(point))
    return sum([1 + x for x in low_points])


def print_map(input: List[List[str]]) -> None:
    for i, x in enumerate(input):
        for j, y in enumerate(input[i]):
            print(input[i][j], end=" ")
        print("")


if __name__ == "__main__":
    heightmap = [
        list(line.strip()) for line in open("./src/day9_input.txt", "r").readlines()
    ]
    print(find_low_points(heightmap))
