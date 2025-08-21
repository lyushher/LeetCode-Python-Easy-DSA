# Problem: Range Sum of BST
# Link: https://leetcode.com/problems/range-sum-of-bst/description/
# Tags: Tree, BST, DFS, Recursion
# Approach: Use BST properties to prune traversal. If node.val < low, skip the left subtree;
#           if node.val > high, skip the right subtree. Otherwise include node.val and recurse
#           into both sides. This avoids visiting irrelevant branches.
# Time Complexity: O(m) where m is the number of visited nodes (≤ n), best-case prunes large parts
# Space Complexity: O(h) recursion stack, where h is the tree height


class Solution:
    def rangeSumBST(self, root, low, high):
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)   # all left < root.val < low -> skip left
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)    # all right > root.val > high -> skip right
       
        # low <= root.val <= high
        return (root.val
                + self.rangeSumBST(root.left, low, high)
                + self.rangeSumBST(root.right, low, high))
