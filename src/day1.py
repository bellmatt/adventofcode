from typing import List


def count_increases(input: List[int] = []) -> int:
    """Count the number of times a measurement is higher than the previous one"""
    count_of_increases = 0
    for index, line in enumerate(input):
        if index > 0:
            if line > input[index - 1]:
                count_of_increases = count_of_increases + 1
    return count_of_increases


def get_sliding_window_measurements(input: List[int]) -> List[int]:
    """Return a list of three-measurement windows"""
    sliding_window_measurements = []
    for index, line in enumerate(input):
        if index < len(input) - 2:
            sliding_window_measurements.append(
                line + input[index + 1] + input[index + 2]
            )
    return sliding_window_measurements


if __name__ == "__main__":
    lines = open("./src/day1_input.txt", "r").readlines()
    input_list = [int(line.rstrip()) for line in lines]
    # Part 1:
    print(count_increases(input_list))
    # Part 2:
    print(count_increases(get_sliding_window_measurements(input_list)))
