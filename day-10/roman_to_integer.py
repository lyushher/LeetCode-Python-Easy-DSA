# Problem: Roman to Integer  
# Link: https://leetcode.com/problems/roman-to-integer/description/  
# Tags: Hash Map, String, Math  
# Approach: Map each Roman numeral to its integer value and scan from right to left, applying the subtraction rule when a smaller numeral precedes a larger one.  
# Time Complexity: O(n)  
# Space Complexity: O(1)  


class Solution:
    def romanToInt(self, s):
        # mapping of Roman numerals to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # iterate from right to left
        for char in reversed(s):
            value = roman_map[char]
            # if current value is less than the previous, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total


