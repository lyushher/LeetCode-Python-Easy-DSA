# Problem: Leaf-Similar Trees
# Link: https://leetcode.com/problems/leaf-similar-trees/description/
# Tags: Tree, DFS, Stack
# Approach: Collect the leaf sequence of each tree by a DFS that appends node values
#           only when a node is a leaf (no children). Compare the two sequences for equality.
#           This isolates order and values of leaves regardless of internal structure.
# Time Complexity: O(n + m) – visit each node of both trees once
# Space Complexity: O(h1 + h2) – recursion/stack depth for both trees (plus leaf lists)


class Solution:
    def leafSimilar(self, root1, root2):
        def leaves(root, out):
            if not root:
                return
            if not root.left and not root.right:
                out.append(root.val)
                return
            leaves(root.left, out)
            leaves(root.right, out)

        a, b = [], []
        leaves(root1, a)
        leaves(root2, b)
        return a == b
