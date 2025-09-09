# Problem: Keyboard Row
# Link: https://leetcode.com/problems/keyboard-row/description/
# Tags: String, Hash Set
# Approach: For each word, check if its letters are a subset of any one keyboard row.
# Time Complexity: O(n * k), n = number of words, k = average word length
# Space Complexity: O(1)


class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        result = []
        for word in words:
            wset = set(word.lower())
            if wset <= row1 or wset <= row2 or wset <= row3:
                result.append(word)
        return result
