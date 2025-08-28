# Problem: Count Complete Tree Nodes
# Link: https://leetcode.com/problems/count-complete-tree-nodes/description/
# Tags: Binary Tree, DFS, Divide and Conquer, Binary Search
# Approach: 
#   Use the properties of complete binary trees. At each node, compute the height of the left
#   and right subtrees. If the heights are equal, the left subtree is perfect (completely filled),
#   so its node count is 2^h - 1; continue counting recursively on the right subtree. If the
#   heights differ, the right subtree is perfect with 2^h - 1 nodes, and recursion continues
#   on the left subtree. This reduces traversal significantly compared to naive DFS.
# Time Complexity: O((log n)^2) – computing height is O(log n) and we do it for O(log n) levels
# Space Complexity: O(log n) – recursion depth equal to the tree height


class Solution:
    def countNodes(self, root):
        if not root:
            return 0

        def getHeight(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        left_h = getHeight(root.left)
        right_h = getHeight(root.right)

        if left_h == right_h:
            # left subtree is perfect
            return (1 << left_h) + self.countNodes(root.right)
        else:
            # right subtree is perfect
            return (1 << right_h) + self.countNodes(root.left)
