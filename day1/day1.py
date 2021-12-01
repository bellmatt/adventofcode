
from typing import List


def day1part1(input:List[int] = []) -> int:
    count_of_increases = 0
    for index, line in enumerate(input):
        if index > 0:
            if int(line) > int(input[index-1]):
                count_of_increases = count_of_increases + 1
    return count_of_increases

def get_sliding_window_measurements(input:List[int]) -> List:
    sliding_window_measurements = []
    for index, line in enumerate(input):
        if index < len(input) - 2:
            sliding_window_measurements.append(line + input[index+1] + input[index+2])
    return sliding_window_measurements

def day1part2(input:List[int] = []) -> int:
    count_of_increases = 0
    sliding_window_measurements = get_sliding_window_measurements(input)
    for index, line in enumerate(input):
        if index > 0 and index < len(input) - 2:
            if sliding_window_measurements[index] > sliding_window_measurements[index-1]:
                count_of_increases = count_of_increases + 1
    return count_of_increases


if __name__ == "__main__":
    lines = open("./day1/input.txt","r").readlines()
    input_list = [int(line.rstrip()) for line in lines]
    print(day1part1(input_list))
    print(day1part2(input_list))
