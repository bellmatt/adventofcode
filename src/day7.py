import statistics
from math import ceil

if __name__ == "__main__":
    crab_horizontal_positions = sorted(
        list(
            int(x.strip())
            for x in open("./src/day7_input.txt", "r").readline().split(",")
        )
    )
    target = int(statistics.median(crab_horizontal_positions))
    fuel_used = sum([abs(crab - target) for crab in crab_horizontal_positions])
    print(f"Part 1: {fuel_used}")

    fuel_used_per_position = []
    for pos in range(min(crab_horizontal_positions), max(crab_horizontal_positions)):
        fuel_used_per_position.append(
            sum(
                [
                    (abs(crab - pos) * (abs(crab - pos) + 1)) / 2
                    for crab in crab_horizontal_positions
                ]
            )
        )

    print(f"Part 2: {min(fuel_used_per_position)}")
