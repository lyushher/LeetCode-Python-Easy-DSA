# Problem: Min Stack  
# Link: https://leetcode.com/problems/min-stack/description/  
# Tags: Stack, Design, Data Structure  
# Approach: Maintain a secondary stack to track the minimum value at each push level for constant-time retrieval.  
# Time Complexity: O(1) for all operations  
# Space Complexity: O(n) – storing elements in both stacks  


class MinStack:
    def __init__(self):
        self.stack = []  # main stack to store all values
        self.min_stack = []  # min stack to store the current minimum at each level

    def push(self, val):
        self.stack.append(val)
        # push the new min value
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
