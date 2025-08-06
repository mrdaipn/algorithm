class SimpleTextEditor:

    def __init__(self, initial_str: str):
        self.__initial_str = initial_str
        self.__current_str = initial_str
        self.__current_str_stack = []

    @property
    def initial_str(self):
        return self.__initial_str

    @property
    def current_str(self):
        return self.__current_str

    def append(self, s: str) -> None:
        self.__current_str_stack.append(self.__current_str)
        self.__current_str += s

    def delete_last(self, k: int) -> None:
        """Delete last k characters"""
        self.__current_str_stack.append(self.current_str)
        if len(self.__current_str) <= k:
            self.__current_str = ""
        else:
            self.__current_str = self.__current_str[0 : len(self.__current_str) - k]

    def print(self, k: int):
        if k >= 0 and k <= len(self.__current_str):
            print(self.__current_str[k - 1])
            return self.__current_str[k - 1]
        else:
            return ""

    def undo(self):
        if self.__current_str_stack:
            self.__current_str = self.__current_str_stack.pop()
