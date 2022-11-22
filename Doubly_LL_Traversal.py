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
                print(n.data)
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
d = Doubly_LL()
d.print_reverse_all()

