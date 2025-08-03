# Problem: Find the Index of the First Occurrence in a String  
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/  
# Tags: String, Substring Search, Sliding Window  
# Approach: Slide a window of length equal to needle across haystack. At each step, compare substring with needle. Return the first matching index, or -1 if not found.  
# Time Complexity: O(n * m)   – where n = len(haystack), m = len(needle)  
# Space Complexity: O(1)      – no extra space used beyond variables  


class Solution:
    def strStr(self, haystack, needle):
        # edge case: empty needle
        if needle == "":
            return 0

        # sliding window comparison
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
      
              return i
      return -1

