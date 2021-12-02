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
