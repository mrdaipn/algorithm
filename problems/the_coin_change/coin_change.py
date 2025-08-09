from typing import List


class CoinChange:

    def get_changes(self, target: int, coins: List[int]) -> int:
        return self.__get_changes(target, coins, index=0, solved_solution={})

    def __get_changes(self, target, coins, index: int, solved_solution: dict):
        if index == len(coins) or target < 0:
            return 0

        if target == 0:
            return 1

        if (index, target) in solved_solution:
            return solved_solution[(index, target)]

        current_coin = coins[index]
        take_index_coin = self.__get_changes(
            target=target - current_coin,
            coins=coins,
            index=index,
            solved_solution=solved_solution,
        )
        not_take_index_coin = self.__get_changes(
            target=target, index=index + 1, coins=coins, solved_solution=solved_solution
        )

        solved_solution[(index, target)] = take_index_coin + not_take_index_coin
        return solved_solution[(index, target)]
