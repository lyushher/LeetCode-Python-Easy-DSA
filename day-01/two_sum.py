# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Tags: Array, Brute Force
# Approach: Brute Force (try all pairs)
# Time Complexity: O(n²)
# Space Complexity: O(1)


class Solution(object):
    def twoSum(self, nums, target):
        # iterate through each element in the array
        for i in range(len(nums)):
            # check all elements that come after the current one
            for j in range(i + 1, len(nums)):
                # if the sum of the two elements equals the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]
