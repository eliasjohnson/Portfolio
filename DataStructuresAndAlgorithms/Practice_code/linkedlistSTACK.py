# The linked list has two methods addHead(item) and removeHead() that run in constant time. These two methods are suitable to implement a stack. 

# getSize()– Get the number of items in the stack.
# isEmpty() – Return True if the stack is empty, False otherwise.
# peek() – Return the top item in the stack. If the stack is empty, raise an exception.
# push(value) – Push a value into the head of the stack.
# pop() – Remove and return a value in the head of the stack. If the stack is empty, raise an exception.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    #initializing a stack
    # using a dummy node 
    # which is used for handling edge cases
    def __init__(self):
        self.head = Node("Head")
        self.size = 0
    
    # string representation of a stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    # get current size of the stack
    def getSize(self):
        return self.size

    # check if the stack is empty 
    def isEmpty(self):
        return self.size == 0

    # peek the top of the stack
    def peek():
        pass
