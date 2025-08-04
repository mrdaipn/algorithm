import pytest

from problems.stack_max.stack_max import StackMax


class TestStackMax:

    @pytest.fixture()
    def stack_max(self):
        return StackMax()

    def test_emtpy_stack_get_max_should_throw_an_error(self, stack_max):
        with pytest.raises(ValueError, match="Stack is empty."):
            stack_max.get_max()

    def test_get_max_with_one_element_in_the_stack_should_return_that_element(
        self, stack_max
    ):
        stack_max.push(5)
        assert 5 == stack_max.get_max()

    def test_get_max_with_2_elements_desc_should_return_the_max_at_each_point(
        self, stack_max
    ):
        stack_max.push(5)
        stack_max.push(4)

        assert 5 == stack_max.get_max()
        stack_max.pop()
        assert 5 == stack_max.get_max()

    def test_get_max_with_pushing_elements_asc_should_return_max_at_each_point(
        self, stack_max
    ):
        stack_max.push(1)
        stack_max.push(2)
        stack_max.push(3)
        stack_max.push(4)
        stack_max.push(5)

        assert 5 == stack_max.get_max()
        stack_max.pop()
        assert 4 == stack_max.get_max()
        stack_max.pop()
        assert 3 == stack_max.get_max()
        stack_max.pop()
        assert 2 == stack_max.get_max()
        stack_max.pop()
        assert 1 == stack_max.get_max()

    def test_get_max_with_complex_situation_should_return_correct_max_at_each_point(
        self, stack_max
    ):
        stack_max.push(10)
        stack_max.push(8)
        stack_max.push(20)
        stack_max.push(25)

        assert 25 == stack_max.get_max()

        stack_max.push(45)
        assert 45 == stack_max.get_max()

        stack_max.pop()
        stack_max.pop()
        assert 20 == stack_max.get_max()
