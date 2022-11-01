class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_all(self):
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def insert_empty(self, data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty")

LL1 = LinkedList()