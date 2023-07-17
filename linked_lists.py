# you can think of linked list as a set of nested dictionaries, with each
# dictionary having a single key-value pair and the value of that pair is
# another dictionary. except the value in the last dictionary is None.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create new Node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        # create new Node
        # add Node to end
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self, value):
        # create new Node
        # add Node to start
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        # create new Node
        # insert node
        pass
    
    def pop(self):
        # find next to tail node
        # set tail to that node
        # return the last node
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp


    def get(self, index):
        pass
    
    def set_value(self, index, value):
        pass
    
    def remove(self, index):
        pass

    def reverse(self):
        pass
    
        

new_ll = LinkedList(4)
new_ll.append(5)
new_ll.prepend(10)
new_ll.print_list()
new_ll.pop_first()
new_ll.print_list()
new_ll.pop_first()
new_ll.print_list()
new_ll.pop_first()
new_ll.print_list()