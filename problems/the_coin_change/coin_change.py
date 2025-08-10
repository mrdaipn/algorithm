from typing import List


class CoinChange:

    def get_changes(self, target: int, coins: List[int]) -> int:
        if not coins and target:
            return 0
        if not coins and not target:
            return 1

        dp = [0 for _ in range(target + 1)]
        dp[0] = 1

        for i in coins:
            for num in range(target + 1):
                if num - i >= 0:
                    dp[num] += dp[num - i]

        return dp[num]
