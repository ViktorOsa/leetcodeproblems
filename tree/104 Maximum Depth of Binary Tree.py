from typing import List
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        depth = 0
        
        stack = [(1, root)]
        
        while len(stack) != 0:
            cur_depth, node = stack.pop(0)
            if node is not None:
                depth = max(depth, cur_depth)
            
                stack.append((cur_depth + 1, node.right))
                stack.append((cur_depth + 1, node.left))
            
            
        
        return depth

# TIME O(n)
# SPACE O(n) - worst, O(log n) - average