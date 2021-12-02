from typing import List
from . import day2
import pytest


@pytest.mark.parametrize(
    "current,input,expected",
    [
        ((0, 0), "forward 5", (5, 0)),
        ((5, 0), "down 5", (5, 5)),
        ((5, 5), "forward 8", (13, 5)),
        ((13, 5), "up 3", (13, 2)),
        ((13, 2), "down 8", (13, 10)),
        ((13, 10), "forward 2", (15, 10)),
    ],
)
def test_position_change(current, input, expected) -> List:
    assert expected == day2.recalculate_position(current, input)


@pytest.mark.parametrize(
    "current,input,expected",
    [
        ((0, 0, 0), "forward 5", (5, 0, 0)),
        ((5, 0, 0), "down 5", (5, 5, 0)),
        ((5, 5, 0), "forward 8", (13, 5, 40)),
        ((13, 5, 40), "up 3", (13, 2, 40)),
        ((13, 2, 40), "down 8", (13, 10, 40)),
        ((13, 10, 40), "forward 2", (15, 10, 60)),
    ],
)
def test_position_change_with_aim(current, input, expected) -> List:
    assert expected == day2.recalculate_position_with_aim(current, input)
