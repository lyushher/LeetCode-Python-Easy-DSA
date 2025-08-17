# Problem: Valid Perfect Square
# Link: https://leetcode.com/problems/valid-perfect-square/description/
# Tags: Math, Binary Search
# Approach: Apply binary search between 1 and num to check if there exists a mid 
#           such that mid*mid == num. Adjust boundaries accordingly until found 
#           or search space is empty.
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def isPerfectSquare(self, num):
        if num < 2:
            return True

        left, right = 1, num // 2

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
