class StackMax:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def get_max(self):
        if not self.max_stack:
            raise ValueError("Stack is empty.")

        return self.max_stack[-1]

    def push(self, value):
        self.stack.append(value)
        if self.max_stack:
            self.max_stack.append(
                value if value > self.max_stack[-1] else self.max_stack[-1]
            )
        else:
            self.max_stack.append(value)

    def pop(self):
        self.max_stack.pop()
        return self.stack.pop()
