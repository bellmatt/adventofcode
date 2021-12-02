from . import day1


def test_calculation_of_sliding_window_measurements():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = [607, 618, 618, 617, 647, 716, 769, 792]
    assert expected == day1.get_sliding_window_measurements(input)


def test_count_of_increasing_measurements():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 7
    assert expected == day1.count_increases(input)


def test_count_of_sliding_window_measurements():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expected = 5
    assert expected == day1.count_increases(day1.get_sliding_window_measurements(input))
