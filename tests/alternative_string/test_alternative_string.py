from problems.alternative_string.alternative_string import AlternativeString


class TestAlternativeString:

    def test_alternative_string_of_2_should_return_2(self):
        alternative_string = AlternativeString()
        assert 2 == alternative_string.alternate("ab")

    def test_alternative_string_acbeab_should_return_4(self):
        alternative_string = AlternativeString()
        assert 4 == alternative_string.alternate("acbaeb")

    def test_alternate_string_beabeefeab_should_return_5(self):
        alternative_string = AlternativeString()
        assert 5 == alternative_string.alternate("beabeefeab")
