from problems.models import single_link_node


def detect_cycle_in_link_list(head: single_link_node) -> bool:
    """Detect if the single link list has a cycle"""
    visited_node = []
    current_node = head
    while current_node:
        if current_node.next in visited_node:
            return True
        
        visited_node.append(current_node)
        current_node = current_node.next

    return False