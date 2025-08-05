import pytest
from problems.stock_maximize.stock_maximize import StockMaximize


class TestStockMaximize:

    @pytest.fixture()
    def stock_maximize(self):
        return StockMaximize()

    def test_stock_maximize_1_2_return_1(self, stock_maximize):
        assert 1 == stock_maximize([1, 2])

    def test_stock_maximize_1_2_100_return_197(self, stock_maximize):
        assert 197 == stock_maximize([1, 2, 100])

    def test_stock_maximize_2_1_return_0(self, stock_maximize):
        assert 0 == stock_maximize([2, 1])

    def test_stock_maximize_1_2_100_2_4_return_199(self, stock_maximize):
        assert 199 == stock_maximize([1, 2, 100, 2, 4])

    def test_stock_maximize_1_2_100_2_1_4_return_202(self, stock_maximize):
        assert 202 == stock_maximize([1, 2, 100, 2, 1, 4])
