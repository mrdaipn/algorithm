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
