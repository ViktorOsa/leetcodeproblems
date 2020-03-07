class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        curr_element = self.root      
        while curr_element:
            curr_value = curr_element.value
            if new_val < curr_value:
                curr_element = curr_element.left
            else:
                curr_element = curr_element.right              
        curr_element = Node(new_val)

    def search(self, find_val):
        curr_element = self.root

        while curr_element:
            curr_value = curr_element.value
            if curr_value == find_val:
                return True
            elif find_val < curr_value:
                curr_element = curr_element.left
            else:
                curr_element = curr_element.right
        
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))