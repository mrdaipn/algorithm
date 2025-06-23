class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list(head: ListNode) -> ListNode:
    """Reverses a singly linked list.

    Args:
        head (ListNode): The head of the linked list to reverse."""
    if not head:
        return head

    current_node = head
    next_node = current_node.next
    while next_node:
        next_node_next = next_node.next
        next_node.next = current_node
        if current_node is head:
            current_node.next = None

        current_node = next_node
        next_node = next_node_next

    head = current_node
    return head
