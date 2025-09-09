# Problem: Find All Numbers Disappeared in an Array
# Link: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Tags: Array, Hashing, In-Place Modification
# Approach: Iterate over the array and mark visited numbers by flipping the sign
#           at the corresponding index. At the end, indices with positive values
#           indicate missing numbers.
# Time Complexity: O(n)
# Space Complexity: O(1) (ignoring output list)


class Solution:
    def findDisappearedNumbers(self, nums):
        for x in nums:
            idx = abs(x) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]
        
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
