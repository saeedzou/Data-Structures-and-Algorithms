# Big O determines the worst case scenario for an algorithm. 
# It is the way to measure the efficiency of an algorithm.
# Omega is the best case scenario for an algorithm.
# Theta is the average case scenario for an algorithm.

# O(n) Linear Time
## O(n) describes an algorithm whose performance will grow
## linearly and in direct proportion to the size of the input data set.
def print_items(n):
    for i in range(n):
        print(i)

# O(1) Constant Time
## O(1) describes an algorithm that will always execute in the same time
## (or space) regardless of the size of the input data set.
def add_items(n):
    return n + n + n

# O(n^2) Quadratic Time
## O(n^2) represents an algorithm whose performance is directly proportional
## to the square of the size of the input data set.
def print_pairs(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

def print_triplets(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)

## O(a * b) represents this algorithm
def print_pairs(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

# O(log n) Logarithmic Time
## O(log n) denotes an algorithm whose growth rate decreases quickly as the
## data set increases in size.
## search for an element in a sorted array
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) / 2
        if array[mid] > target:
            high = mid - 1
        elif array[mid] < target:
            low = mid + 1
        else:
            return mid

    return None

# O(n log n) Log Linear Time
## O(n log n) is the best sorting algorithm

# Big O lists
## appending or popping from the end of a list is O(1)
## inserting or removing from the beginning of a list is O(n)
## so is inserting or removing from any arbitrary position
## since it requires shifting all the following elements over by one
## because of the worst case scenario
## searching for an element in a list is O(n)
## looking up an element by index is O(1)

# Wrap up
## O(1) is constant
## O(log n) is divide and conquer
## O(n) is proportional
## O(n^2) is loop withing a loop

# References
## https://www.bigocheatsheet.com/
