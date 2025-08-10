from problems.the_coin_change.coin_change import CoinChange


class TestCoinChange:

    def test_get_changes_for_3_of_empty_coins(self):
        coin_change = CoinChange()
        assert 0 == coin_change.get_changes(3, [])

    def test_get_changes_for_0_of_empty_coins(self):
        coin_change = CoinChange()
        assert 1 == coin_change.get_changes(0, [])

    def test_get_changes_for_3_of_non_empty_coins_should_compute(self):
        coin_change = CoinChange()
        assert 2 == coin_change.get_changes(3, [1, 2])

    def test_get_changes_for_hacker_rank_input(self):
        coin_change = CoinChange()
        assert 3 == coin_change.get_changes(3, [8, 3, 1, 2])
