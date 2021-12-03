from abc import abstractproperty
from os import remove
from typing import List
from collections import Counter


def calculate_power_consumption(input: List[str] = []) -> int:
    gamma_binary = ""
    epsilon_binary = ""
    for row in list(map(list, zip(*input))):
        count = Counter(row)
        gamma_binary += count.most_common(2)[0][0]
        epsilon_binary += count.most_common(2)[1][0]
    return int(gamma_binary, 2) * int(epsilon_binary, 2)


def count_elements_in_columns(input: List[str] = []) -> List[Counter]:
    counters = []
    for row in list(map(list, zip(*input))):
        # Sort the row first, it helps with ordering the Counter results
        counters.append(Counter(sorted(row, reverse=True)))
    return counters


def calculate_rating(input: List[str] = [], counter_index: int = 0) -> int:
    """counter_index determines whether to look for most common (0) or least common (1) elements"""
    bitindex = 0
    while len(input) > 1 and bitindex < len(list(input[0])):
        counters = count_elements_in_columns(input)
        most_common_bit_counter = counters[bitindex].most_common(2)
        input = [
            x
            for x in input
            if list(x)[bitindex] == most_common_bit_counter[counter_index][0]
        ]
        bitindex += 1
    return int(input[0], 2)


if __name__ == "__main__":
    lines = open("./src/day3_input.txt", "r").readlines()
    lines = [s.strip() for s in lines]
    print(f"Part 1: Power Consumption = {calculate_power_consumption(lines)}")
    print(
        f"Part 2: Life Support Rating = {calculate_rating(lines,0)*calculate_rating(lines,1)}"
    )
