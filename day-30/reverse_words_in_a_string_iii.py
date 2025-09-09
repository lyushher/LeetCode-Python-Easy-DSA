# Problem: Reverse Words in a String III
# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Tags: String, Two Pointers
# Approach: Split the sentence by spaces, reverse each word individually,
#           and rejoin them with spaces.
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def reverseWords(self, s):
        return " ".join(word[::-1] for word in s.split())
