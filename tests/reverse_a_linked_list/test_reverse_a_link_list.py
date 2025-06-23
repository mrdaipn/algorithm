from problems.reverse_a_linked_list.reverse_a_linked_list import (
    reverse_linked_list,
    ListNode,
)


def test_reverse_linked_list_basic_should_work():
    # Create a linked list: 1 -> 2 -> 3 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    # Reverse the linked list
    reversed_head = reverse_linked_list(head)
    # Check the values in the reversed linked list
    assert reversed_head.val == 3
    assert reversed_head.next.val == 2
    assert reversed_head.next.next.val == 1
    assert reversed_head.next.next.next is None


def test_reverse_linked_list_single_node_should_work():
    # Create a linked list with a single node: 1 -> None
    head = ListNode(1)
    # Reverse the linked list
    reversed_head = reverse_linked_list(head)
    # Check the value in the reversed linked list
    assert reversed_head.val == 1
    assert reversed_head.next is None


def test_reverse_linked_list_empty_should_work():
    # Create an empty linked list: None
    head = None
    # Reverse the linked list
    reversed_head = reverse_linked_list(head)
    # Check that the reversed linked list is still None
    assert reversed_head is None
