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
                print(n.data, "--->", end=' ')
                n = n.ref

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print('Node is not present in the LinkedList')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head == None:
            print('Linked List is empty')
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n is None:
            print('Element is not present in the Linked List')
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_before(500, 10)
LL1.add_before(50, 10)
print(LL1.print_all())