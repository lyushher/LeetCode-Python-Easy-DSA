# Problem: Valid Parentheses  
# Link: https://leetcode.com/problems/valid-parentheses/description/  
# Tags: Stack, String, Bracket Matching  
# Approach: Use a stack to track opening brackets and match them against closing ones during traversal.  
# Time Complexity: O(n)  
# Space Complexity: O(n)


class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}

        for char in s:
            # if it's a closing bracket, check for match
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                # it's an opening bracket, push to stack
                stack.append(char)

        # if stack is empty, all brackets matched correctly
        return not stack

