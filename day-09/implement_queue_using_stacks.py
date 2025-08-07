# Problem: Implement Queue using Stacks  
# Link: https://leetcode.com/problems/implement-queue-using-stacks/description/  
# Tags: Stack, Queue, Design, Amortized Analysis  
# Approach: Maintain two stacks; push to in_stack and move elements to out_stack only when out_stack is empty for pop/peek.  
# Time Complexity: O(1) amortized for each operation  
# Space Complexity: O(n) – storing all elements in two stacks combined  


class MyQueue:
    def __init__(self):
        self.in_stack = []  # stack for incoming elements
        self.out_stack = []  # stack for outgoing elements

    def push(self, x):
        self.in_stack.append(x)  # always push to in_stack

    def pop(self):
        # if out_stack is empty, move all elements from in_stack to out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    def peek(self):
        # ensure out_stack has the current front element
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        # queue is empty if both stacks are empty
        return not self.in_stack and not self.out_stack



