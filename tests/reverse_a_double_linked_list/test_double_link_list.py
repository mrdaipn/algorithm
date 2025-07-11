import pytest
from problems.double_linked_list.double_linked_list import DoubleLinkedList, LinkedNode


def test_can_create_double_linked_list_correctly():
    double_linked_list = DoubleLinkedList([1, 2, 3])
    assert double_linked_list.to_list() == [1, 2, 3]

    assert isinstance(double_linked_list.head, LinkedNode)
    assert double_linked_list.head.value == 1

    assert isinstance(double_linked_list.head.next, LinkedNode)
    assert double_linked_list.head.next.value == 2

    assert isinstance(double_linked_list.tail, LinkedNode)
    assert double_linked_list.tail.value == 3
    assert double_linked_list.tail.prev.value == 2

    assert double_linked_list.tail.prev.next is double_linked_list.tail
    assert double_linked_list.head.next.prev is double_linked_list.head


def test_reverse_double_linked_list_to_new_list_with_normal_list():
    double_linked_list = DoubleLinkedList([1, 2, 3, 4, 5])
    reversed_linked_list = double_linked_list.reverse(in_place=False)
    assert reversed_linked_list.to_list() == [5, 4, 3, 2, 1]
    assert double_linked_list.to_list() == [1, 2, 3, 4, 5]
    assert double_linked_list.head.value == 1


def test_reverse_double_linked_list_in_place():
    double_linked_list = DoubleLinkedList([1, 2, 3, 4, 5])
    double_linked_list.reverse(in_place=True)
    assert double_linked_list.to_list() == [5, 4, 3, 2, 1]
    assert double_linked_list.head.value == 5
    assert double_linked_list.tail.value == 1
    assert double_linked_list.head.next.value == 4
    assert double_linked_list.tail.prev.value == 2


def test_reverse_empty_double_linked_list_should_work():
    double_linked_list = DoubleLinkedList([])
    reversed_linked_list = double_linked_list.reverse(in_place=False)
    assert reversed_linked_list.to_list() == []
    assert double_linked_list.to_list() == []


def test_insert_a_node_at_position_2_should_work():
    double_linked_list = DoubleLinkedList([1, 2, 3])
    new_node = LinkedNode(4)
    double_linked_list.insert_at_position(new_node, 2)
    assert double_linked_list.to_list() == [1, 2, 4, 3]


def test_insert_at_position_should_work_for_empty_list():
    double_linked_list = DoubleLinkedList([])
    new_node = LinkedNode(1)
    double_linked_list.insert_at_position(new_node, 0)
    assert double_linked_list.to_list() == [1]


def test_insert_at_position_should_raise_index_error_for_out_of_bounds():
    double_linked_list = DoubleLinkedList([1, 2, 3])
    new_node = LinkedNode(4)
    with pytest.raises(IndexError):
        double_linked_list.insert_at_position(new_node, 5)

    with pytest.raises(IndexError):
        double_linked_list.insert_at_position(new_node, -1)


def test_clone_double_linked_list_should_work():
    double_linked_list = DoubleLinkedList([1, 2, 3])
    cloned_list = double_linked_list.clone()
    assert isinstance(cloned_list, DoubleLinkedList)
    assert cloned_list.to_list() == [1, 2, 3]


def test_clone_empty_double_linked_list_should_work():
    double_linked_list = DoubleLinkedList([])
    cloned_list = double_linked_list.clone()
    assert isinstance(cloned_list, DoubleLinkedList)
    assert cloned_list.to_list() == []


def test_merge_2_double_linked_list__not_in_place_should_work():
    double_linked_list1 = DoubleLinkedList([1, 2, 3])
    double_linked_list2 = DoubleLinkedList([4, 5, 6])

    merged_list = double_linked_list1.merge(double_linked_list2)
    assert merged_list.to_list() == [1, 2, 3, 4, 5, 6]

    assert merged_list.head.value == 1
    assert merged_list.tail.value == 6
    assert merged_list.head.next.value == 2
    assert merged_list.tail.prev.value == 5


def test_merge_2_double_linked_list_in_place_should_work():
    double_linked_list1 = DoubleLinkedList([1, 2, 3])
    double_linked_list2 = DoubleLinkedList([4, 5, 6])

    double_linked_list1.merge(double_linked_list2, in_place=True)
    assert double_linked_list1.to_list() == [1, 2, 3, 4, 5, 6]

    assert double_linked_list1.head.value == 1
    assert double_linked_list1.tail.value == 6
    assert double_linked_list1.head.next.value == 2
    assert double_linked_list1.tail.prev.value == 5


def test_merge_empty_double_linked_list_should_work():
    double_linked_list1 = DoubleLinkedList([1, 2, 3])
    double_linked_list2 = DoubleLinkedList([])

    merged_list = double_linked_list1.merge(double_linked_list2)
    assert merged_list.to_list() == [1, 2, 3]

    assert merged_list.head.value == 1
    assert merged_list.tail.value == 3
    assert merged_list.head.next.value == 2
    assert merged_list.tail.prev.value == 2


def test_merge_empty_double_linked_list_in_place_should_work():
    double_linked_list1 = DoubleLinkedList([1, 2, 3])
    double_linked_list2 = DoubleLinkedList([])

    double_linked_list1.merge(double_linked_list2, in_place=True)
    assert double_linked_list1.to_list() == [1, 2, 3]

    assert double_linked_list1.head.value == 1
    assert double_linked_list1.tail.value == 3
    assert double_linked_list1.head.next.value == 2
    assert double_linked_list1.tail.prev.value == 2


def test_merge_2_empty_double_linked_list_should_work():
    double_linked_list1 = DoubleLinkedList([])
    double_linked_list2 = DoubleLinkedList([])

    merged_list = double_linked_list1.merge(double_linked_list2)
    assert merged_list.to_list() == []

    assert merged_list.head is None
    assert merged_list.tail is None


def test_merge_2_empty_double_linked_list_in_place_should_work():
    double_linked_list1 = DoubleLinkedList([])
    double_linked_list2 = DoubleLinkedList([])

    double_linked_list1.merge(double_linked_list2, in_place=True)
    assert double_linked_list1.to_list() == []

    assert double_linked_list1.head is None
    assert double_linked_list1.tail is None


def test_merge_double_linked_list_with_self_should_raise_error():
    with pytest.raises(ValueError):
        double_linked_list = DoubleLinkedList([1, 2, 3])
        double_linked_list.merge(double_linked_list, in_place=True)


def test_sort_a_double_linked_list_should_work():
    double_linked_list = DoubleLinkedList([4, 3, 7])
    result = double_linked_list.sort(ascending=True)
    assert result.to_list() == [3, 4, 7]
