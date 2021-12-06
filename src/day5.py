from dataclasses import dataclass
from typing import Counter, List, Tuple


@dataclass
class Position:
    x: int
    y: int


@dataclass
class VentPosition:
    positions: List[Position]
    line_start: Position
    line_end: Position

    def __init__(self, start: Tuple[str, str], end: Tuple[str, str]):
        self.line_start = Position(int(start[0].strip()), int(start[1].strip()))
        self.line_end = Position(int(end[0].strip()), int(end[1].strip()))
        self.positions = []
        if self.line_start.x == self.line_end.x:
            if self.line_start.y < self.line_end.y:
                for y in range(self.line_start.y, self.line_end.y + 1, 1):
                    self.positions.append(Position(self.line_start.x, y))
            else:
                for y in range(self.line_end.y, self.line_start.y + 1, 1):
                    self.positions.append(Position(self.line_start.x, y))
        elif self.line_start.y == self.line_end.y:
            if self.line_start.x < self.line_end.x:
                for x in range(self.line_start.x, self.line_end.x + 1, 1):
                    self.positions.append(Position(x, self.line_start.y))
            else:
                for x in range(self.line_end.x, self.line_start.x + 1, 1):
                    self.positions.append(Position(x, self.line_start.y))


def parse_input(input: List[str]):
    vent_positions = []
    max_x = 0
    max_y = 0
    for line in input:
        position = line.split(" -> ")
        x_start, y_start = position[0].split(",")
        x_end, y_end = position[1].split(",")
        # Find size of map
        if int(x_end.strip()) > max_x:
            max_x = int(x_end.strip())
        if int(y_end.strip()) > max_y:
            max_y = int(y_end.strip())
        vent_positions.append(VentPosition((x_start, y_start), (x_end, y_end)))
    size = max([max_x, max_y]) + 1
    return vent_positions, size


def count_overlapping_positions(vents: List[VentPosition], size: int) -> int:
    i = 0
    all_vent_positions = []
    for vent in vents:
        for pos in vent.positions:
            all_vent_positions.append((pos.x, pos.y))

    c = Counter(all_vent_positions)
    pos_counts = []
    while i < size:
        j = 0
        while j < size:
            pos_counts.append(c[(i, j)])
            j += 1
        i += 1
    return pos_counts


if __name__ == "__main__":
    input = open("./src/day5_input.txt", "r").readlines()
    vents, size = parse_input(input)
    pos_counts = count_overlapping_positions(vents, size)
    count_gt2 = 0
    for count in pos_counts:
        if count >= 2:
            count_gt2 += 1
    print(count_gt2)
