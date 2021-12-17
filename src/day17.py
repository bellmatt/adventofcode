from typing import List, Tuple


def has_probe_missed_target_area(
    pos: Tuple[int, int], target_area: List[List[int]]
) -> bool:
    """
    - If x > the end of the target area (as the probe doesn't move backwards)
    - y < start of target area (as it won't go back up)
    """
    return (
        pos[1] < target_area[1][0] or pos[0] > target_area[0][len(target_area[0]) - 1]
    )


def is_probe_in_target_area(pos: Tuple[int, int], target_area: List[List[int]]) -> bool:
    return pos[0] in target_area[0] and pos[1] in target_area[1]


def fire_probe(
    curr_pos: Tuple[int, int], velocity: Tuple[int, int], target_area: List[List[int]]
) -> Tuple[bool, Tuple[int, int], int]:
    """Returns true if probe hits target area"""
    start_velocity = velocity
    max_y_pos = curr_pos[1]
    if is_probe_in_target_area(curr_pos, target_area):
        return True
    while not has_probe_missed_target_area(curr_pos, target_area):
        curr_pos = (curr_pos[0] + velocity[0], curr_pos[1] + velocity[1])
        if velocity[0] > 0:
            velocity = (velocity[0] - 1, velocity[1] - 1)
        elif velocity[0] == 0:
            velocity = (velocity[0], velocity[1] - 1)
        else:
            velocity = (velocity[0] + 1, velocity[1] - 1)
        if max_y_pos < curr_pos[1]:
            max_y_pos = curr_pos[1]
        if is_probe_in_target_area(curr_pos, target_area):
            return (True, start_velocity, max_y_pos)
    return (False, start_velocity, max_y_pos)


if __name__ == "__main__":
    input = "target area: x=20..30, y=-10..-5"
    input = "target area: x=192..251, y=-89..-59"

    target_area_x = list(range(192, 251 + 1, 1))
    target_area_y = list(range(-89, -59 + 1, 1))
    # Test input:
    # target_area_x = list(range(20,30+1,1))
    # target_area_y = list(range(-10,-5+1,1))
    results = [
        fire_probe((0, 0), (x, y), [target_area_x, target_area_y])
        for x in range(500)
        for y in range(-500, 500, 1)
    ]
    print(len([result[1] for result in results if result[0]]))
    print(max([result[2] for result in results if result[0]]))
