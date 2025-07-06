from typing import List

class LinkedNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList():
    def __init__(self, values: List[int]=None):
        self.values = values if values is not None else []
        self.head = None
        self.tail = None
        self.__assign_nodes()
        

    def reverse(self, in_place: bool=False) -> 'DoubleLinkedList':
        """
        Reverse the double linked list in place.
        """
        if in_place:
            self.__reverse_in_place()
            return self
        else:
            return DoubleLinkedList(self.values[::-1])
        
    def insert_at_position(self, new_node: LinkedNode, position: int) -> None:
        if self.head is None:
            if position == 0:
                self.__assign_first_node(new_node)
                return
            else:
                raise IndexError("Position out of bounds for empty list.")
        if position < 0 or position > len(self.values):
            raise IndexError("Position out of bounds.")
        
        current = self.head
        current_position = 0
        while current_position < position:
            current = current.next
            current_position += 1

        previous_node = current.prev
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = current
        current.prev = new_node
        

    def to_list(self) -> List[int]:
        """
        Convert the double linked list to a Python list.
        """
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values        
    
    def __assign_nodes(self) -> None:
        """
        Assign nodes to the double linked list based on the values.
        """
        for value in self.values:
            new_node = LinkedNode(value)
            if not self.head:
                self.__assign_first_node(new_node)
            else:
                self.__append_new_node_to_non_empty_list(new_node)

    def __assign_first_node(self, new_node: LinkedNode) -> None:
        """
        Assign the first node to the double linked list.
        """
        self.head = new_node
        self.tail = new_node
        self.tail.next = None
        self.tail.prev = None
    
    def __append_new_node_to_non_empty_list(self, new_node: LinkedNode) -> None:
        """
        Add a new node to the non empty double linked list.
        """       
        new_node.prev = self.tail       
        self.tail.next = new_node        
        self.tail = new_node
        self.tail.next = None

    def __reverse_in_place(self) -> None:
        """
        Reverse the double linked list in place.
        """
        current = self.head
        prev_node = None
        
        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        
        self.head, self.tail = self.tail, self.head
                
    