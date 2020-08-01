"""
modified from original in /stack
"""

# ## Array version


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def push(self, node):
        self.storage.append(node)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(self.size)
        else:
            return None
