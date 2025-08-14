# Problem: Binary Search
# Link: https://leetcode.com/problems/binary-search/description/
# Tags: Array, Binary Search
# Approach: Use two pointers (left and right) to repeatedly divide the search range in half 
#           until the target is found or the range becomes empty.
# Time Complexity: O(log n)
# Space Complexity: O(1) – only constant extra space used


class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
