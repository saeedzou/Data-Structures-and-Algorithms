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
        pass

    def prepend(self, value):
        # create new Node
        # add Node to start
        pass
    def insert(self, index, value):
        # create new Node
        # insert node
        pass

new_ll = LinkedList(4)
new_ll.print_list()