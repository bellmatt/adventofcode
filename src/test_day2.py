from typing import List
from . import day2
import pytest


@pytest.mark.parametrize(
    "cur_h, cur_d, instruction,exp_h, exp_d",
    [
        (0, 0, "forward 5", 5, 0),
        (5, 0, "down 5", 5, 5),
        (5, 5, "forward 8", 13, 5),
        (13, 5, "up 3", 13, 2),
        (13, 2, "down 8", 13, 10),
        (13, 10, "forward 2", 15, 10),
    ],
)
def test_position_change(cur_h, cur_d, instruction, exp_h, exp_d):
    current_pos = day2.Position(cur_h, cur_d)
    assert exp_h == day2.recalculate_position(current_pos, instruction).horizontal
    current_pos = day2.Position(cur_h, cur_d)
    assert exp_d == day2.recalculate_position(current_pos, instruction).depth


@pytest.mark.parametrize(
    "cur_h, cur_a, cur_d,instruction,exp_h,exp_a,exp_d",
    [
        (0, 0, 0, "forward 5", 5, 0, 0),
        (5, 0, 0, "down 5", 5, 5, 0),
        (5, 5, 0, "forward 8", 13, 5, 40),
        (13, 5, 40, "up 3", 13, 2, 40),
        (13, 2, 40, "down 8", 13, 10, 40),
        (13, 10, 40, "forward 2", 15, 10, 60),
    ],
)
def test_position_change_with_aim(
    cur_h, cur_a, cur_d, instruction, exp_h, exp_a, exp_d
) -> List:
    current_pos = day2.Position(cur_h, cur_d, cur_a)
    assert (
        exp_h == day2.recalculate_position_with_aim(current_pos, instruction).horizontal
    )
    current_pos = day2.Position(cur_h, cur_d, cur_a)
    assert exp_d == day2.recalculate_position_with_aim(current_pos, instruction).depth
    current_pos = day2.Position(cur_h, cur_d, cur_a)
    assert exp_a == day2.recalculate_position_with_aim(current_pos, instruction).aim
