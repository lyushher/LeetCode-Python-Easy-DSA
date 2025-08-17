# Problem: Sqrt(x)
# Link: https://leetcode.com/problems/sqrtx/description/
# Tags: Math, Binary Search
# Approach: Apply binary search between 0 and x to find the integer square root.
#           Adjust boundaries based on mid*mid comparison with x and return the
#           floor of the square root.
# Time Complexity: O(log n)
# Space Complexity: O(1)
  

class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x

        left, right = 1, x // 2
        ans = 1

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid   # candidate
                left = mid + 1
            else:
                right = mid - 1

        return ans

