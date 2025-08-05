# Problem: First Unique Character in a String  
# Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/  
# Tags: Hash Map, String, Counting  
# Approach: Count character frequencies using Counter, then scan for the first index with a unique character.  
# Time Complexity: O(n)  
# Space Complexity: O(1) 


from collections import Counter

class Solution:
    def firstUniqChar(self, s):
        # count frequency of each character
        freq = Counter(s)

        # iterate through string to find first character with count 1
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i

        return -1

