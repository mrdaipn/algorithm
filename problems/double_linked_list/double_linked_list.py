from typing import List


class LinkedNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, values: List[int] = None):
        self.head = None
        self.tail = None
        self.__length = 0
        self.__assign_nodes(values)

    def reverse(self, in_place: bool = False) -> "DoubleLinkedList":
        """
        Reverse the double linked list in place.
        """
        if in_place:
            self.__reverse_in_place()
            return self
        else:
            return self.__reverse_clone()

    def insert_at_position(self, new_node: LinkedNode, position: int) -> None:
        if self.head is None:
            if position == 0:
                self.__assign_first_node(new_node)
                return
            else:
                raise IndexError("Position out of bounds for empty list.")
        if position < 0 or position > self.__length:
            raise IndexError("Position out of bounds.")

        if position == 0:
            self.__insert_to_the_first(new_node)
            return

        if position == self.__length:
            self.__insert_node_to_the_end(new_node)
            return

        current = self.find_node_at_possition(position)

        if current is None:  # Insert at the end
            self.__append_new_node_to_non_empty_list(new_node)
        else:
            self.__insert_in_the_middle_of_the_list(new_node, current)
        self.__length += 1

    def find_node_at_possition(self, position):
        current = self.head
        current_position = 0
        while current_position < position:
            current = current.next
            current_position += 1
        return current

    def clone(self) -> "DoubleLinkedList":
        """
        Clone the double linked list.
        """
        cloned_list = DoubleLinkedList()
        current = self.head
        current_position = 0
        while current:
            cloned_list.insert_at_position(LinkedNode(current.value), current_position)
            current = current.next
            current_position += 1
        return cloned_list

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

    def merge(self, other: "DoubleLinkedList", in_place=False) -> "DoubleLinkedList":
        """
        Merge another double linked list into this one.
        """
        if other is self:
            raise ValueError(
                "Cannot merge a double linked list with itself with in place mode."
            )

        if in_place:
            self.__merge_in_place(other)
            return self
        else:
            return self.__merge_clone(other)

    def sort(self, ascending=True):
        """
        Return a sorted doubled linked list
        """
        if ascending:
            return self.__sort_ascending()
        else:
            return self.__sort_descending()

    def __sort_ascending(self) -> "DoubleLinkedList":
        result = DoubleLinkedList()
        current_node = self.head
        while current_node:
            result.__order_insert(current_node.value)
            current_node = current_node.next

        return result

    def __order_insert(self, value) -> None:
        new_node = LinkedNode(value=value)
        current_node = self.head
        position = 0
        while current_node and current_node.value < value:
            current_node = current_node.next
            position += 1

        self.insert_at_position(new_node, position)

    def __insert_to_the_first(self, new_node: LinkedNode) -> None:
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.__length += 1

    def __insert_node_to_the_end(self, new_node) -> None:
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.__length += 1

    def __sort_descending(self):
        ascending = self.__sort_ascending()
        descending = ascending.reverse(in_place=False)
        return descending

    def __assign_nodes(self, values) -> None:
        """
        Assign nodes to the double linked list based on the values.
        """
        if not values:
            return
        length = len(values)
        for value in values:
            new_node = LinkedNode(value)
            if not self.head:
                self.__assign_first_node(new_node)
            else:
                self.__append_new_node_to_non_empty_list(new_node)

        self.__length = length

    def __assign_first_node(self, new_node: LinkedNode) -> None:
        """
        Assign the first node to the double linked list.
        """
        self.head = new_node
        self.tail = new_node
        self.tail.next = None
        self.tail.prev = None
        self.__length = 1

    def __append_new_node_to_non_empty_list(self, new_node: LinkedNode) -> None:
        """
        Add a new node to the non empty double linked list.
        """
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.tail.next = None

    def __insert_in_the_middle_of_the_list(self, new_node, current):
        previous_node = current.prev
        previous_node.next = new_node
        new_node.prev = previous_node
        new_node.next = current
        current.prev = new_node

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

    def __reverse_clone(self) -> "DoubleLinkedList":
        """
        Reverse the double linked list and return a new list.
        """
        reversed_list = DoubleLinkedList()
        current = self.tail
        current_possition = 0
        while current:
            reversed_list.insert_at_position(
                LinkedNode(current.value), current_possition
            )
            current = current.prev
            current_possition += 1

        return reversed_list

    def __merge_in_place(self, other: "DoubleLinkedList") -> None:
        """
        Merge another double linked list into this one in place.
        """
        if not other.head:
            return

        if not self.head:
            self.head = other.head
            self.tail = other.tail
            self.__length = other.__length
            return

        self.tail.next = other.head
        other.head.prev = self.tail
        self.tail = other.tail
        self.__length += other.__length

    def __merge_clone(self, other: "DoubleLinkedList") -> "DoubleLinkedList":
        """
        Merge another double linked list into this one and return a new list.
        """
        merged_list = DoubleLinkedList()
        merged_list = merged_list.merge(self, in_place=True)
        merged_list = merged_list.merge(other, in_place=True)
        return merged_list
