# Problem: Summary Ranges
# Link: https://leetcode.com/problems/summary-ranges/
# Tags: Array, Two Pointers
# Approach: Track the start of each range, and whenever consecutive order breaks record the range and reset start; add the final range at the end.
# Time Complexity: O(n)
# Space Complexity: O(1) (excluding output)


class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []

        res = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1: 
                if start == nums[i-1]:
                    res.append(str(start)) 
                else:
                    res.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]    

        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(nums[-1]))

        return res
