"""
modified from the original in the /queue folder
"""


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, node):
        self.storage.append(node)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(0)
        else:
            return None
