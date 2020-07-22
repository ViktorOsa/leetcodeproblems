from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor_rec(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        if root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestor(root.right, p, q)
        
        return root

# TIME : O(n) worst, O(log n) - average, because its like searching in BST
# SPACE : O(n) - recursion stack
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root

# TIME : O(n) worst, O(log n) - average, because its like searching in BST
# SPACE : O(1) - in iterative approach no extra space needed
