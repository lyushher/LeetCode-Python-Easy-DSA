# Problem: Guess Number Higher or Lower
# Link: https://leetcode.com/problems/guess-number-higher-or-lower/description/
# Tags: Binary Search, Interactive
# Approach: Use binary search to minimize the number of guesses. 
#           Adjust search range based on API feedback:
#           - guess(num) returns -1 -> target is lower
#           - guess(num) returns 1 -> target is higher
#           - guess(num) returns 0 -> target found
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def guessNumber(self, n):
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)     # compare guess with target
            
            if res == 0:
                return mid         # correct guess
              
            elif res < 0:
                right = mid - 1    # target is smaller, go left
              
            else:
                left = mid + 1     # target is bigger, go right
