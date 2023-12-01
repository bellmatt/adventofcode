from typing import List, Tuple
import pytest
import os


@pytest.fixture
def example() -> List[str]:
    return """noop
addx 3
addx -5""".splitlines(
        keepends=True
    )


@pytest.fixture
def example2() -> List[str]:
    return """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop""".splitlines(
        keepends=True
    )


class CPU:
    x: int = 1
    x_history: List[int]

    def __init__(self) -> None:
        self.x_history = []

    def noop(self) -> None:
        self.x_history.append(self.x)

    def addx(self, amount: int) -> None:
        self.x_history.append(self.x)
        self.x_history.append(self.x)
        self.x += amount


class CRT:
    sprite_position: Tuple[int, int, int]
    crt_row: List[str]

    def __init__(self) -> None:
        self.sprite_position = (0, 1, 2)
        self.crt_row = ["."] * 240

    def draw(self, cycle: int, x: int) -> None:
        self.sprite_position = (x - 1, x, x + 1)
        if cycle % 40 in self.sprite_position:
            self.crt_row[cycle] = "#"

    def print(self) -> None:
        rows = list([self.crt_row[i : i + 40] for i in range(0, len(self.crt_row), 40)])
        print(rows)
        for row in rows:
            for char in row:
                print(char, end="")
            print()


def part1(input: List[str]) -> int:
    cpu = CPU()
    for line in input:
        if line.strip() == "noop":
            cpu.noop()
            continue
        command, amount = line.strip().split(" ")
        if command == "addx":
            cpu.addx(int(amount))
    signal = 0
    if len(cpu.x_history) > 20:
        for i in range(19, len(cpu.x_history), 40):
            signal += cpu.x_history[i] * (i + 1)

    return signal


def part2(input: List[str]) -> int:
    cpu = CPU()
    for line in input:
        if line.strip() == "noop":
            cpu.noop()
            continue
        command, amount = line.strip().split(" ")
        if command == "addx":
            cpu.addx(int(amount))
    crt = CRT()
    for i, x in enumerate(cpu.x_history):
        crt.draw(i, x)
    crt.print()
    return 0


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 0


def test_example2(example2: List[str]) -> None:
    assert part1(example2) == 13140
    assert part2(example2) == 0


def test_part1() -> None:
    assert part1(get_input()) == 15260


def test_part2() -> None:
    assert part2(get_input()) == 0


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
