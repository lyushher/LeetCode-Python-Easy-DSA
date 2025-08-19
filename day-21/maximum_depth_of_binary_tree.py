# Problem: Maximum Depth of Binary Tree
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Tags: Tree, DFS, Recursion
# Approach: Recursively compute 1 + max(depth of left, depth of right).
#           An empty node has depth 0, and leaf returns 1.
# Time Complexity: O(n)  - visit each node once
# Space Complexity: O(h) - recursion stack, h = tree height (worst O(n), best O(log n))


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + (left if left > right else right)

