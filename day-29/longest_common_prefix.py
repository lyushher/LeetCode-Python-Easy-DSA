# Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/description/
# Tags: String
# Approach: Take the first word as a template and compare each character index
#           against all other words; stop at the first mismatch or length overrun.
# Time Complexity: O(S) where S is the sum of all characters
# Space Complexity: O(1)


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        first = strs[0]
        for i in range(len(first)):
            ch = first[i]
            for w in strs[1:]:
                if i == len(w) or w[i] != ch:
                    return first[:i]
        return first
