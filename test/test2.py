# binary tree node
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def bstDistance(num, values, node1, node2):
    
    is_node1 = False
    is_node2 = False
    
    if node1 is None or node2 is None or num == 0:
        return -1

    # 1. Construct BST from array
    root = None
    for el in values:
        root = insert_in_bst(root, el)
        if el == node1:
            is_node1 = True
        if el == node2:
            is_node2 = True
    
    # 2. check if nodes are not in the values
    if not is_node1 or not is_node2 :
        return -1
        
    # 3. Find lowest common parent for node1 and node2
    lcp = find_lowest_common_parent(root, node1, node2)
    
    # 4. calculate height for both nodes
    height1 = calculate_height(lcp, node1)
    height2 = calculate_height(lcp, node2)
    
    return height1 + height2    


def calculate_height(root, node):
    
    if root.val == node:
        return 0
    
    if node < root.val:
        return calculate_height(root.left, node) + 1
    else:
        return calculate_height(root.right, node) + 1


def find_lowest_common_parent(root, node1, node2):

    # recursive way to find lowest common parent
    
    if root.val > node1 and root.val >node2:
        root = find_lowest_common_parent(root.left, node1, node2)
    elif root.val < node1 and root.val < node2:
        root = find_lowest_common_parent(root.right, node1, node2)
    
    return root


def insert_in_bst(root, value):

    if not root:
        return TreeNode(val = value)
        
    if value < root.val:
        root.left = insert_in_bst(root.left, value)
    else:
        root.right = insert_in_bst(root.right, value)
    
    return root
        
        
        
        
        
        
        
        
