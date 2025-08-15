# Problem: Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/description/
# Tags: Array, Binary Search
# Approach: Use binary search to find the target index in a sorted array. If not found, 
#           the left pointer at the end of the search loop will indicate the correct 
#           insertion position to maintain sorted order.
# Time Complexity: O(log n)
# Space Complexity: O(1) 


class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
