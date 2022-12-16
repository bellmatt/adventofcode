from typing import List, Tuple
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines(
        keepends=True
    )


class Position:
    contains: str
    x: int
    y: int
    covered_by_sensor: bool = False

    def __init__(self, x: int, y: int, contains: str) -> None:
        self.x = x
        self.y = y
        self.contains = contains

    def __repr__(self) -> str:
        if self.contains == ".":
            if self.covered_by_sensor:
                return "#"
        return self.contains

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return NotImplemented
        return other.x == self.x and other.y == self.y


class Sensor(Position):
    closest_beacon: Tuple[int, int]

    def __init__(
        self, x: int, y: int, contains: str, beacon_pos: Tuple[int, int]
    ) -> None:
        super().__init__(x, y, contains)
        self.closest_beacon = beacon_pos


def print_map(input: List[List[Position]]) -> None:
    print("map:")
    for y in range(len(input[0])):
        print(f"{y:02}", end=" ")
        for x in range(len(input)):
            print(input[x][y], end="")
        print("")
    print("---")


def part1(input: List[str], result_y: int) -> int:
    # Make map
    min_x = 0
    max_x = 0
    sensors_beacons: List[Tuple[int, int, int, int]] = []
    for line in input:
        sensor_position, beacon_position = line.strip().split(":")
        beacon_x_str, beacon_y_str = beacon_position.split(",")
        beacon_x = int(beacon_x_str.split("=")[1])
        beacon_y = int(beacon_y_str.split("=")[1])
        sensor_x_str, sensor_y_str = sensor_position.split(",")
        sensor_x = int(sensor_x_str.split("=")[1])
        sensor_y = int(sensor_y_str.split("=")[1])
        sensors_beacons.append((sensor_x, sensor_y, beacon_x, beacon_y))
        if sensor_x > max_x:
            max_x = sensor_x
        if beacon_x > max_x:
            max_x = beacon_x
        if sensor_x < min_x:
            min_x = sensor_x
        if beacon_x < min_x:
            min_x = beacon_x
    # Add some padding - we can rule out locations outside the min/max x
    min_x -= 100000
    max_x += 100000
    no_beacon_cells = []
    for x, y, i, j in sensors_beacons:
        # Get distance between sensor and closest beacon
        distance = abs(x - i) + abs(y - j)
        # Get all locations that are within that distance, excluding those where there is a beacon
        for z in range(min_x, max_x):
            if abs(x - z) + abs(y - result_y) <= distance and (z, result_y) != (i, j):
                no_beacon_cells.append(z)
    return len(set(sorted(no_beacon_cells)))


def part2(input: List[str], x_range:Tuple[int,int], y_range:Tuple[int,int]) -> int:
    return 0


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example(example: List[str]) -> None:
    assert part1(example, 10) == 26
    assert part2(example, (0, 20), (0,20)) == (14 * 4000000) + 11


def test_part1() -> None:
    assert part1(get_input(), 2000000) == 5166077


def test_part2() -> None:
    assert part2(get_input(),(0,4000000),(0,4000000)) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input(),2000000)}")
    test_part1()
    print(f"Part 2: {part2(get_input(),(0,4000000),(0,4000000))}")
    test_part2()
