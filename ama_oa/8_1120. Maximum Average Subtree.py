# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        
        self.res = 0
        
        def helper(root):
            if not root: return [0, 0.0]
            c1, sum1 = helper(root.left)
            c2, sum2 = helper(root.right)
            counter = c1 + c2 + 1
            sum_all = sum1 + sum2 + root.val
            self.res = max(self.res, sum_all / counter)
            return [counter, sum_all]
        helper(root)
        return self.res
    
    
# Time O(N)
# Space O(H)