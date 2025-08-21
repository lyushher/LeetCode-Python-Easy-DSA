# Problem: Path Sum
# Link: https://leetcode.com/problems/path-sum/
# Tags: Tree, DFS, Recursion, Binary Tree
# Approach: The solution applies a recursive DFS traversal. 
#           At each step, the current node’s value is subtracted from the target sum. 
#           If a leaf node is reached, the algorithm checks whether the remaining sum equals the leaf’s value. 
#           If so, a valid path exists and the function returns True. 
#           Otherwise, the recursion continues down the left and right subtrees, and the result is True if any root-to-leaf path satisfies the condition.
# Time Complexity: O(n) – visit each node once
# Space Complexity: O(h) – recursion stack, where h is the tree height


class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        # leaf check
        if not root.left and not root.right:
            return targetSum == root.val

        # DFS on children with reduced target
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
