class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class rBinarySearchTree:
    def __init__(self):
        self.root = None
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if current_node.value < value:
            current_node.right = self.__r_insert(current_node.right, value)
        if current_node.value > value:
            current_node.left = self.__r_insert(current_node.left, value)
        return current_node

    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if current_node.value > value:
            return self.__r_contains(current_node.left, value)
        else:
            return self.__r_contains(current_node.right, value)
    
    def r_delete(self, value):
        self.__r_delete(self.root, value)

    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if current_node.value > value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif current_node.value < value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            # 1) leaf nodes
            if current_node.left is None and current_node.right is None:
                return None
            # 2) have nodes to the left
            elif current_node.right is None:
                return current_node.left
            # 3) have nodes to the right
            elif current_node.left is None:
                return current_node.right
            # 4) have nodes to both sides
            else:
                min_val = self.min_value(current_node.right)
                current_node.value = min_val
                current_node.right = self.__r_delete(current_node.right, min_val)
        return current_node
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

