from . import day1


def test_sum_depths():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = [607, 618, 618, 617, 647, 716, 769, 792]
    assert expected == day1.get_sliding_window_measurements(input)


def test_increase_counts_part1():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 7
    assert expected == day1.day1part1(input)


def test_increase_counts_part2():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 5
    assert expected == day1.day1part2(input)
