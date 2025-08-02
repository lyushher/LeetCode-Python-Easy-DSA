# Problem: Single Number  
# Link: https://leetcode.com/problems/single-number/description/  
# Tags: Bit Manipulation, XOR  
# Approach: Use XOR to cancel out duplicate numbers. Since a ^ a = 0 and a ^ 0 = a, only the single number will remain.  
# Time Complexity: O(n)  
# Space Complexity: O(1)  


class Solution:
    def singleNumber(self, nums):
        # Start with 0 as the initial result
        # We'll use XOR to cancel out the numbers that appear twice
        result = 0

        for num in nums:
            # XOR each number with the current result
            # since a ^ a = 0 and a ^ 0 = a, all duplicates will cancel each other out
            result ^= num
        return result

