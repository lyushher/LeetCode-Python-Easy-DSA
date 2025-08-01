# Problem: Majority Element
# Link: https://leetcode.com/problems/majority-element/description/
# Tags: Array, Boyer-Moore Voting
# Approach: Boyer–Moore Voting Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def majorityElement(self, nums):
        candidate = None
        count = 0

        # iterate through the array to find the majority candidate
        for num in nums:
            if count == 0:
                candidate = num  

            count += 1 if num == candidate else -1

        return candidate

