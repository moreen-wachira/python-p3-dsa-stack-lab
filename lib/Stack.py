class Stack:
    def __init__(self, limit=None):
        self.items = []
        self.limit = limit

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return self.limit is not None and len(self.items) == self.limit

    def size(self):
        return len(self.items)

    def push(self, item):
        if not self.is_full():
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise ValueError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise ValueError("Stack is empty")

    def search(self, value):
        try:
            index = self.items.index(value)
            return len(self.items) - index
        except ValueError:
            return -1
