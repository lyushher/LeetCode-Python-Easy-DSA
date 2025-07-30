# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/description/
# Tags: Array, Hashing
# Approach: Hash Set (Track seen elements)
# Time Complexity: O(n)
# Space Complexity: O(n)


class Solution:
    def containsDuplicate(self, nums):
        # create a set to keep track of unique elements we've seen
        seen = set()

        # loop through each number in the input list
        for num in nums:
            # if the number is already in the set, it's a duplicate
            if num in seen:
                return True  # Duplicate found, return True
            # otherwise, add the number to the set
            seen.add(num)

        # if loop completes without finding duplicates, return False
        return False


