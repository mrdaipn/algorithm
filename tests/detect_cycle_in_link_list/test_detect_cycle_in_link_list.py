from problems.detect_cycle_in_link_list.detect_cycle_in_link_list import detect_cycle_in_link_list
from problems.models.single_link_node import SingleLinkNode

def test_detect_cycle_in_link_list_with_a_cycle_should_return_true():
    head = SingleLinkNode(1)
    node2 = SingleLinkNode(2)
    node3 = SingleLinkNode(3)
    node4 = SingleLinkNode(4)
    node5 = SingleLinkNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3
    
    assert True == detect_cycle_in_link_list(head)


def test_detect_cycle_in_link_list_with_no_cycle_should_return_false():
    head = SingleLinkNode(1)
    node2 = SingleLinkNode(2)
    node3 = SingleLinkNode(3)
    node4 = SingleLinkNode(4)
    node5 = SingleLinkNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5    
    
    assert False == detect_cycle_in_link_list(head)