from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        if s is None and t is not None:
            return False
        if self.compare(s, t):
            return True
        
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
    
    def compare(self, s, t):
        
        if s is None and t is None:
            return True
        elif s is None or t is None or s.val != t.val:
            return False
        
        return self.compare(s.left, t.left) and self.compare(s.right, t.right)
              

# TIME O(n * m) ,where n size of s, m size of t. 
# Time complexity: because for each node in S (n nodes) 
# we compare with a tree from t (m nodes)
# SPACE O(n) !!!
        