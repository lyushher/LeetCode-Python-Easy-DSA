# Problem: Balanced Binary Tree
# Link: https://leetcode.com/problems/balanced-binary-tree/description/
# Tags: Tree, DFS, Recursion, Divide and Conquer
# Approach: Use a post-order DFS that computes subtree heights and detects imbalance early.
#           For each node, obtain left and right heights; if either subtree is already
#           unbalanced or their height difference exceeds 1, propagate an unbalanced signal.
#           Otherwise return 1 + max(left_height, right_height). This short-circuits on the
#           first violation and visits each node once.
# Time Complexity: O(n)
# Space Complexity: O(h) where h is the tree height


class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return True, 0
            lb, lh = dfs(node.left)
            if not lb:
                return False, 0
            rb, rh = dfs(node.right)
            if not rb:
                return False, 0
            ok = abs(lh - rh) <= 1
            return ok, 1 + (lh if lh > rh else rh)

        ok, _ = dfs(root)
        return ok
