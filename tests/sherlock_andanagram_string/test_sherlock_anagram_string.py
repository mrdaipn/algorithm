from problems.sherlock_and_anagram_string.sherlock_and_anagram_string import (
    sherlock_and_anagram,
)


def test_check_anagram_of_mom_should_return_2():
    assert sherlock_and_anagram("mom") == 2


def test_check_anagram_of_mm_should_return_1():
    assert sherlock_and_anagram("mm") == 1


def test_check_anagram_of_cdcd_should_return_5():
    assert sherlock_and_anagram("cdcd") == 5
    # c,c; d,d;  cd,cd;
