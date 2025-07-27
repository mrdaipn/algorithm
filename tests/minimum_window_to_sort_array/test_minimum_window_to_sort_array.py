from problems.minimum_window_to_sort_array.minimum_window_to_sort_arry import (
    minimum_window_to_sort,
    minimum_window_to_sort_optimized,
)


def test_able_to_call_minimum_window_to_sort_with_random_array():
    assert minimum_window_to_sort([3, 7, 5, 6, 9]) == (1, 3)


def test_minimum_window_to_sort_with_decreasing_array():
    assert minimum_window_to_sort([5, 4, 3, 2, 1]) == (0, 4)


def test_minimum_window_to_sort_with_sorted_array():
    assert minimum_window_to_sort([1, 2, 3, 4, 5]) == (0, 0)


def test_able_to_call_minimum_window_to_sort_optimized_with_random_array():
    assert minimum_window_to_sort_optimized([3, 7, 5, 6, 9]) == (1, 3)


def test_minimum_window_to_sort_optimized_with_decreasing_array():
    assert minimum_window_to_sort_optimized([5, 4, 3, 2, 1]) == (0, 4)


def test_minimum_window_to_sort_optimized_with_sorted_array():
    assert minimum_window_to_sort_optimized([1, 2, 3, 4, 5]) == (0, 0)
