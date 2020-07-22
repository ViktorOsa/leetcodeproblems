from typing import List

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return []
        
        answer = []
        
        queue = deque([(0, root)])
        
        while len(queue) != 0:
            index, node = queue.popleft()
            if index >= len(answer):
                answer.append([node.val])
            else:
                answer[index].append(node.val)
            
            if node.left:
                queue.append((index+1, node.left))
            if node.right:
                queue.append((index +1, node.right))
            
        
        
        return answer

# TIME O(n)
# SPACE O(n)


    def levelOrder_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels

# SAme time and space complexity