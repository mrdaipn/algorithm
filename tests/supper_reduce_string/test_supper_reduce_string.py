from problems.supper_reduce_string.supper_reduce_string import supper_reduce_string


def test_supper_reduce_string_should_return_correct_result():
    assert supper_reduce_string("abba") == "Empty String"


def test_supper_reduce_string_with_reducible_string():
    assert supper_reduce_string("aabbcc") == "Empty String"


def test_supper_reduce_string_with_non_reducible_string():
    assert supper_reduce_string("abcde") == "abcde"


def test_supper_reduce_string_with_aa_should_return_empty():
    assert supper_reduce_string("aa") == "Empty String"


def test_supper_reduce_string_with_single_character():
    assert supper_reduce_string("a") == "a"


def test_supper_reduce_string_with_empty_string():
    assert supper_reduce_string("") == "Empty String"


def test_supper_reduce_string_with_long_reducible_string():
    assert supper_reduce_string("aaabbbccc") == "abc"
