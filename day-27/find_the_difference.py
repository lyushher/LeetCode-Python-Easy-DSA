# Problem: Find the Difference
# Link: https://leetcode.com/problems/find-the-difference/description/
# Tags: String, Bit Manipulation, Hashing
# Approach: XOR yöntemi: Aynı karakterler birbirini yok eder, geriye sadece eklenen
#           karakter kalır. Tüm s ve t karakterlerini XOR’layıp sonucu döndür.
# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def findTheDifference(self, s, t):
        x = 0
        for ch in s:
            x ^= ord(ch)
        for ch in t:
            x ^= ord(ch)
        return chr(x)
