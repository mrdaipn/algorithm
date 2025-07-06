from problems.sherlock_string.sherlock_string import sherlock_string


def test_can_call_sherlock_string():
    sherlock_string("aaabbbccc")


def test_sherlock_string_with_all_same_characters():
    assert sherlock_string("aaaaaa") == "YES"


def test_sherlock_string_with_2_different_chars_and_same_frequency_return_yes():
    assert sherlock_string("aabb") == "YES"


def test_sherlock_string_with_3_different_frequencies_return_no():
    assert sherlock_string("aaabbccdde") == "NO"


def test_sherlock_string_with_2_different_chars_and_frequency_difference_return_no():
    assert sherlock_string("aabbbb") == "NO"


def test_sherlock_string_with_one_char_different_frequency_return_yes():
    assert sherlock_string("aabbccdde") == "YES"
