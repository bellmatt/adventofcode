from typing import List


def simulate_fish(fishes: List[str], days=0) -> int:
    day = 0
    while day < days:
        # print(f"After {day} days:  {fishes}")
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
        int(x.strip())
        for x in open("./src/day6_testinput.txt", "r").readline().split(",")
    )
    print(simulate_fish(fish_internal_timers, 80))
