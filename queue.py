"""
first in last out (or) last in first out, insertion and removal happens in a different end
queue = []
queue.append(10)
queue.append(20)
queue.append(30)

# deleting element from the queue

queue.pop(0)
queue.pop(0)
queue.pop(0)
"""
# we can insert the element in a different side and removes the element in different side

queue = []
queue.insert(0, 30)
queue.insert(0, 20)
queue.insert(0, 10)

# no we can remove the element

queue.pop()
queue.pop()
queue.pop()
