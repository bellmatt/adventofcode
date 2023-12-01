from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Optional
import pytest
import os
import pprint
import sys


@pytest.fixture
def example() -> List[str]:
    return """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines(
        keepends=True
    )


""" 
- / (dir)
  - a (dir)
    - e (dir)
      - i (file, size=584)
    - f (file, size=29116)
    - g (file, size=2557)
    - h.lst (file, size=62596)
  - b.txt (file, size=14848514)
  - c.dat (file, size=8504156)
  - d (dir)
    - j (file, size=4060174)
    - d.log (file, size=8033020)
    - d.ext (file, size=5626152)
    - k (file, size=7214296) """


@dataclass
class Directory:
    name: str
    files: Optional[List[Tuple[str, int]]] = None
    directories: Optional[List[Directory]] = None
    parent: str = ""

    def __init__(self, name: str, parent: str) -> None:
        self.name = name
        self.parent = parent
        if not self.directories:
            self.directories = []
        if not self.files:
            self.files = []

    def add_file(self, file_name: str, file_size: str) -> None:
        self.files.append((file_name, int(file_size)))

    def add_dir(self, dir: Directory) -> None:
        if dir.name != self.parent:
            self.directories.append(dir)

    @property
    def file_size(self) -> int:
        size = 0
        for file in self.files:
            size += file[1]
        return size

    @property
    def total_size(self) -> int:
        size = self.file_size
        for dir in self.directories:
            size += dir.total_size
        return size


def create_directory_structure(input: List[str]) -> Dict[str, Directory]:

    directory_structure: Dict[str, Directory] = {}
    current_dir: Directory = Directory("", "")
    current_path = ""
    for line in input:
        # commands
        if line.startswith("$"):
            # Separate command and args
            command = line.strip()[2:].split(" ")
            if command[0] == "cd":
                if command[1] == "/":
                    # root dir
                    current_dir = Directory(command[1], "")
                    current_path += command[1]
                    directory_structure[current_path] = current_dir
                    continue
                if command[1] == "..":
                    # exiting directory, put current dir in the dir structure
                    directory_structure[current_path] = current_dir
                    current_path = current_path.rsplit(";", 1)[0] or "/"
                    current_dir = directory_structure[current_path]
                else:
                    # entering a directory that we haven't seen yet
                    current_path += ";" + command[1]
                    if current_path not in directory_structure:
                        current_dir = Directory(command[1], current_path)
                    # Entering dir that we saw in an ls output earlier
                    else:
                        current_dir = directory_structure[current_path]
            elif command[0] == "ls":
                continue
        else:
            # output of an ls command
            command = line.strip().split(" ")
            if command[0] == "dir":
                # add a stub if we haven't seen this dir before
                if command[1] not in directory_structure:
                    directory_structure[current_path + ";" + command[1]] = Directory(
                        command[1], current_path
                    )
                current_dir.add_dir(
                    directory_structure[current_path + ";" + command[1]]
                )
            else:
                # file
                current_dir.add_file(command[1], command[0])
    return directory_structure


def part1(input: List[str]) -> int:
    directory_structure = create_directory_structure(input)
    total = 0
    for directory in directory_structure.values():
        total += directory.total_size if directory.total_size <= 100000 else 0
    return total


def part2(input: List[str]) -> int:
    directory_structure = create_directory_structure(input)
    sizes = sorted([d.total_size for d in directory_structure.values()])
    print(sizes)
    used_space = max(sizes)
    free_space = 70000000 - used_space
    required_space = 30000000
    for size in sizes:
        if size + free_space >= required_space:
            return size
    return 0


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 95437
    assert part2(example) == 24933642


def test_part1() -> None:
    assert part1(get_input()) == 1348005


def test_part2() -> None:
    assert part2(get_input()) == 45811471


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
