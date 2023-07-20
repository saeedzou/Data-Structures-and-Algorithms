# Instructions:
# LL: Partition List (⚡Interview Question)
# You are given a singly linked list implementation in Python 
# that does not have a tail pointer 
# (which will make this method simpler to implement).

# You are tasked with implementing a method 
# partition_list(self, x) that will take an integer x and 
# partition the linked list such that all nodes with values 
# less than x come before nodes with values greater than or equal to x. 
# You should preserve the original relative order of the nodes in 
# each of the two partitions.

# You need to implement this method as a method of the LinkedList class. 
# The method should take an integer x as input. 
# If the linked list is empty, the method should return None.

# To implement this method, you should create two new linked lists. 
# These two linked lists will be made up of the original nodes 
# from the linked list that is being partitioned, 
# one for nodes less than x and one for nodes greater than or equal to x.  
# None of the nodes from the linked list should be duplicated.

# The creation of a limited number of new nodes is allowed 
# (e.g., dummy nodes to facilitate the partitioning process).

# You should then traverse the original linked list
#  and append each node to the appropriate new linked list.

# Finally, you should connect the two new linked lists together.

def partition_list(self, x):
    if self.length == 0:
        return None
    dummy_1 = Node(0)
    dummy_2 = Node(0)
    prev_1 = dummy_1
    prev_2 = dummy_2
    current = self.head
    
    while current:
        if current.value < x:
            prev_1.next = current
            prev_1 = current
        else:
            prev_2.next = current
            prev_2 = current
        current = current.next

    prev_2.next = None
    prev_1.next = dummy_2.next
    self.head = dummy_1.next