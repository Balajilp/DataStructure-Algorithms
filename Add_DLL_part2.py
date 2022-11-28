class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None 
        self.pref = None 


class Doubly_LL:
    def __init__(self):
        self.head = None 

    def print_all(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, end=' ')
                n = n.nref 
    
    def print_reverse_all(self):

        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref 

            while n is not None:
                print(n.data) 
                n = n.pref
     

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node 
        else:
            print("Linked list is not empty")

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            new_node.nref = self.head 
            self.head.pref = new_node 
            self.head = new_node 

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
        else:
            n = self.head 
            while n.nref is not None:
                n = n.nref 

            n.nref = new_node 
            new_node.pref = n

    def add_after(self, data, x):
        if self.head is None:
            print("Linked list empty!!!")
        else:
            n = self.head 
            while n is not None:
                if x == n.data:
                    break 
                n = n.nref 
            if n is None:
                print("given node is not present in the entire linked list")
            else:
                new_node = Node(data)
                new_node.nref = n.nref 
                new_node.pref = n 
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node 

    def add_before(self, data, x):
        if self.head is None:
            print("Linked list empty!!!")
        else:
            n = self.head 
            while n is not None:
                if x == n.data:
                    break 
                n = n.nref 
            if n is None:
                print("given node is not present in the entire linked list")
            else:
                new_node = Node(data)
                new_node.nref = n 
                new_node.pref = n.pref 
                if n.pref is not None:
                    n.pref.nref = new_node 
                else:
                    self.head = new_node 
                n.pref = new_node 



d = Doubly_LL()    

d.add_begin(10)
d.add_begin(20)
d.add_end(40)
d.add_end(50)
d.add_after(25, 20)
d.print_all()
