import math
from typing import List


def minimum_window_to_sort(arr: List[int]) -> tuple[int, int]:
    sorted_arr = sorted(arr)

    if arr == sorted_arr:
        return 0, 0

    start, end = 0, len(arr) - 1
    for i in range(len(arr)):
        if arr[i] != sorted_arr[i]:
            start = i
            break

    for i in range(len(arr) - 1, -1, -1):
        if arr[i] != sorted_arr[i]:
            end = i
            break

    return start, end


def minimum_window_to_sort_optimized(arr: List[str]):
    """Return the left, right index of the arr which need to rearrange to have shorted list."""
    left = __find_left(arr)
    if left >= len(arr):
        return 0, 0
    right = __find_right(arr, arr[left])
    return (left, right) if left < right else (0, len(arr) - 1)


def __find_left(arr):
    current_index = 0
    max_so_far = -math.inf
    while True:
        if arr[current_index] < max_so_far:
            return current_index - 1

        max_so_far = arr[current_index]
        current_index += 1

        if current_index == len(arr):
            return current_index


def __find_right(arr, left_value):
    current_index = len(arr) - 1
    while current_index > -1 and arr[current_index] > left_value:
        current_index -= 1

    return current_index
