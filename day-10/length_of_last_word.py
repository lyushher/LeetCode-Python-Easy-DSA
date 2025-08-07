# Problem: Length of Last Word  
# Link: https://leetcode.com/problems/length-of-last-word/description/  
# Tags: String  
# Approach: Trim spaces and split into words, then measure the length of the last element.  
# Time Complexity: O(n)  
# Space Complexity: O(n) – due to word list creation  


class Solution:
    def lengthOfLastWord(self, s):
        # remove trailing spaces and split into words
        words = s.strip().split()
        # return length of the last word
        return len(words[-1])
