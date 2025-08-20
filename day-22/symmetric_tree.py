# Problem: Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/description/
# Tags: Tree, DFS, BFS, Recursion
# Approach: A tree is symmetric if left and right subtrees are mirror images.
#           Recursively check matching nodes on opposite sides.
# Time Complexity: O(n) – visit each node once
# Space Complexity: O(h) – recursion stack, h = tree height


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and 
                    isMirror(t1.left, t2.right) and 
                    isMirror(t1.right, t2.left))
        
        return isMirror(root.left, root.right)
