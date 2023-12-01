from typing import List, Callable
import pytest
import os
from math import trunc, prod, sqrt


@pytest.fixture
def example() -> List[str]:
    return """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".splitlines(
        keepends=True
    )


def make_operation_func(input: str) -> Callable[[int], int]:
    calc = input.split(" = ")[1].strip()
    op = "+" if "+" in calc else "*"
    number = calc.split("+")[1].strip() if "+" in calc else calc.split("*")[1].strip()

    def _function(old: int) -> int:
        if number == "old":
            amount = old
        else:
            amount = int(number)
        if op == "+":
            return old + amount
        if op == "*":
            return old * amount
        raise Exception(f"{old} {number} {op} {amount}")

    return _function


class Monkey:
    items: List[int]
    op: Callable[[int], int]
    inspect_count = 0
    test_divisor = 0
    next_monkey_if_true = 0
    next_monkey_if_false = 0

    def __init__(
        self, items: str, operation: str, test: str, result: List[str]
    ) -> None:
        if "," in items:
            self.items = [int(item) for item in items.split(", ")]
        else:
            self.items = [int(items)]
        self.op = make_operation_func(operation)
        self.test_divisor = int(test.split(" by ")[1].strip())
        self.next_monkey_if_true = int(result[0].strip()[-1])
        self.next_monkey_if_false = int(result[1].strip()[-1])

    def test(self, number: int) -> bool:
        if self.test_divisor == 5:
            return int(repr(number)[-1]) in [0, 5]
        if self.test_divisor == 5:
            return int(repr(number)[-1]) in [0, 5]

        return number % self.test_divisor == 0

    def throw(self, test_result: bool) -> int:
        return self.next_monkey_if_true if test_result else self.next_monkey_if_false


def part1(input: List[str], worry_level_divisor: int = 3, count: int = 20) -> int:
    monkeys: List[Monkey] = []
    for i, line in enumerate(input):
        if line.strip().startswith("Monkey"):
            items = input[i + 1].split(":")[1].strip()
            operation = input[i + 2].split(":")[1].strip()
            test = input[i + 3].split(":")[1].strip()
            throw = input[i + 4 : i + 6]
            monkeys.append(Monkey(items, operation, test, throw))
    # Multiply all the divisors together, then mod the worry level by it.
    # this makes the huge numbers smaller without affecting divisibility
    modulo = prod([monkey.test_divisor for monkey in monkeys])
    while count > 0:
        for i, monkey in enumerate(monkeys):
            # print(f"\nmonkey {i}: {monkey.items}")
            for item in list(monkey.items):
                # print(f"  Monkey inspects an item with a worry level of {item}")
                monkey.items.remove(item)
                monkey.inspect_count += 1
                item = monkey.op(item)
                # print(f"    Worry level is now {item}")
                if worry_level_divisor > 1:
                    item = trunc(item / worry_level_divisor)
                else:
                    item %= modulo
                # print(f"    Monkey gets bored with item. Worry level is divided by 3 to {item}")
                test_result = monkey.test(item)
                # print(f"    Current worry level divisiblity: {test_result}")
                monkey_to = monkey.throw(test_result)
                # print(f"    Item with worry level {item} is thrown to monkey {monkey_to}.")
                monkeys[monkey_to].items.append(item)
                # print(f"      Monkey {monkey_to} items: {monkeys[monkey_to].items}" )

    inspect_counts = sorted(
        list([monkey.inspect_count for monkey in monkeys]), reverse=True
    )[:2]

    return prod(inspect_counts)


def part2(input: List[str], worry_level_divisor: int = 1, count: int = 10000) -> int:
    return part1(input, worry_level_divisor, count)


def get_input() -> List[str]:
    base, _ = os.path.splitext(os.path.abspath(__file__))
    return open(base + ".txt", "r").readlines()


def test_example1(example: List[str]) -> None:
    assert part1(example) == 10605
    assert part2(example, 1, 1) == 24
    assert part2(example, 1, 20) == 99 * 103
    assert part2(example) == 2713310158


def test_part1() -> None:
    assert part1(get_input(), 3, 20) == 78678


def test_part2() -> None:
    assert part2(get_input(), 1, 10000) == 15333249714


if __name__ == "__main__":
    print(f"Part 1: {part1(get_input())}")
    test_part1()
    print(f"Part 2: {part2(get_input())}")
    test_part2()
