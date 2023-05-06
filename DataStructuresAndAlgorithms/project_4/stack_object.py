
class StackObject:
    """Creates a StackObject() object with item = 1 and next = None"""

    def __init__(self, item):
        """inits StackObject object with pointer to None and item = item"""
        self.item = item
        self.next = None
        self.priority = None

    def get_item(self):
        """get_item() returns self.item"""
        return self.item

    def set_priority(self, value):
        """set_priority(value) sets priority to value"""
        self.priority = value

    def get_priority(self):
        """get_priority() returns self.priority"""
        return self.priority

    def set_next(self, node):
        """set_next(node) sets pointer to node"""
        self.next = node

    def get_next(self):
        """get_next() returns self.next"""
        return self.next
