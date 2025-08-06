# Problem: Remove Duplicates from Sorted Array  
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/  
# Tags: Two Pointers, Array, In-Place  
# Approach: Use two pointers to overwrite duplicates in-place as we iterate through the sorted array.  
# Time Complexity: O(n)  
# Space Complexity: O(1)  


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # pointer for the position of the next unique element
        k = 1

        for i in range(1, len(nums)):
          
            # if current element is different from the previous unique one
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
