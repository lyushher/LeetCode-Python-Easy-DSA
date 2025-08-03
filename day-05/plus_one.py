# Problem: Plus One  
# Link: https://leetcode.com/problems/plus-one/description/  
# Tags: Array, Math, Simulation  
# Approach: Traverse the digits from the end and simulate addition with carry. Replace 9s with 0s until a digit < 9 is found, or insert 1 at the front.  
# Time Complexity: O(n)  
# Space Complexity: O(1)   


class Solution:
    def plusOne(self, digits):
        # start from the last digit and move left
        for i in range(len(digits) - 1, -1, -1):
            # if current digit is less than 9, just increment and return
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # if digit is 9, set it to 0 and continue
            digits[i] = 0
        
        # if loop completes, all digits were 9 - need extra 1 at the front
        return [1] + digits
