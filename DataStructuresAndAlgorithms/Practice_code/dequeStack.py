from collections import deque

stack = deque()

# now append items (push)

stack.append('hi')
stack.append('bye bye')
stack.append("fuck off mate")

print("initial stack")
print(stack)

# pop some elements in LAST IN FIRST OUT 
stack.pop()
print(stack)
stack.pop()
print(stack)

