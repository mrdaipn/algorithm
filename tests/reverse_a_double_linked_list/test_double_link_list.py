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