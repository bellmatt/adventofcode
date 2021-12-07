import statistics


if __name__ == "__main__":
    crab_horizontal_positions = sorted(
        list(
            int(x.strip())
            for x in open("./src/day7_input.txt", "r").readline().split(",")
        )
    )
    target = int(statistics.median(crab_horizontal_positions))
    fuel_used = 0
    for crab in crab_horizontal_positions:
        if crab > target:
            fuel_used += crab - target
        else:
            fuel_used += target - crab
    print(fuel_used)
