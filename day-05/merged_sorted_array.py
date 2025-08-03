# Problem: Merge Sorted Array  
# Link: https://leetcode.com/problems/merge-sorted-array/description/  
# Tags: Two Pointers, In-place, Array, Sorting  
# Approach: Start merging from the end of nums1 to avoid overwriting. Use two pointers to compare elements from nums1 and nums2 in reverse.  
# Time Complexity: O(n + m)  
# Space Complexity: O(1)  


class Solution:
    def merge(self, nums1, m, nums2, n):
        # set pointers to the end of both arrays
        p1 = m - 1  # last valid element in nums1
        p2 = n - 1  # last element in nums2
        p = m + n - 1  # last position in nums1

        # merge from the end to avoid overwriting elements in nums1
        while p1 >= 0 and p2 >= 0:
          
            # place the larger value at the current position from the back
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # if any elements remain in nums2, copy them over
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
