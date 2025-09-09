# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# Tags: String, Sliding Window, Hash Map
# Approach: Use a sliding window with a dict mapping char -> last index.
#           Move 'right' over s; when a repeat is seen, jump 'left' to
#           max(left, last_index + 1). Track the maximum window length.
# Time Complexity: O(n)
# Space Complexity: O(k) where k is the charset size


class Solution:
    def lengthOfLongestSubstring(self, s):
        last = {}          # char -> last index
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1   # shrink window past the repeat
            last[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len
