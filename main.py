class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List_1:
    def __init__(self, data):
        new_node = Node(data)
        self.start_node = new_node

    def print_1(self):
        n = self.start_node
        while n is not None:
            print(n.data, end=" ")
            n = n.next

    def insert_start(self, data):
        new_node = Node(data)
        new_node.next = self.start_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node

    def perevorot(self):
        n = self.start_node
        a = n
        while n.next:
            n = n.next
        n.next = a

    def poriadok(self):
        n = self.start_node
        while n.next:
            if(n.data > n.next.data):
                a = n.data
                n.data = n.next.data
                n.next.data = a



l1 = List_1(4)
l1.insert_start(4)
l1.insert_start(8)
l1.insert_start(3)
l1.insert_end(28)
l1.print_1()
l1.poriadok()
l1.print_1()
l1.perevorot()
l1.print_1()
