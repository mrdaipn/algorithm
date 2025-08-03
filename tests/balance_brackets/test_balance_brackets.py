from problems.balance_brackets.balance_brackets import BalanceBrackets


class TestBalanceBracket:
    def test_is_balance_of_emtpy_string_should_return_YES(self):
        assert "YES" == BalanceBrackets.is_balance_brackets(input="")

    def test_is_balance_of_open_close_curly_backets_should_return_YES(self):
        assert "YES" == BalanceBrackets.is_balance_brackets(input="{}")

    def test_is_balance_of_open_close_square_backets_should_return_YES(self):
        assert "YES" == BalanceBrackets.is_balance_brackets(input="[]")

    def test_is_balance_of_open_close_parenthese_backets_should_return_YES(self):
        assert "YES" == BalanceBrackets.is_balance_brackets(input="()")

    def test_is_balance_of_open_close_curly_backet_square_close_bracket_should_return_NO(
        self,
    ):
        assert "NO" == BalanceBrackets.is_balance_brackets(input="{]")

    def test_is_balance_of_open_curly_backets_should_return_NO(self):
        assert "NO" == BalanceBrackets.is_balance_brackets(input="{{{{{{")

    def test_is_balance_of_open_square_backets_should_return_NO(self):
        assert "NO" == BalanceBrackets.is_balance_brackets(input="[[[[[")

    def test_is_balance_of_open_parenthese_backets_should_return_NO(self):
        assert "NO" == BalanceBrackets.is_balance_brackets(input="(((((")

    def test_is_balance_of_multiple_balance_backets_should_return_YES(self):
        assert "YES" == BalanceBrackets.is_balance_brackets(input="([(){}[]])([]{})")
