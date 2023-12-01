from typing import Tuple, List
import pytest
import os
import re


@pytest.fixture
def example() -> List[str]:
    return """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2""".splitlines(
        keepends=True
    )


def assemble_stacks(input: List[str]) -> Tuple[List[List[str]], int]:
    """Read the input and create a list of lists resembling the stacks of crates"""
    # Assemble the stacks as list of lists
    stacks: List[List[str]] = []
    max_stack_height = 0
    for i, line in enumerate(input):
        if line.startswith(" 1"):
            max_stack_height = i
            # this line shows how many stacks there are
            for stack in line.split("   "):
                stacks.append([])
            break
    for line in input[:max_stack_height]:
        # Split the line into chunks of 4 chars
        for index, item in enumerate([line[i : i + 4] for i in range(0, len(line), 4)]):
            # check for ""
            item_char = item.strip().strip("[]")
            if item_char:
                stacks[index].append(item_char)
    for crate_list in stacks:
        crate_list.reverse()
    return stacks, max_stack_height


def process_instructions_part1(
    input: List[str], stacks: List[List[str]]
) -> List[List[str]]:
    """Process move instructions and return updated stacks"""
    for line in input:
        m = re.match(r"move (.*) from (.*) to (.*)", line.strip())
        if m:
            crates_to_move = int(m.group(1))
            stack_from = int(m.group(2)) - 1
            stack_to = int(m.group(3)) - 1
            for _ in range(0, crates_to_move):
                stacks[stack_to].append(stacks[stack_from].pop())
    return stacks


def process_instructions_part2(
    input: List[str], stacks: List[List[str]]
) -> List[List[str]]:
    """Process move instructions and return updated stacks"""
    for line in input:
        m = re.match(r"move (.*) from (.*) to (.*)", line.strip())
        if m:
            crates_to_move = int(m.group(1))
            stack_from = int(m.group(2)) - 1
            stack_to = int(m.group(3)) - 1
            crates_being_moved = stacks[stack_from][-crates_to_move:]
            stacks[stack_from] = stacks[stack_from][
                : len(stacks[stack_from]) - crates_to_move
            ]
            for crate in crates_being_moved:
                stacks[stack_to].append(crate)
    return stacks


def part1(input: List[str]) -> str:
    stacks, max_stack_height = assemble_stacks(input)
    stacks = process_instructions_part1(input[max_stack_height + 2 :], stacks)

    stack_tops = []
    for stack in stacks:
        stack_tops.append(stack.pop())

    return "".join(stack_tops)


def part2(input: List[str]) -> str:
    stacks, max_stack_height = assemble_stacks(input)
    stacks = process_instructions_part2(input[max_stack_height + 2 :], stacks)

    stack_tops = []
    for stack in stacks:
        stack_tops.append(stack.pop())
    return "".join(stack_tops)


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == "CMZ"


def test_example2(example: List[str]) -> None:
    assert part2(example) == "MCD"


def test_part1() -> None:
    assert part1(get_input()) == "FZCMJCRHZ"


def test_part2() -> None:
    assert part2(get_input()) == "JSDHQMZGF"


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
