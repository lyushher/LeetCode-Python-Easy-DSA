# Problem: Intersection of Two Arrays II
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# Tags: Array, Hash Table, Two Pointers, Sorting
# Approach: Hash Map (frequency counting from smaller array)
# Time Complexity: O(n + m)  >>>  n = len(nums1), m = len(nums2)
# Space Complexity: O(min(n, m))  >>>  only storing frequencies for the smaller array



from collections import Counter    # import counter to count occurrences of elements in an array

class Solution:
    def intersect(self, nums1, nums2):
        #ensure that nums1 is the smaller array to optimize space usage
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)    #recursive call with the arrays swapped

        #create a frequency map (hash table) for nums1
        count = Counter(nums1)

        result = []  # this will store the final intersection result

        #iterate through each element in nums2
        for num in nums2:
            #if the current number exists in the frequency map and count is more than 0
            if count[num] > 0:
                result.append(num) 
                count[num] -= 1

        return result



