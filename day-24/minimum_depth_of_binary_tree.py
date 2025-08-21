# Problem: Minimum Depth of Binary Tree
# Link: https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Tags: Binary Tree, DFS, Recursion, BFS
# Approach: The minimum depth is the length of the shortest root-to-leaf path.
#           Use DFS: if one child is None, you must take the other (a missing child
#           doesn't form a leaf). Otherwise take 1 + min(leftDepth, rightDepth).
# Time Complexity: O(n)
# Space Complexity: O(h)  # h = tree height (recursion stack)


class Solution:
    def minDepth(self, root):
        if not root:
            return 0

        # if one child is missing, must go through the other
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
