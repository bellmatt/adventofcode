from dataclasses import dataclass
from pathlib import PurePath
import sys


@dataclass
class Cuboid:
    x: int
    y: int
    z: int
    state: bool = False


if __name__ == "__main__":
    cubes = [
        Cuboid(x, y, z)
        for x in range(-50, 51)
        for y in range(-50, 51)
        for z in range(-50, 51)
    ]
    print(len(cubes))

    instructions = [
        (
            line.rstrip().split(" ")[0],
            line.rstrip().split(" ")[1].split(",")[0].split("=")[1].split(".."),
            line.rstrip().split(" ")[1].split(",")[1].split("=")[1].split(".."),
            line.rstrip().split(" ")[1].split(",")[2].split("=")[1].split(".."),
        )
        for line in open(PurePath(sys.argv[0]).with_suffix('.txt'), "r").readlines()
    ]
    count_on = 0
    for instruction in instructions:
        for cuboid in cubes:
            if (
                cuboid.x in range(int(instruction[1][0]), int(instruction[1][1]) + 1)
                and cuboid.y
                in range(int(instruction[2][0]), int(instruction[2][1]) + 1)
                and cuboid.z
                in range(int(instruction[3][0]), int(instruction[3][1]) + 1)
            ):
                if instruction[0] == "on":
                    if not cuboid.state:
                        count_on += 1
                    cuboid.state = True
                else:
                    if cuboid.state:
                        count_on -= 1
                    cuboid.state = False
        print(f"{instruction} -> {count_on}")
    print(count_on)
