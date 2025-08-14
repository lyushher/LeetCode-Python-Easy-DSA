# Problem: Find Smallest Letter Greater Than Target
# Link: https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
# Tags: Array, Binary Search
# Approach: Binary search ile hedef harften kesin büyük olan ilk harfi bul.
#           Eğer böyle bir harf yoksa (tüm harfler <= target) wrap-around yapıp letters[0] döndür.
# Time Complexity: O(log n)
# Space Complexity: O(1)


class Solution:
    def nextGreatestLetter(self, letters, target):
        left, right = 0, len(letters) - 1
        ans = None
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                ans = letters[mid]    # found a letter > target, store as potential answer
                right = mid - 1      # narrow search to the left to find smaller > target
            else:
                left = mid + 1      # current letter <= target, search in right half

        # if no letter > target, wrap around and return the first letter
        return ans if ans is not None else letters[0]
