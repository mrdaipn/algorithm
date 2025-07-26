from problems.product_all_other_elements.product_all_other_elements import (
    product_all_other_elements,
)


def test_product_all_other_elements_should_work():
    input_data = [1, 2, 3, 4]
    expected_output = [24, 12, 8, 6]
    assert product_all_other_elements(input_data) == expected_output


def test_product_all_other_elements_with_zero_should_work():
    input_data = [1, 2, 0, 4]
    expected_output = [0, 0, 8, 0]
    assert product_all_other_elements(input_data) == expected_output


def test_product_all_other_elements_with_negative_numbers_should_work():
    input_data = [-1, 2, -3, 4]
    expected_output = [-24, 12, -8, 6]
    assert product_all_other_elements(input_data) == expected_output
