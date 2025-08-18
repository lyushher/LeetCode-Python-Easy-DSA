# Problem: Power of Two
# Link: https://leetcode.com/problems/power-of-two/description/
# Tags: Math, Bit Manipulation
# Approach: A power of two has only one bit set in its binary representation.
#           Check positivity and apply the condition n & (n - 1) == 0.
# Time Complexity: O(1)
# Space Complexity: O(1)


class Solution:
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0
