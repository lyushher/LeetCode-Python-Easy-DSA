# Problem: Valid Palindrome  
# Link: https://leetcode.com/problems/valid-palindrome/description/  
# Tags: Two Pointers, String, Filtering  
# Approach: Filter out non-alphanumeric characters and lowercase the string. Use two pointers to compare from both ends.  
# Time Complexity: O(n)  
# Space Complexity: O(n)



class Solution:
    def isPalindrome(self, s):
        # convert to lowercase and remove non-alphanumeric characters
        cleaned = [c.lower() for c in s if c.isalnum()]
        
        # use two pointers to check for palindrome
        left, right = 0, len(cleaned) - 1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
          
        return True

