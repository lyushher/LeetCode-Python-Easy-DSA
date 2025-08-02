# Problem: Missing Number  
# Link: https://leetcode.com/problems/missing-number/description/  
# Tags: Bit Manipulation, XOR  
# Approach: XOR all indices and values; matched pairs cancel out, leaving the missing number.  
# Time Complexity: O(n)  
# Space Complexity: O(1)  


class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        result = n  # start with 'n' since indices go from 0 to n

        for i in range(n):
            # XOR index and value at each step
            result ^= i ^ nums[i]
        return result

