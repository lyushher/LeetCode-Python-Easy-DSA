# Problem: Relative Ranks
# Link: https://leetcode.com/problems/relative-ranks/description/
# Tags: Array, Sorting, Hash Map
# Approach: Pair each score with its original index, sort by score descending,
#           and assign "Gold/Silver/Bronze Medal" for top three; for the rest,
#           assign rank numbers as strings. Place results back using original indices.
# Time Complexity: O(n log n)  # sorting
# Space Complexity: O(n)       # result array + index pairs


class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        res = [""] * n

        # (score, index) pairs sorted by score descending
        order = sorted([(s, i) for i, s in enumerate(score)], reverse=True)

        for rank, (_, idx) in enumerate(order, start=1):
            if rank == 1:
                res[idx] = "Gold Medal"
            elif rank == 2:
                res[idx] = "Silver Medal"
            elif rank == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank)

        return res
