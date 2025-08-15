# Problem: First Bad Version
# Link: https://leetcode.com/problems/first-bad-version/description/
# Tags: Binary Search
# Approach: Binary search over versions 1..n. If mid is bad, record it as a candidate
#           answer and move left to find an earlier bad version; otherwise move right.
#           The earliest bad version found during the search is returned.
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def firstBadVersion(self, n):
        left, right = 1, n
        ans = n
        
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                ans = mid      # mid is bad; try to find an earlier bad version
                right = mid - 1
            else:
                left = mid + 1     # mid is good; bad version must be to the right
              
        return ans

