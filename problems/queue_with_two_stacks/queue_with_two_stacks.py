class CubeWithTwoStacks():
    def __init__(self):
        self.__forward_stack = []
        self.__backward_stack = []

    def enqueue(self, value) -> None:        
        self.__move_elements(self.__forward_stack, self.__backward_stack)
        self.__forward_stack.append(value)
        self.__move_elements(self.__backward_stack, self.__forward_stack)

    def dequeue(self) -> int:
        if not self.__forward_stack:
            return None
        return self.__forward_stack.pop()
        
    
    def length(self) -> int:
        return len(self.__forward_stack)
    
    def peek(self) -> int:
        return self.__forward_stack[-1] if self.__forward_stack else None

    def __move_elements(self, source, destination) -> None:
        while source:
            v = source.pop()
            destination.append(v)    