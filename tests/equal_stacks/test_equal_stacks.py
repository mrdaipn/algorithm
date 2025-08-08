import pytest
from problems.equal_stacks.equal_stack import EqualStacks


class TestEqualStacks:

    @pytest.fixture()
    def equal_stack(self):
        return EqualStacks()

    def test_equal_stacks_of_3_stack_with_common_heigh_and_same_length_should_return_the_common_heigh(
        self, equal_stack
    ):
        h1 = [1, 2]
        h2 = [1, 1]
        h3 = [10, 2]

        assert 2 == equal_stack.compute_common_heigh(h1, h2, h3)

    def test_equal_stacks_of_3_stack_with_common_heigh_with_different_length_should_return_common(
        self, equal_stack
    ):
        h1 = [1, 2, 3]
        h2 = [1, 1, 1, 1, 1, 1]
        h3 = [3, 6, 7, 4, 1]

        assert 5 == equal_stack.compute_common_heigh(h1, h2, h3)

    def test_equal_stacks_of_3_stack_with_stack1_empty_should_return_0(
        self, equal_stack
    ):
        h1 = []
        h2 = [1, 1, 1, 1, 1, 1]
        h3 = [3, 6, 7, 4, 1]

        assert 0 == equal_stack.compute_common_heigh(h1, h2, h3)

    def test_equal_stacks_of_3_stack_with_stack1_None_should_return_0(
        self, equal_stack
    ):
        h1 = None
        h2 = [1, 1, 1, 1, 1, 1]
        h3 = [3, 6, 7, 4, 1]

        assert 0 == equal_stack.compute_common_heigh(h1, h2, h3)

    def test_equal_stacks_of_3_stack_with_stack2_None_should_return_0(
        self, equal_stack
    ):

        h1 = [2, 3, 5]
        h2 = None
        h3 = [3, 6, 7, 4, 1]

        assert 0 == equal_stack.compute_common_heigh(h1, h2, h3)

    def test_equal_stacks_of_3_stack_with_stack3_None_should_return_0(
        self, equal_stack
    ):

        h1 = [2, 3, 5]
        h2 = [3, 5, 6]
        h3 = None

        assert 0 == equal_stack.compute_common_heigh(h1, h2, h3)
