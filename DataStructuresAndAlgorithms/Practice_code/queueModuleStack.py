# stack implementation using queue module Lifoqueue
from queue import LifoQueue

stack = LifoQueue(maxsize=3)

print(stack.qsize())

stack.put(1)
stack.put(2)
stack.put(3)

print("Full: ", stack.full())
print("Size: ", stack.qsize())
 
# get() function to pop
# element from stack in
# LIFO order
print('\nElements popped from the stack')
print(stack.get())
print(stack.get())
print(stack.get())

print("\nEmpty: ", stack.empty())


