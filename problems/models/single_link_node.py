class SingleLinkNode:
    def __init__(self, value, next: "SingleLinkNode" = None):
        if not value:
            raise ValueError("value must be specified.")
        self.value = value
        self.next = next
