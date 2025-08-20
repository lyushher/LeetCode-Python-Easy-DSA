# Problem: Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/description/
# Tags: Tree, Recursion, DFS
# Approach: Swap left and right children recursively
# Time Complexity: O(n)
# Space Complexity: O(h) where h is height of tree


class Solution:
    def invertTree(self, root):
        if not root:
            return None

        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
