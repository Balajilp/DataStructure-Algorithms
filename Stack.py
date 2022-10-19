"""
1.  Last IN First Out (OR)  First In Last Out

Stack performs 4 operations:
1.  Push --> adds elements to the stack
2.  Pop  --> Removes elements from the stack
3.  Peek or top  -->  gives elements which present at the top
4.  Isempty  -->  Returns true if the stock is empty

Two ways we can implement stack data structure
1.  Python list
2.  Using built in modules
"""
#  Stack implementation using python list

#  Push -->  append method

stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

#  Pop  -->  Pop method


stack.pop()
print(stack)
print(stack.pop())
stack.pop()
print(not stack)

#  Sample program

stack1 = []

def push():
    element = input("Enter the element: ")
    stack1.append(element)
    print(stack1)
def pop_element():
    if not stack1:
        print("Stack is Empty")
    else:
        e = stack1.pop()
        print('Removed element is ', e)
        print(stack1)

while True:
    print("Select the operation 1. Push ,  2. Pop,  3. quit")
    choice = int(input("Enter the operation number :"))
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter  the correct operation")


#  Implement stack using the modules
#  Using collections module
import collections
stack2 = collections.deque()
print(stack2)

stack2.append(10)
stack2.append(20)
stack2.append(30)

print(stack2)

stack2.pop()
stack2.pop()

#  Implement using queue module

import queue
stack3 = queue.LifoQueue()
print(stack3)
stack3.put(10)
stack3.put(20)
stack3.put(30)
print(stack3)
stack3.get()