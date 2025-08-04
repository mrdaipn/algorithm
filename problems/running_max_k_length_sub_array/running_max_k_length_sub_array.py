from typing import List


class RuningMaxKLengthSubArray:

    def __init__(self, array: List, k: int):
        self.__array = array
        self.__k = k

    def get_running_max_array(self) -> List:
        result = []
        if not self.__array:
            return result

        for window in range(0, len(self.__array) - self.__k + 1):
            max_value = self.__find_max_window_value(window)
            result.append(max_value)

        return result

    def __find_max_window_value(self, window: int):
        return max(self.__array[window : window + self.__k])
