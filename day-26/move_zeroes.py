# Problem: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/description/
# Tags: Array, Two Pointers
# Approach: Use a two-pointer method to overwrite non-zero values in order,
#           then fill remaining positions with zeros.
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def moveZeroes(self, nums):
        last_non_zero = 0      # position to place next non-zero
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero] = nums[i]
                last_non_zero += 1
        
        # fill the rest with zeros
        for i in range(last_non_zero, len(nums)):
            nums[i] = 0


