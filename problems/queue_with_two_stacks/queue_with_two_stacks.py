class CubeWithTwoStacks():
    def __init__(self):
        self.__stack1 = []
        self.__stack2 = []
        self.__length = 0

    @property
    def length(self):
        return self.__length
    
    def enqueue(self, value) -> None:        
       self.__stack1.append(value)
       self.__length += 1

    def dequeue(self) -> int:
        self.__fill_stack2_if_empty()        
        self.__length -= 1
        return self.__stack2.pop() if self.__stack2 else None
    
    
    def peek(self) -> int:
        self.__fill_stack2_if_empty()
        return self.__stack2[-1] if self.__stack2 else None

    def __fill_stack2_if_empty(self) -> None:
        if not self.__stack2:
            while self.__stack1:
                self.__stack2.append(self.__stack1.pop())