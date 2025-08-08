from typing import List


class EqualStacks:

    def compute_common_heigh(self, h1: List, h2: List, h3: List) -> int:
        """Computet the highest stack that those 3 stacks share"""
        if not h1 or not h2 or not h3:
            return 0

        running_list1 = self.__compute_running_list(h1)
        running_list2 = self.__compute_running_list(h2)
        running_list3 = self.__compute_running_list(h3)

        heighest_common_tall = self.__find_heighest_common_tall(
            running_list1, running_list2, running_list3
        )
        return heighest_common_tall

    def __compute_running_list(self, h: List[int]) -> list:
        running_list = []
        running_total = 0

        for i in range(len(h) - 1, -1, -1):
            running_total += h[i]
            running_list.append(running_total)

        return running_list

    def __find_heighest_common_tall(
        self, heigh_index1: List[int], heigh_index2: List[int], heigh_index3: List[int]
    ) -> int:
        common_indexes = (
            set(heigh_index1)
            .intersection(set(heigh_index2))
            .intersection(set(heigh_index3))
        )
        if common_indexes:
            return max(common_indexes)
        else:
            return 0
