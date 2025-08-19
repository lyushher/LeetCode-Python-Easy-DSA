# Problem: Same Tree
# Link: https://leetcode.com/problems/same-tree/description/
# Tags: Tree, DFS, Recursion, BFS
# Approach: Compare nodes pairwise. If both are None, return True. If only one is None or values 
#           differ, return False. Otherwise recursively check left and right subtrees.
# Time Complexity: O(n) – visit each node once
# Space Complexity: O(h) – recursion stack or queue space, where h is the tree height


from collections import deque

class Solution:
    def isSameTree(self, p, q):
        dq = deque([(p, q)])
        while dq:
            a, b = dq.popleft()
            if not a and not b:
                continue
            if not a or not b or a.val != b.val:
                return False
            dq.append((a.left, b.left))
            dq.append((a.right, b.right))
        return True
