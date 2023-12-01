import sys
from typing import Iterable
from pathlib import PurePath


def flatten(items, level=0):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if level >= 3:
            yield x
        elif isinstance(x, Iterable):
            for sub_x in flatten(x, level + 1):
                yield sub_x
        else:
            yield x


def unflatten(items, level=4):
    """Yield items from any nested iterable; see Reference."""
    for x in items:
        if level >= 3:
            yield x
        elif isinstance(x, Iterable):
            for sub_x in flatten(x, level + 1):
                yield sub_x
        else:
            yield x


def add_numbers(x, y):
    return reduce([x, y])


def reduce(x):
    flattened_input = list(flatten(x))
    print(flattened_input)
    for i, item in enumerate(flattened_input):
        # If there's a list in the flattened input, it was nested by 4 pairs
        if isinstance(item, list):
            if i == 0:
                flattened_input[i + 1] += item[1]
            elif i >= len(flattened_input) - 1:
                flattened_input[i - 1] += item[0]
            else:
                flattened_input[i - 1] += item[0]
                flattened_input[i + 1] += item[1]
            flattened_input[i] = 0
            return flattened_input
    print(flattened_input)


def depth(x):
    if isinstance(x, list):
        return 1 + max(depth(item) for item in x)
    else:
        return 0


if __name__ == "__main__":
    input = open(PurePath(sys.argv[0]).with_suffix(".txt"), "r").readlines()
    result = add_numbers([[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1])
    print(result)
    print(reduce([[[[[9, 8], 1], 2], 3], 4]))
    print(reduce([7, [6, [5, [4, [3, 2]]]]]))
    print(reduce([[6, [5, [4, [3, 2]]]], 1]))
    print(reduce([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]]))
    print(reduce([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]))
    # print(flatten([[[[[9,8],1],2],3],4]))
