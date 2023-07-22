# Instructions:
# DLL: Palindrome Checker (⚡Interview Question)
# Write a method to determine whether a given doubly linked list
# reads the same forwards and backwards.

# For example, if the list contains the values [1, 2, 3, 2, 1], 
# then the method should return True, since the list is a palindrome.

# If the list contains the values [1, 2, 3, 4, 5], 
# then the method should return False, since the list is not a palindrome.

# Method name:
# is_palindrome
def is_palindrome(self):
    # 1) find half of length = half
    # 2) go through the list half times
    # 3) create two counters, one at the head and one at tail
    # go through list and check if the counter from the head value
    # is the same as the counter starting at tail
    # O(n)
    if self.length <= 1:
        return True
    forward, backward = self.head, self.tail
    mid = int(self.length / 2)
    for _ in range(mid):
        if forward.value != backward.value:
            return False
        forward = forward.next
        backward = backward.prev
    return True