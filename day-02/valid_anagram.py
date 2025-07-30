# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/description/
# Tags: String, Hash Table, Frequency Counter
# Approach: Hash Map (character frequency comparison)
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def isAnagram(self, s, t):
      
        # if the lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        # dictionary to count characters in string s
        count = {}

        # count each character in s
        for char in s:
            count[char] = count.get(char, 0) + 1

        # subtract each character found in t
        for char in t:
            if char not in count:
                return False  # character doesn't exist in s
            count[char] -= 1
            if count[char] < 0:
                return False  # more of this char in t than in s

        # all counts balanced, valid anagram
        return True


