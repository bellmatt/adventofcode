from typing import List


def simulate_fish_v2(fishes: List[int], days=0) -> int:
    """Put fish into buckets depending on what day we need to update them"""
    buckets = [0] * (days + 9)
    for f in fishes:
        buckets[f] += 1
    for day in range(days):
        while buckets[day] > 0:
            # Reset fish timer
            buckets[day + 7] += buckets[day]
            # Add new fish
            buckets[day + 9] += buckets[day]
            # Reset the bucket for this day
            buckets[day] = 0
    return sum(buckets)


def simulate_fish(fishes: List[int], days=0) -> int:
    """loop over the list and process TTL of every fish"""
    day = 0

    while day < days:
        fishes = sorted(fishes)
        new_fish = []
        for i, fish in enumerate(fishes):
            if fish == 0:
                fishes[i] = 6
                new_fish.append(8)
            if fish > 0:
                fishes[i] -= 1
        for fish in new_fish:
            fishes.append(fish)
        day += 1
    return len(fishes)


if __name__ == "__main__":
    fish_internal_timers = list(
        int(x.strip()) for x in open("./src/day6_input.txt", "r").readline().split(",")
    )
    # Part 1
    print(simulate_fish(fish_internal_timers, 80))
    # Part 2
    print(simulate_fish_v2(fish_internal_timers, 256))
