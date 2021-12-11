from typing import List, Tuple
import heapq
from functools import reduce


def find_low_points(heightmap: List[List[str]]) -> List[Tuple[int, int, int]]:
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
                        low_points.append((int(point), i, j))
                elif j == len(heightlist) - 1:
                    # bottom left corner
                    # 2 neighbours up and right
                    if int(point) < int(heightlist[j - 1]) and int(point) < int(
                        heightmap[i + 1][j]
                    ):
                        low_points.append((int(point), i, j))
                else:
                    # left column after first row and before last row
                    # 3 neighbours up right and down
                    if (
                        int(point) < int(heightlist[j + 1])
                        and int(point) < int(heightlist[j - 1])
                        and int(point) < int(heightmap[i + 1][j])
                    ):
                        low_points.append((int(point), i, j))
            elif j == 0:
                if i == len(heightmap) - 1:
                    # top right corner
                    # 2 neighbours down and left
                    if int(point) < int(heightlist[j + 1]) and int(point) < int(
                        heightmap[i - 1][j]
                    ):
                        low_points.append((int(point), i, j))
                else:
                    # top row after first column and before last column
                    # 3 neighbours left down right
                    if (
                        int(point) < int(heightlist[j + 1])
                        and int(point) < int(heightmap[i - 1][j])
                        and int(point) < int(heightmap[i + 1][j])
                    ):
                        low_points.append((int(point), i, j))
            elif i == len(heightmap) - 1:
                if j == len(heightlist) - 1:
                    # bottom right corner
                    # 2 neighbours up and left
                    if int(point) < int(heightlist[j - 1]) and int(point) < int(
                        heightmap[i - 1][j]
                    ):
                        low_points.append((int(point), i, j))
                else:
                    # right column after first row and before last row
                    # 3 neighbours left up and down
                    if (
                        int(point) < int(heightlist[j + 1])
                        and int(point) < int(heightlist[j - 1])
                        and int(point) < int(heightmap[i - 1][j])
                    ):
                        low_points.append((int(point), i, j))
            elif j == len(heightlist) - 1:
                # bottom row
                # 3 neighbours up left and right
                if (
                    int(point) < int(heightlist[j - 1])
                    and int(point) < int(heightmap[i - 1][j])
                    and int(point) < int(heightmap[i + 1][j])
                ):
                    low_points.append((int(point), i, j))
            else:
                # any other points, all with 4 neighbours
                if (
                    int(point) < int(heightlist[j - 1])
                    and int(point) < int(heightlist[j + 1])
                    and int(point) < int(heightmap[i - 1][j])
                    and int(point) < int(heightmap[i + 1][j])
                ):
                    low_points.append((int(point), i, j))
    return low_points


def sum_low_point_values(low_points: List[Tuple[int, int, int]]) -> int:
    return sum([1 + x[0] for x in low_points])


def find_basin_sums(
    input: List[List[str]], low_points: List[Tuple[int, int, int]]
) -> int:
    basin_sizes = []
    # All basins have a low point:
    for low_point in low_points:
        basin_sizes.append(
            len(
                find_basin(
                    input,
                    (low_point[1], low_point[2]),
                    [(low_point[1], low_point[2])],
                    [(low_point[1], low_point[2])],
                )
            )
        )
    print(reduce((lambda x, y: x * y), (heapq.nlargest(3, basin_sizes))))
    return


def find_basin(
    input: List[List[str]],
    start: Tuple[int, int],
    basin_points: List[Tuple[int, int]],
    inspected: List[Tuple[int, int]],
) -> List[Tuple[int, int]]:
    # check neighbours
    num_inspected = len(inspected)
    if int(start[0]) > 0:
        if (
            int(input[start[0] - 1][start[1]]) == 9
            or input[start[0] - 1][start[1]] in inspected
        ):
            pass
        elif (start[0] - 1, start[1]) not in inspected:
            basin_points.append((start[0] - 1, start[1]))
            inspected.append((start[0] - 1, start[1]))

    if int(start[1]) > 0:
        if (
            int(input[start[0]][start[1] - 1]) == 9
            or input[start[0]][start[1] - 1] in inspected
        ):
            pass
        elif (start[0], start[1] - 1) not in inspected:
            basin_points.append((start[0], start[1] - 1))
            inspected.append((start[0], start[1] - 1))

    if int(start[0]) < len(input) - 1:
        if (
            int(input[start[0] + 1][start[1]]) == 9
            or input[start[0] + 1][start[1]] in inspected
        ):
            pass
        elif (start[0] + 1, start[1]) not in inspected:
            basin_points.append((start[0] + 1, start[1]))
            inspected.append((start[0] + 1, start[1]))

    if int(start[1]) < len(input[0]) - 1:
        if (
            int(input[start[0]][start[1] + 1]) == 9
            or input[start[0]][start[1] + 1] in inspected
        ):
            pass
        elif (start[0], start[1] + 1) not in inspected:
            basin_points.append((start[0], start[1] + 1))
            inspected.append((start[0], start[1] + 1))

    while num_inspected < len(inspected):
        find_basin(input, inspected[num_inspected], basin_points, inspected)
        num_inspected += 1

    return basin_points


def print_map(input: List[List[str]]) -> None:
    for i in range(len(input)):
        for j in range(len(input[i])):
            print(input[i][j], end=" ")
        print("")


if __name__ == "__main__":
    heightmap = [
        list(line.strip()) for line in open("./src/day9_input.txt", "r").readlines()
    ]
    low_points = find_low_points(heightmap)
    # Part 1
    print(sum_low_point_values(low_points))

    # Part 2
    print(find_basin_sums(heightmap, low_points))
