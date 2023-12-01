from pathlib import PurePath
import sys
from typing import List


def count_increases(input: List[int]) -> int:
    """Count the number of times a measurement is higher than the previous one"""
    count_of_increases = 0
    for index, line in enumerate(input):
        if index > 0 and line > input[index - 1]:
            count_of_increases += 1
    return count_of_increases


def get_sliding_window_measurements(
    input: List[int], window_size: int = 3
) -> List[int]:
    """Return a list of three-measurement windows"""
    sliding_window_measurements = []
    i = 0
    while i < len(input) - (window_size - 1):
        sliding_window_measurements.append(sum(input[i : i + window_size]))
        i += 1
    return sliding_window_measurements


if __name__ == "__main__":
    lines = open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readlines()
    input_list = [int(line.rstrip()) for line in lines]
    # Part 1:
    print(count_increases(input_list))
    # Part 2:
    print(count_increases(get_sliding_window_measurements(input_list)))
