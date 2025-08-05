# Problem: Reverse String  
# Link: https://leetcode.com/problems/reverse-string/description/  
# Tags: Two Pointers, String, In-Place  
# Approach: Use two pointers to swap characters in-place, one from the start and one from the end.  
# Time Complexity: O(n)  
# Space Complexity: O(1)  


class Solution:
    def reverseString(self, s):
        # initialize two pointers at the start and end of the list
        left, right = 0, len(s) - 1

        # swap characters while moving the pointers toward each other
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

