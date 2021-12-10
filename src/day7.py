import statistics
from math import ceil

if __name__ == "__main__":
    crab_horizontal_positions = sorted(
        list(
            int(x.strip())
            for x in open("./src/day7_testinput.txt", "r").readline().split(",")
        )
    )
    target = int(statistics.median(crab_horizontal_positions))
    fuel_used = sum([abs(crab - target) for crab in crab_horizontal_positions])
    print(f"Part 1: {fuel_used}")

    # This works for test data, but not the real data:
    target = statistics.mean(crab_horizontal_positions)
    fuel_used = sum(
        [
            (abs(crab - target) * (abs(crab - target) + 1)) / 2
            for crab in crab_horizontal_positions
        ]
    )

    print(f"Part 2: {int(ceil(fuel_used))}")
