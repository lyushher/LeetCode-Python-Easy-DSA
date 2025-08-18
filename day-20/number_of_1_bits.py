# Problem: Number of 1 Bits
# Link: https://leetcode.com/problems/number-of-1-bits/description/
# Tags: Bit Manipulation
# Approach: Use Brian Kernighan’s Algorithm. Each operation n = n & (n - 1)
#           removes the lowest set bit, counting how many times until n = 0.
# Time Complexity: O(k), where k is the number of 1 bits (worst case O(32))
# Space Complexity: O(1)


class Solution:
    def hammingWeight(self, n):
        count = 0
        while n:
            n = n & (n - 1)  # remove lowest set bit
            count += 1
        return count
