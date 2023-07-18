# Instructions:
# LL: Find Kth Node From End (⚡Interview Question)
# Method name:
# find_kth_from_end

# Find the item that is a certain number of steps away from the 
# end of the linked list WITHOUT USING LENGTH.

# For example, let's say you want to find the item that is 3 steps
# away from the end of the LL. To do this, you would start from 
# the head of the LL and move through the links until you reach 
# the item that is 3 steps away from the end.

# This is the problem of finding the "kth node from the end" 
# of a linked list. Your task is to write a program that takes
# as input a linked list and a number k, and returns the item
# that is k steps away from the end of the list. 
# If the linked list has fewer than k items, the program should return None.

## So we should have 2 pointers, starting at the head
## one should go k steps ahead at first
## then they should go step by step until the 
## first one hits None(end of list)
## then the second one points to the kth node
## at the end
def find_kth_node_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast:
            fast = fast.next
        else:
            return None
    while fast:
        fast = fast.next
        slow = slow.next
    return slow
